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
import time

###########################
### Training Parameters ###
###########################
learning_rate = 0.0001
discount_rate = 0.99
exploration_decay_rate = 0.05
max_episode_limit = 40


###############################
### Load Pre-Trained Models ###
###############################

# Uncomment to train from scratch
# model_path = None 

# Path to agent pretrained on Oval track and trackers
q_table_name = 'good q_tbl.npy'
trackers_name = 'trackers.npy'

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
steps_tracker = []
gates_tracker = []
loss = 0
reward = 0.0
cnt = 0
num_gates = 0
gateflag = 'start'
corr_seq = True
lap_done = 0
total_steps = 0
new_gates = 0

exploration_rate = {'start' : 0.95,'gate1' : 0.95,'gate2' : 0.95,'gate3' : 0.95,'gate4' : 0.95,'gate5' : 0.95,'gate6' : 0.95,'gate7' : 0.95,'gate8' : 0.95,'gate9' : 0.95,'gate10' : 0.95,'gate1' : 0.95,'gate11' : 0.95,'gate12' : 0.95,'gate13' : 0.95,'gate14' : 0.95,'gate15' : 0.95,'gate16' : 0.95}
max_exploration_rate = 0.95
min_exploration_rate = 0.1
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

### Create the Q-table and Reward matrix ###
q_table = np.zeros((7,3))
r_table = np.zeros((7,3))
r_table= [[10,0,0],[0,0,10],[0,10,0],[0,10,0],[0,0,10],[0,10,0],[0,0,10]]

# Load pretrained Q-table if exists
if q_table_name is not None:
    q_table = np.load(q_table_name)

distance = 1280
nstate = [0,0,0]
msg = ''


### Episode starts #####################
while not done or episodes < max_episode_limit:
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
    
    ##########################################
    ### Select action according to Q-Table ###
    ##########################################
    # If exploration threshold is not surpassed, choose action from q-table, otherwise choose random action
    exploration_rate_threshold = random.uniform(0, 1)
    if exploration_rate_threshold > exploration_rate[gateflag]:
        #AIchoice = np.argmax(q_table[next_state[0],next_state[1],:]) #exploit without rotation
        AIchoice = np.argmax(q_table[np.argmax(present_points_distances)]) #exploit with rotation        
    else:
        AIchoice = random.randrange(3)
    reward = 0.0

    # Get any manually pressed keys
    pressed = pygame.key.get_pressed()

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
    tmp_gate = gateflag
    cstate, nstate, reward, corr_seq, gateflag, cnt, tot_reward, reward_episode, num_gates = utils.check_reward_gates(cstate, nstate, rewardgate1, rewardgate2, rewardgate3, rewardgate4, rewardgate5, rewardgate6, rewardgate7,rewardgate8, rewardgate9, rewardgate10,rewardgate11, rewardgate12, rewardgate13, rewardgate14, rewardgate15, rewardgate16, reward, corr_seq, gateflag, cnt, tot_reward, reward_episode, num_gates)
    # if gate has been passed, then add to counter
    if gateflag != tmp_gate: new_gates += 1
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
        reward_episode += 10 
        msg = 'Correct Choice!'
    elif (np.argmax(present_points_distances) == 1 or np.argmax(present_points_distances) == 4 or np.argmax(present_points_distances) == 6) and AIchoice == 2:
        reward +=10
        reward_episode += 10 
        msg = 'Correct Choice!'
    elif (np.argmax(present_points_distances) == 2 or np.argmax(present_points_distances) == 3 or np.argmax(present_points_distances) == 5) and AIchoice == 1:
        reward +=10
        reward_episode += 10 
        msg = 'Correct Choice!'
    else:
        msg = 'Bad choice'
    
    ### Update Q-table values
    if cnt > 0:
        q_table[np.argmax(present_points_distances),AIchoice] = q_table[np.argmax(present_points_distances),AIchoice] * (1 - learning_rate) + \
    learning_rate * (reward + discount_rate * np.max(q_table[np.argmax(forward_points_distances)]))
    
    cnt+=1
    total_steps +=1 

    ### Reset envrionment at end of episode ###
    if lap_done == 1 or cnt>= 200 or total_steps >= 1000:# or num_gates==6: #End of Episode conditions

        curspeed2 = 0
        num_gates = 0

        # random starting position for the next episode
        x2,y2,rotater2,gateflag = random.choice(init_pos)

        episodes+=1

        # Save Q-table
        np.save(q_table_name, q_table)
        
        #tot_reward += reward
        print('episodes: ', episodes, 'Total Reward: ', reward_episode)

        #Exploration rate decay
        exploration_rate[gateflag] = min_exploration_rate + \
            (max_exploration_rate - min_exploration_rate) * np.exp(-exploration_decay_rate*episodes)
        
        # Metric Trackers
        reward_episode_tracker.append(reward_episode)
        loss_tracker.append(loss)
        steps_tracker.append(total_steps)
        gates_tracker.append(new_gates)
        reward = 0.0
        reward_episode = 0.0 
        cnt = 0
        lap_done = 0
        total_steps = 0
        new_gates = 0
        corr_seq = True
        
        plt.plot(loss_tracker)
        plt.plot(reward_episode_tracker)
        plt.plot(steps_tracker)
        plt.show()

        # Save Metrics
        np.save(trackers_name, (loss_tracker, reward_episode_tracker, steps_tracker, gates_tracker))
    ####### Episode ends ########

         

    #################################
    #### Drawing and rendering ######
    
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
    ExplRtext = font.render('Exploration Rate:' + str(exploration_rate[gateflag]),1,(255,255,255))
    text6 = font.render('Cnt:' + str(cnt),1,(255,255,255))
    reward_episode_txt = font.render('Current Reward:'  + str(reward_episode),1,(255,255,255))
    maxdisttext = font.render('Max dist:'  + str(maxdist[np.argmax(forward_points_distances)]),1,(255,255,255))
    choicemsg = font.render('Good Coice:'  + str(msg),1,(255,255,255))
     
    #screen.blit(text5,(500,40))
    screen.blit(text3,(500,60))
    screen.blit(txtreward,(500,20))
    screen.blit(reward_episode_txt,(500,40))
    screen.blit(xy,(500,80))
    screen.blit(text2,(500,100))
    
    screen.blit(ExplRtext,(500,120))
    screen.blit(text6,(500,140))
    #print(to_reward/episodes)
    screen.blit(maxdisttext,(200,20))
    screen.blit(choicemsg,(200,40))

    #ANND, GO!
    pygame.display.flip()
    clock.tick(clockspeed)

#### TRAINING ENDS ####

