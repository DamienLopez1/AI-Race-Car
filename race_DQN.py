
import pygame
from PIL import Image
from random import randint
import random
import numpy as np
import math
from collections import namedtuple
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torchvision.transforms as T
import matplotlib.pyplot as plt

###########################
### Training Parameters ###
###########################
batch_size = 128
learning_rate = 0.0001
discount_rate = 0.99
gamma = 0.99
exploration_decay_rate = 0.001
memory_size = 100000
target_update = 100

###############################
### Load Pre-Trained Models ###
###############################

# Uncomment to train from scratch
# model_path = None 

# Path to agent pretrained on Oval track
model_path = 'good targetnet.pck'

# Path to agent pretrained on Polar Bear track
# model_path = 'PBPT targetnet.pck'

#######################################################################
### All the helper functions to make the code cleaner (and shorter) ###
#######################################################################
import utils

###########################################################
## Load all the initial values of race window variables ###
###########################################################
from init_race import * 

AIdirection = 'no'
Experience = namedtuple(
    'Experience',
    ('state', 'action', 'next_state', 'reward')
)

######################################
### All the classes needed for DQN ###
######################################
import dqn_utils

maxdist = ['front','left','right','front right','front left', 'FMR','FML']       
direction = ['up','right','left','donothing']


# Variables for tracking performance
tot_reward = 0
episodes = 0
reward_episode = 0.0
reward_episode_tracker = []
loss_tracker = []
loss = 0
reward = 0.0
cnt = 0
num_gates = 0
gateflag = 'start'
corr_seq = True

exploration_rate = {'start' : 0.95,'gate1' : 0.95,'gate2' : 0.95,'gate3' : 0.95,'gate4' : 0.95,'gate5' : 0.95,'gate6' : 0.95,'gate7' : 0.95,'gate8' : 0.95,'gate9' : 0.95,'gate10' : 0.95,'gate1' : 0.95,'gate11' : 0.95,'gate12' : 0.95,'gate13' : 0.95,'gate14' : 0.95,'gate15' : 0.95,'gate16' : 0.95}
max_exploration_rate = 0.95
min_exploration_rate = 0.1


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
em = dqn_utils.EnvManager(device,screen)
strategy = dqn_utils.EpsilonGreedyStrategy(max_exploration_rate, min_exploration_rate, exploration_decay_rate)
agent = dqn_utils.Agent(strategy, em.num_actions_available(), device)

distance = 1280
nstate = [0,0,0]
msg = ''

#1. Initialise replay memory capcity
memory = dqn_utils.ReplayMemory(memory_size)

#2. Initialise policy network with random weights
policy_net = dqn_utils.DQN(1, 1,dropout= True, dropout_prob= 0.2).to(device)
# Load pre-trained model
if model_path is not None:
    policy_net.load_state_dict(torch.load(model_path))

#3. Clone policy network, call it target network
target_net = dqn_utils.DQN(1, 1,dropout= True, dropout_prob= 0.2).to(device)
target_net.load_state_dict(policy_net.state_dict())
target_net.eval()

optimizer = optim.Adam(params=policy_net.parameters(), lr=learning_rate)

