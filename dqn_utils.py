import pygame
from PIL import Image
import random
import numpy as np
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as T
from collections import namedtuple

Experience = namedtuple(
    'Experience',
    ('state', 'action', 'next_state', 'reward')
)

class ReplayMemory():
    def __init__(self, capacity):
        self.capacity = capacity
        self.memory = []
        self.push_count = 0
         
    def push(self, experience):
        if len(self.memory) < self.capacity:
            self.memory.append(experience)
        else:
            self.memory[self.push_count % self.capacity] = experience
        self.push_count += 1

    def sample(self, batch_size):
        return random.sample(self.memory, batch_size)

    def can_provide_sample(self, batch_size):
        return len(self.memory) >= batch_size


class DQN(nn.Module):
    def __init__(self, img_height, img_width,dropout = False,dropout_prob = 0.5):
        super(DQN,self).__init__()
        
        self.dropout = dropout
        self.dropout_prob = dropout_prob 
        
        self.fc1 = nn.Linear(in_features=img_height*img_width*10, out_features=64)
        self.fc2 = nn.Linear(in_features=64, out_features=32)
        self.fc3 = nn.Linear(in_features = 32, out_features = 32)
        self.out = nn.Linear(in_features=32, out_features=3) 

    def forward(self, t):
        
        if self.dropout:
            t = F.dropout(F.selu(self.fc1(t)), p = self.dropout_prob)
            t = F.dropout(F.selu(self.fc2(t)), p = self.dropout_prob)
            t = F.dropout(F.selu(self.fc3(t)), p = self.dropout_prob)
        else: 
            t = F.selu(self.fc1(t))
            t = F.selu(self.fc2(t))
            t = F.selu(self.fc3(t))
        t = self.out(t)
        return t

class EpsilonGreedyStrategy():
    def __init__(self, start, end, decay):
        self.start = start
        self.end = end
        self.decay = decay
        
        
    def get_exploration_rate(self, current_step):
        return self.end + (self.start - self.end) * \
            math.exp(-1. * current_step * self.decay)
            
class Agent():
    def __init__(self, strategy, num_actions,device):
        self.current_step = 0
        self.strategy = strategy
        self.num_actions = num_actions
        self.device = device
        
        
    def select_action(self, state, policy_net,expl_rate):
        self.rate = expl_rate
        self.current_step += 1

        if self.rate > random.random():                               #this must change to reflect AIchoice(action) 
            action = random.randrange(self.num_actions)
            #print('explore', action)
            return torch.tensor([action]).to(self.device) # explore      
        else:
            with torch.no_grad():
                out = policy_net(state).argmax(dim = 1)  
                return torch.tensor([out]).to(self.device) # exploit


#Tensor Processing    
def extract_tensors(experiences):
    # Convert batch of Experiences to Experience of batches
    batch = Experience(*zip(*experiences))

    t1 = torch.cat(batch.state,dim=0)
    t2 = torch.cat(batch.action)
    t3 = torch.cat(batch.reward)
    t4 = torch.cat(batch.next_state)

    return (t1,t2,t3,t4)   

#Q-value calculator
class QValues():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    @staticmethod
    def get_current(policy_net, states, actions):
        return policy_net(states).gather(dim=1, index=actions.unsqueeze(-1))    
    
    @staticmethod        
    def get_next(target_net, next_states):                
        values = target_net(next_states).max(dim=1)[0].detach()
        return values 
 

class EnvManager():
    def __init__(self, device, screen):
        self.device = device
        self.current_screen = None
        self.done = False
        self.screen = screen
    #Wrapped functions
    
    def num_actions_available(self):
        return 3
    #Starting an episode
    def just_starting(self):
        return self.current_screen is None
    
    #Getting the state of the environment
    def get_state(self):

        s2 = self.get_processed_screen()
        self.current_screen = s2
        return s2 #- s1
    
    #Get processed screen dimensions   
    def get_screen_height(self):
        screen = self.get_processed_screen()
        return screen.shape[2]
    
    def get_screen_width(self):
        screen = self.get_processed_screen()
        return screen.shape[3]
    
    #Processing the screen image
    def get_processed_screen(self):
 
        screen = pygame.surfarray.array3d(self.screen).transpose((2,0,1))
        return self.transform_screen_data(screen)
    
    #Crop screen image
    def crop_screen(self, screen):
        return screen
        
    
    #Convert and rescale screen image data
    
    def transform_screen_data(self, screen):       
        # Convert to float, rescale, convert to tensor
        screen = np.ascontiguousarray(screen, dtype=np.float32) / 255
        screen = torch.from_numpy(screen)
        
        # Use torchvision package to compose image transforms
      
        resize = T.Compose([
            T.ToPILImage()
            ,T.Resize((40,90))
            ,T.ToTensor()
        ])
    
        return resize(screen).unsqueeze(0).to(self.device) # add a batch dimension (BCHW)