### Episode starts #####################
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # get current position, and rotation of the car
    cstate = [int(x2)+30,int(y2)+30,int(rotater2)]

    ############################################
    ### Get the distances until end of track ###
    ############################################
    present_state, end_of_track_points = utils.get_distances_as_state(cstate, distance, rotater2, trackpil, screen)
    present_points_distances = [present_state[0],present_state[1],present_state[2],present_state[3],present_state[4],present_state[8],present_state[9]]
    state = torch.tensor(present_state, device = device, dtype=torch.float).unsqueeze(0)
    
    #############################################
    ### Select action according to Policy Net ###
    #############################################
    AIchoice = agent.select_action(state, policy_net, exploration_rate[gateflag])
    reward = 0.0

    # Get any manually pressed keys
    pressed = pygame.key.get_pressed()

    # Get color of position of car (black is on track, green is off track)
    try:
        pixcoloour = trackpil[x2 + 30,y2 + 30]
    except IndexError:
        pixcoloour = trackpil[x2,y2]

    # If car on track, reduce speed according to aerodynamics of car
    if pixcoloour == (0, 0, 0, 255):
        topspeed2 = int(carspeed2) / 18 * aero2
        if trackkey == "track5":
            cartopspeed2 = int(carspeed2) / 10 * aero2
            topspeed2 = int(carspeed2) / 10 * aero2
    # If car off the track, give negative reward (-100) and end episode (set cnt to 999)
    else:
        reward = -100.0 
        cnt = 999
    
    # Press 'Esc' to exit game
    if pressed[pygame.K_ESCAPE]:
        pygame.QUIT
        quit()
    
    # Press 'r' to change from exploration to pure exploitation (at 10%)
    if pressed[pygame.K_r]:
        expl = exploration_rate
        exploration_rate = {'start' : 0.1,'gate1' : 0.1,'gate2' : 0.1,'gate3' : 0.1,'gate4' : 0.1,'gate5' : 0.1,'gate6' : 0.1,'gate7' : 0.1,'gate8' : 0.1,'gate9' : 0.1,'gate10' : 0.1,'gate1' : 0.1,'gate11' : 0.1,'gate12' : 0.1,'gate13' : 0.1,'gate14' : 0.1,'gate15' : 0.1,'gate16' : 0.1}
        
    # Press 't' to change from pure exploitation to exploration
    if pressed[pygame.K_t]:
        exploration_rate = expl #{'start' : 0.95,'gate1' : 0.95,'gate2' : 0.95,'gate3' : 0.95,'gate4' : 0.95,'gate5' : 0.95,'gate6' : 0.95,'gate7' : 0.95,'gate8' : 0.95,'gate9' : 0.95,'gate10' : 0.95,'gate1' : 0.95,'gate11' : 0.95,'gate12' : 0.95,'gate13' : 0.95,'gate14' : 0.95,'gate15' : 0.95,'gate16' : 0.95}
        
    # Press 'w','d','a' to use human action
    if pressed[pygame.K_w]:
        AIchoice = 0
        AIchoice = torch.tensor([AIchoice]).to(device)
    elif pressed[pygame.K_d]:
        AIchoice = 1
        AIchoice = torch.tensor([AIchoice]).to(device)
    elif pressed[pygame.K_a]:
        AIchoice = 2
        AIchoice = torch.tensor([AIchoice]).to(device)
    

    #########################################
    ### Make the move according to choice ###
    #########################################
    curspeed2, rotater2, x2, y2, reward, carimage3, carimage4,cnt = utils.move(AIchoice, curspeed2, accel2, cartopspeed2, topspeed2, rotater2, x2, y2, carimage3, carimage4, reward, handling2,cnt)
    
    #4.3 Observe reward and next state
    nstate = [int(x2)+30,int(y2)+30,int(rotater2)]

    #########################################
    ### check if car passes reward gates  ###
    #########################################
    cstate, nstate, reward, corr_seq, gateflag, cnt, tot_reward, reward_episode, num_gates = utils.check_reward_gates(cstate, nstate, rewardgate1, rewardgate2, rewardgate3, rewardgate4, rewardgate5, rewardgate6, rewardgate7,rewardgate8, rewardgate9, rewardgate10,rewardgate11, rewardgate12, rewardgate13, rewardgate14, rewardgate15, rewardgate16, reward, corr_seq, gateflag, cnt, tot_reward, reward_episode, num_gates)
    reward = torch.tensor([reward], device=device)
       
    ############################################
    ### Get the distances until end of track ###
    ############################################
    future_state, end_of_track_points = utils.get_distances_as_state(nstate, distance, rotater2, trackpil, screen)           
    next_state = torch.tensor(future_state, device = device, dtype=torch.float).unsqueeze(0)
    
    forward_points_distances = [future_state[0],future_state[1],future_state[2],future_state[3],future_state[4],future_state[8],future_state[9]]

    # If action results in the forward direction being the maximum distance, add reward of 20
    if np.argmax(forward_points_distances) == 0:
        reward +=20
        reward_episode += 20 
        
    # If the agent made the correct choice to turn or accelerate add 10 to the reward    
    if np.argmax(present_points_distances) == 0 and AIchoice == 0:
        reward +=10
        msg = 'Correct Choice!'
    elif (np.argmax(present_points_distances) == 1 or np.argmax(present_points_distances) == 4 or np.argmax(present_points_distances) == 6) and AIchoice == 2:
        reward +=10
        msg = 'Correct Choice!'
    elif (np.argmax(present_points_distances) == 2 or np.argmax(present_points_distances) == 3 or np.argmax(present_points_distances) == 5) and AIchoice == 1:
        reward +=10
        msg = 'Correct Choice!'
    else:
        msg = 'Bad choice'
        
        
    #4.4 Store experience in replay memory
    memory.push(Experience(state, AIchoice, next_state, reward))

    #4.5 Check to see if memeory stack has enough experiences to fill a batch
    if memory.can_provide_sample(batch_size):
        
        # retrieve experiences from batch
        experiences = memory.sample(batch_size)
        states, actions, rewards, next_states = dqn_utils.extract_tensors(experiences)

        # Get Q Values from policy and target network
        current_q_values = dqn_utils.QValues.get_current(policy_net, states, actions)
        next_q_values = dqn_utils.QValues.get_next(target_net, next_states)
        target_q_values = (next_q_values * gamma) + rewards

        # Calculate Loss and back propagate
        loss = F.mse_loss(current_q_values, target_q_values.unsqueeze(1))
        optimizer.zero_grad()
        loss.backward()
        #torch.nn.utils.clip_grad_norm_(policy_net.parameters(), 5)
        optimizer.step()
            
    cnt+=1
    
    ### Reset envrionment at end of episode ###
    if cnt == 1000:# or num_gates==6: #End of Episode conditions
     
        curspeed2 = 0
        num_gates = 0
        episodes+=1

        # random starting position for the next episode
        x2,y2,rotater2,gateflag = random.choice(init_pos)
        
        #4.9 Update and Save target network if target_update has been reached
        if episodes % target_update == 0:
            target_net.load_state_dict(policy_net.state_dict())
            torch.save(target_net.state_dict(), './targetnet.pck')
        
        #Exploration rate decay
        exploration_rate[gateflag] = min_exploration_rate + \
            (max_exploration_rate - min_exploration_rate) * np.exp(-exploration_decay_rate*episodes)

        print('episodes: ', episodes, 'Total Reward: ', tot_reward)

        
        # Metric Trackers
        reward_episode_tracker.append(reward_episode)
        loss_tracker.append(loss)
        plt.plot(loss_tracker)
        plt.plot(reward_episode_tracker)
        plt.show()
        reward = 0.0
        reward_episode = 0.0
        cnt = 0
        corr_seq = True
    ####### Episode ends ########
        

    #################################
    #### Drawing and rendering ######
    #################################
    
    screen.blit(trackimage, (0,0))
    rewardgate1.draw(screen)
    rewardgate8.draw(screen)
    rewardgate9.draw(screen)
    rewardgate2.draw(screen)
    rewardgate10.draw(screen)
    rewardgate11.draw(screen)
    rewardgate3.draw(screen)
    rewardgate12.draw(screen)
    rewardgate4.draw(screen)
    rewardgate13.draw(screen)
    rewardgate14.draw(screen)
    rewardgate5.draw(screen)
    rewardgate15.draw(screen)
    rewardgate16.draw(screen)
    rewardgate6.draw(screen)
    rewardgate7.draw(screen)
    
    screen.blit(carimage4, (x2,y2))
    pygame.draw.rect(screen, (0,255,0), (x2+30,y2+30,10,10))

    ##########################################################
    ### Show the points that the car detects end of track ####
    ##########################################################
    for i in range(len(end_of_track_points)):
        pygame.draw.rect(screen, (0,0,255), end_of_track_points[i])
        
    #screen.blit(carimage2, (x,y))
    if finished:
        screen.blit(donel, (620, 7340))
        
    txtreward = font.render('Reward:'  + str(reward),1,(255,255,255))
    text2 = font.render('Episodes:'  + str(episodes),1,(255,255,255))
    text3 = font.render('Total Reward:'  + str(tot_reward),1,(255,255,255))
    xy = font.render('X,Y:' + str(x2) + ',' + str(y2),1,(255,255,255))
    ExplRtext = font.render('Exploration Rate:' + str(agent.rate),1,(255,255,255))
    text6 = font.render('Cnt:' + str(cnt),1,(255,255,255))
    reward_episode_txt = font.render('Current Reward:'  + str(reward_episode),1,(255,255,255))
    maxdisttext = font.render('Max dist:'  + str(maxdist[np.argmax(forward_points_distances)]),1,(255,255,255))
    choicemsg = font.render('Good Coice:'  + str(msg),1,(255,255,255))
     
    screen.blit(text3,(500,60))
    screen.blit(txtreward,(500,20))
    screen.blit(reward_episode_txt,(500,40))
    screen.blit(xy,(500,80))
    screen.blit(text2,(500,100))
    screen.blit(ExplRtext,(500,120))
    screen.blit(text6,(500,140))
    screen.blit(maxdisttext,(200,20))
    screen.blit(choicemsg,(200,40))

    #ANND, GO!
    pygame.display.flip()
    clock.tick(clockspeed)
    
#### TRAINING ENDS ####