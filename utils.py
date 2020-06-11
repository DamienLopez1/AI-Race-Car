import pygame
import math

def move(AIchoice, curspeed2, accel2, cartopspeed2, topspeed2, rotater2, x2, y2, carimage3, carimage4, reward, handling2,cnt):
    rot2 = 0
    # 0: forward (a.k.a. 'up')
    if AIchoice == 0:
        amount = 0
        
        curspeed2 = curspeed2 + accel2
        #lastdirection = Up
        if curspeed2 >= topspeed2:
            curspeed2 = topspeed2
        if rotater2 <= 90:
            xnow = x2
            if rot2 <= 0:
                amount = 0
            if rot2 >= 0:
                amount = rotater2 / 90
            segspeed2 = amount * curspeed2
            x2 = xnow - segspeed2
        if rotater2 >= 90:
            if rotater2 <= 180:
                xnow = x2
                rot2 = 180 - rotater2
                amount = rot2 / 90
                segspeed2 = amount * curspeed2
                x2 = xnow - segspeed2
        if rotater2 >= 90.01:
            if rotater2 <= 180:
                ynow = y2
                rot2 = rotater2 - 90
                amount = rot2 / 90
                segspeed2 = amount * curspeed2
                y2 = ynow + segspeed2
        if rotater2 >= 180:
            if rotater2 <= 270:
                ynow = y2
                rot2 = 270 - rotater2
                amount = rot2 / 90
                segspeed2 = amount * curspeed2
                y2 = ynow + segspeed2
        if rotater2 >= 180:
            if rotater2 <= 270:
                xnow = x2
                rot2 = rotater2 - 180
                amount = rot2 / 90
                segspeed2 = amount * curspeed2
                x2 = xnow + segspeed2
        if rotater2 >= 270:
            if rotater2 <= 360:
                xnow = x2
                rot2 = rotater2 - 270
                rot3 = -90 + rot2
                if rot3 >= 0:
                    amount = 1
                if rot3 <= 0:
                    amount = rot3 / -90
                segspeed2 = amount * curspeed2
                x2 = xnow + segspeed2
        if rotater2 >= 270:
            if rotater2 <= 360:
                ynow = y2
                rot2 = rotater2 - 270
                amount = rot2 / 90
                segspeed2 = amount * curspeed2
                y2 = ynow - segspeed2
        if rotater2 <= 89.9:
            ynow = y2
            rot2 = -90 + rotater2
            if rot2 >= 0:
                amount = 1
            if rot2 <= 0:
                amount = rot2 / -90
            segspeed2 = amount * curspeed2
            y2 = ynow - segspeed2
    if AIchoice == 2:
        #lastdirection = Left
        if curspeed2 >= topspeed2:
            curspeed2 = topspeed2
        if curspeed2 >= 0.1:
            rotater2 += handling2
        #if not pressed [pygame.K_w]:
        #if not AIdirection == 'up':  
        if not AIchoice == 0:
            if rotater2 <= 90:
                xnow = x2
                if rot2 <= 0:
                    amount = 0
                if rot2 >= 0:
                    amount = rotater2 / 90
                segspeed2 = amount * curspeed2
                x2 = xnow - segspeed2
            if rotater2 >= 90:
                if rotater2 <= 180:
                    xnow = x2
                    rot2 = 180 - rotater2
                    amount = rot2 / 90
                    segspeed2 = amount * curspeed2
                    x2 = xnow - segspeed2
            if rotater2 >= 90.01:
                if rotater2 <= 180:
                    ynow = y2
                    rot2 = rotater2 - 90
                    amount = rot2 / 90
                    segspeed2 = amount * curspeed2
                    y2 = ynow + segspeed2
            if rotater2 >= 180:
                if rotater2 <= 270:
                    ynow = y2
                    rot2 = 270 - rotater2
                    amount = rot2 / 90
                    segspeed2 = amount * curspeed2
                    y2 = ynow + segspeed2
            if rotater2 >= 180:
                if rotater2 <= 270:
                    xnow = x2
                    rot2 = rotater2 - 180
                    amount = rot2 / 90
                    segspeed2 = amount * curspeed2
                    x2 = xnow + segspeed2
            if rotater2 >= 270:
                if rotater2 <= 359.9:
                    xnow = x2
                    rot2 = rotater2 - 270
                    rot3 = -90 + rot2
                    if rot3 >= 0:
                        amount = 1
                    if rot3 <= 0:
                        amount = rot3 / -90
                    segspeed2 = amount * curspeed2
                    x2 = xnow + segspeed2
            if rotater2 >= 270:
                if rotater2 <= 360:
                    ynow = y2
                    rot2 = rotater2 - 270
                    amount = rot2 / 90
                    segspeed2 = amount * curspeed2
                    y2 = ynow - segspeed2
            if rotater2 <= 89.9:
                ynow = y2
                rot2 = -90 + rotater2
                if rot2 >= 0:
                    amount = 1
                if rot2 <= 0:
                    amount = rot2 / -90
                segspeed2 = amount * curspeed2
                y2 = ynow - segspeed2
        if rotater2 >= 360:
            rotater2 = 0
        if rotater2 <= 0:
            rotater2 = 0
        carimage4 = pygame.transform.rotate(carimage3, rotater2)
        #if pressed[pygame.K_w]:
        #if AIdirection == 'up':
        #if AIchoice == 0:
            #lastdirection = LeftUp
        #if pressed[pygame.K_s]:
        #if AIdirection == 'down':
            #lastdirection = LeftDown
    #if pressed[pygame.K_d]:
    #if AIdirection == 'right':
    if AIchoice == 1:
        #lastdirection = Right
        #if not pressed [pygame.K_w]:
        #if not AIdirection == 'up':
        if not AIchoice == 0:
            if rotater2 <= 90:
                xnow = x2
                if rot2 <= 0:
                    amount = 0
                if rot2 >= 0:
                    amount = rotater2 / 90
                segspeed2 = amount * curspeed2
                x2 = xnow - segspeed2
            if rotater2 >= 90:
                if rotater2 <= 180:
                    xnow = x2
                    rot2 = 180 - rotater2
                    amount = rot2 / 90
                    segspeed2 = amount * curspeed2
                    x2 = xnow - segspeed2
            if rotater2 >= 90.01:
                if rotater2 <= 180:
                    ynow = y2
                    rot2 = rotater2 - 90
                    amount = rot2 / 90
                    segspeed2 = amount * curspeed2
                    y2 = ynow + segspeed2
            if rotater2 >= 180:
                if rotater2 <= 270:
                    ynow = y2
                    rot2 = 270 - rotater2
                    amount = rot2 / 90
                    segspeed2 = amount * curspeed2
                    y2 = ynow + segspeed2
            if rotater2 >= 180:
                if rotater2 <= 270:
                    xnow = x2
                    rot2 = rotater2 - 180
                    amount = rot2 / 90
                    segspeed2 = amount * curspeed2
                    x2 = xnow + segspeed2
            if rotater2 >= 270:
                if rotater2 <= 360:
                    xnow = x2
                    rot2 = rotater2 - 270
                    rot3 = -90 + rot2
                    if rot3 >= 0:
                        amount = 1
                    if rot3 <= 0:
                        amount = rot3 / -90
                    segspeed2 = amount * curspeed2
                    x2 = xnow + segspeed2
            if rotater2 >= 270:
                if rotater2 <= 360:
                    ynow = y2
                    rot2 = rotater2 - 270
                    amount = rot2 / 90
                    segspeed2 = amount * curspeed2
                    y2 = ynow - segspeed2
            if rotater2 <= 89.9:
                ynow = y2
                rot2 = -90 + rotater2
                if rot2 >= 0:
                    amount = 1
                if rot2 <= 0:
                    amount = rot2 / -90
                segspeed2 = amount * curspeed2
                y2 = ynow - segspeed2
        if curspeed2 >= topspeed2:
            curspeed2 = topspeed2
        if curspeed2 >= 0.1:
            rotater2 -= handling2
            if rotater2 >= 360:
                rotater2 = 0
            if rotater2 <= 0:
                rotater2 = 360
        carimage4 = pygame.transform.rotate(carimage3, rotater2)
        #if pressed[pygame.K_w]:
        #if AIdirection == 'up':
        #if AIchoice == 0:
            #lastdirection = RightUp
        #if pressed[pygame.K_s]:
        #if AIdirection == 'down':
            #lastdirection = RightDown
    
    #if pressed[pygame.K_s]:
    if False: #AIdirection == 'down':
        curspeed2 = curspeed2 - braking
        if curspeed2 >= -1.6:
            curspeed2 = curspeed2 - 0.1
        else:
            curspeed2 = -1.5
        if rotater2 <= 90:
            xnow = x2
            if rot2 <= 0:
                amount = 0
            if rot2 >= 0:
                amount = rotater2 / 90
            segspeed2 = amount * curspeed2
            x2 = xnow - segspeed2
        if rotater2 >= 90:
            if rotater2 <= 180:
                xnow = x2
                rot2 = 180 - rotater2
                amount = rot2 / 90
                segspeed2 = amount * curspeed2
                x2 = xnow - segspeed2
        if rotater2 >= 90.01:
            if rotater2 <= 180:
                ynow = y2
                rot2 = rotater2 - 90
                amount = rot2 / 90
                segspeed2 = amount * curspeed2
                y2 = ynow + segspeed2
        if rotater2 >= 180:
            if rotater2 <= 270:
                ynow = y2
                rot2 = 270 - rotater2
                amount = rot2 / 90
                segspeed2 = amount * curspeed2
                y2 = ynow + segspeed2
        if rotater2 >= 180:
            if rotater2 <= 270:
                xnow = x2
                rot2 = rotater2 - 180
                amount = rot2 / 90
                segspeed2 = amount * curspeed2
                x2 = xnow + segspeed2
        if rotater2 >= 270:
            if rotater2 <= 360:
                xnow = x2
                rot2 = rotater2 - 270
                rot3 = -90 + rot2
                if rot3 >= 0:
                    amount = 1
                if rot3 <= 0:
                    amount = rot3 / -90
                segspeed2 = amount * curspeed2
                x2 = xnow + segspeed2
        if rotater2 >= 270:
            if rotater2 <= 360:
                ynow = y2
                rot2 = rotater2 - 270
                amount = rot2 / 90
                segspeed2 = amount * curspeed2
                y2 = ynow - segspeed2
        if rotater2 <= 89.9:
            ynow = y2
            rot2 = -90 + rotater2
            if rot2 >= 0:
                amount = 1
            if rot2 <= 0:
                amount = rot2 / -90
            segspeed2 = amount * curspeed2
            y2 = ynow - segspeed2
    #if not pressed[pygame.K_d]:
    #if not AIdirection == 'right':
    if not AIchoice == 1:
        #if not pressed[pygame.K_a]:
        #if not AIdirection == 'left':
        if not AIchoice == 2:
            #if not pressed[pygame.K_s]:
            if True: #not AIdirection == 'down':
                #if not pressed[pygame.K_w]:
                #if not AIdirection == 'up':
                if not AIchoice == 0:
                    #if not pressed[pygame.K_q]:
                        if curspeed2 >= 0.19:
                            curspeed2 = curspeed2 - 0.1
                        if curspeed2 <= -0.1:
                            curspeed2 = curspeed2 + 0.1
                        if curspeed2 >= -0.1:
                            if curspeed2 <= 0.19:
                                curspeed2 = 0
                        if rotater2 <= 90:
                            xnow = x2
                            if rot2 <= 0:
                                amount = 0
                            if rot2 >= 0:
                                amount = rotater2 / 90
                            segspeed2 = amount * curspeed2
                            x2 = xnow - segspeed2
                        if rotater2 >= 90:
                            if rotater2 <= 180:
                                xnow = x2
                                rot2 = 180 - rotater2
                                amount = rot2 / 90
                                segspeed2 = amount * curspeed2
                                x2 = xnow - segspeed2
                        if rotater2 >= 90.01:
                            if rotater2 <= 180:
                                ynow = y2
                                rot2 = rotater2 - 90
                                amount = rot2 / 90
                                segspeed2 = amount * curspeed2

                                y2 = ynow + segspeed2
                        if rotater2 >= 180:
                            if rotater2 <= 270:
                                ynow = y2
                                rot2 = 270 - rotater2
                                amount = rot2 / 90
                                segspeed2 = amount * curspeed2
                                y2 = ynow + segspeed2
                        if rotater2 >= 180:
                            if rotater2 <= 270:
                                xnow = x2
                                rot2 = rotater2 - 180
                                amount = rot2 / 90
                                segspeed2 = amount * curspeed2
                                x2 = xnow + segspeed2
                        if rotater2 >= 270:
                            if rotater2 <= 360:
                                xnow = x2
                                rot2 = rotater2 - 270
                                rot3 = -90 + rot2
                                if rot3 >= 0:
                                    amount = 1
                                if rot3 <= 0:
                                    amount = rot3 / -90
                                segspeed2 = amount * curspeed2
                                x2 = xnow + segspeed2
                        if rotater2 >= 270:
                            if rotater2 <= 360:
                                ynow = y2
                                rot2 = rotater2 - 270
                                amount = rot2 / 90
                                segspeed2 = amount * curspeed2
                                y2 = ynow - segspeed2
                        if rotater2 <= 89.9:
                            ynow = y2
                            rot2 = -90 + rotater2
                            if rot2 >= 0:
                                amount = 1
                            if rot2 <= 0:
                                amount = rot2 / -90
                            segspeed2 = amount * curspeed2
                            y2 = ynow - segspeed2
    #movement
    #Collision/OOB detection
    if x2 >=1220:
        x2 = 1218
        reward = -100.0
        cnt = 999
    if x2 <= -1:
        x2 = 2
        reward = -100.0
        cnt = 999
    if y2 >= 660:
        y2 = 658
        reward = -100.0
        cnt = 999
    if y2 <= -1:
        y2 = 2
        reward = -100.0
        cnt = 999

    return curspeed2, rotater2, x2, y2, reward, carimage3, carimage4,cnt

def check_reward_gates(cstate, nstate, rewardgate1, rewardgate2, rewardgate3, rewardgate4, rewardgate5, rewardgate6, rewardgate7,rewardgate8, rewardgate9, rewardgate10,rewardgate11, rewardgate12, rewardgate13, rewardgate14, rewardgate15, rewardgate16, reward, corr_seq, gateflag, cnt, tot_reward, reward_episode, num_gates):
    if nstate[1] <= rewardgate1.hitbox[1] + rewardgate1.hitbox[3] and nstate[1] >= rewardgate1.hitbox[1] and nstate != cstate and gateflag != 'gate1': #this is for leading edge being within the reward gate in the y plane
        if nstate[0] >= rewardgate1.hitbox[0] and nstate[0] <= rewardgate1.hitbox[0] + rewardgate1.hitbox[2] and nstate != cstate: # this is for the outer edges of the car having to be completley within the reward gate to receive a reward
            if gateflag == 'start' and corr_seq == True:
                #reward = 100.0
                num_gates += 1
                reward = 10.0*num_gates
                cnt = 0
            else: 
                reward = 0.5
                corr_seq = False
            gateflag = 'gate1'
            tot_reward += reward
            reward_episode += reward
            
    if nstate[1] <= rewardgate2.hitbox[1] + rewardgate2.hitbox[3] and nstate[1] >= rewardgate2.hitbox[1] and nstate != cstate and gateflag != 'gate2': #this is for leading edge being within the reward gate in the y plane
        if nstate[0] >= rewardgate2.hitbox[0] and nstate[0] <= rewardgate2.hitbox[0] + rewardgate2.hitbox[2] and nstate != cstate: # this is for the outer edges of the car having to be completley within the reward gate to receive a reward
            if gateflag == 'gate1' and corr_seq == True:
                #reward = 100.0
                num_gates += 1
                reward = 10.0*num_gates
                cnt = 0
            else: 
                reward = 0.5
                corr_seq = False
            gateflag = 'gate2'
            tot_reward += reward
            reward_episode += reward
    
    if nstate[1] <= rewardgate3.hitbox[1] + rewardgate3.hitbox[3] and nstate[1] >= rewardgate3.hitbox[1] and nstate != cstate and gateflag != 'gate3': #this is for leading edge being within the reward gate in the y plane
        if nstate[0] >= rewardgate3.hitbox[0] and nstate[0] <= rewardgate3.hitbox[0] + rewardgate3.hitbox[2] and nstate != cstate: # this is for the outer edges of the car having to be completley within the reward gate to receive a reward
            if gateflag == 'gate2' and corr_seq == True:
                #reward = 100.0
                num_gates += 1
                reward = 10.0*num_gates
                cnt = 0
            else: 
                reward = 0.5
                corr_seq = False
            gateflag = 'gate3' 
            tot_reward += reward
            reward_episode += reward
    
    if nstate[1] <= rewardgate4.hitbox[1] + rewardgate4.hitbox[3] and nstate[1] >= rewardgate4.hitbox[1] and nstate != cstate and gateflag != 'gate4': #this is for leading edge being within the reward gate in the y plane
        if nstate[0] >= rewardgate4.hitbox[0] and nstate[0] <= rewardgate4.hitbox[0] + rewardgate4.hitbox[2] and nstate != cstate: # this is for the outer edges of the car having to be completley within the reward gate to receive a reward
            if gateflag == 'gate3' and corr_seq == True:
                #reward = 100.0
                num_gates += 1
                reward = 10.0*num_gates
                cnt = 0
            else: 
                reward = 0.5
                corr_seq = False
            gateflag = 'gate4'
            tot_reward += reward
            reward_episode += reward
    
    if nstate[1] <= rewardgate5.hitbox[1] + rewardgate5.hitbox[3] and nstate[1] >= rewardgate5.hitbox[1] and nstate != cstate and gateflag != 'gate5': #this is for leading edge being within the reward gate in the y plane
        if nstate[0] >= rewardgate5.hitbox[0] and nstate[0] <= rewardgate5.hitbox[0] + rewardgate5.hitbox[2] and nstate != cstate: # this is for the outer edges of the car having to be completley within the reward gate to receive a reward
            if gateflag == 'gate4' and corr_seq == True:
                #reward = 100.0
                num_gates += 1
                reward = 10.0*num_gates
                cnt = 0
            else: 
                reward = 0.5
                corr_seq = False
            gateflag = 'gate5' 
            tot_reward += reward
            reward_episode += reward
    
    if nstate[1] <= rewardgate6.hitbox[1] + rewardgate6.hitbox[3] and nstate[1] >= rewardgate6.hitbox[1] and nstate != cstate and gateflag != 'gate6': #this is for leading edge being within the reward gate in the y plane
        if nstate[0] >= rewardgate6.hitbox[0] and nstate[0] <= rewardgate6.hitbox[0] + rewardgate6.hitbox[2] and nstate != cstate: # this is for the outer edges of the car having to be completley within the reward gate to receive a reward
            if gateflag == 'gate5' and corr_seq == True:
                #reward = 100.0
                num_gates += 1
                reward = 10.0*num_gates
                cnt = 0
            else: 
                reward = 0.5
                corr_seq = False
            gateflag = 'gate6'
            tot_reward += reward
            reward_episode += reward
    
    if nstate[1] <= rewardgate7.hitbox[1] + rewardgate7.hitbox[3] and nstate[1] >= rewardgate7.hitbox[1] and nstate != cstate and gateflag != 'gate7': #this is for leading edge being within the reward gate in the y plane
        if nstate[0] >= rewardgate7.hitbox[0] and nstate[0] <= rewardgate7.hitbox[0] + rewardgate7.hitbox[2] and nstate != cstate: # this is for the outer edges of the car having to be completley within the reward gate to receive a reward
            if gateflag == 'gate6' and corr_seq == True:
                #reward = 100.0
                num_gates += 1
                reward = 10.0*num_gates
                cnt = 0
            else: 
                reward = 0.5
                corr_seq = False
            gateflag = 'gate7'
            tot_reward += reward
            reward_episode += reward
    
    if nstate[1] <= rewardgate8.hitbox[1] + rewardgate8.hitbox[3] and nstate[1] >= rewardgate8.hitbox[1] and nstate != cstate and gateflag != 'gate8': #this is for leading edge being within the reward gate in the y plane
        if nstate[0] >= rewardgate8.hitbox[0] and nstate[0] <= rewardgate8.hitbox[0] + rewardgate8.hitbox[2] and nstate != cstate: # this is for the outer edges of the car having to be completley within the reward gate to receive a reward
            if gateflag == 'gate7' and corr_seq == True:
                #reward = 100.0
                num_gates += 1
                reward = 10.0*num_gates
                cnt = 0
            else: 
                reward = 0.5
                corr_seq = False
            gateflag = 'gate8'
            tot_reward += reward
            reward_episode += reward
            
    if nstate[1] <= rewardgate9.hitbox[1] + rewardgate9.hitbox[3] and nstate[1] >= rewardgate9.hitbox[1] and nstate != cstate and gateflag != 'gate9': #this is for leading edge being within the reward gate in the y plane
        if nstate[0] >= rewardgate9.hitbox[0] and nstate[0] <= rewardgate9.hitbox[0] + rewardgate9.hitbox[2] and nstate != cstate: # this is for the outer edges of the car having to be completley within the reward gate to receive a reward
            if gateflag == 'gate8' and corr_seq == True:
                #reward = 100.0
                num_gates += 1
                reward = 10.0*num_gates
                cnt = 0
            else: 
                reward = 0.5
                corr_seq = False
            gateflag = 'gate9'
            tot_reward += reward
            reward_episode += reward
            
    if nstate[1] <= rewardgate10.hitbox[1] + rewardgate10.hitbox[3] and nstate[1] >= rewardgate10.hitbox[1] and nstate != cstate and gateflag != 'gate10': #this is for leading edge being within the reward gate in the y plane
        if nstate[0] >= rewardgate10.hitbox[0] and nstate[0] <= rewardgate10.hitbox[0] + rewardgate10.hitbox[2] and nstate != cstate: # this is for the outer edges of the car having to be completley within the reward gate to receive a reward
            if gateflag == 'gate9' and corr_seq == True:
                #reward = 100.0
                num_gates += 1
                reward = 10.0*num_gates
                cnt = 0
            else: 
                reward = 0.5
                corr_seq = False
            gateflag = 'gate10'
            tot_reward += reward
            reward_episode += reward
    
    if nstate[1] <= rewardgate11.hitbox[1] + rewardgate11.hitbox[3] and nstate[1] >= rewardgate11.hitbox[1] and nstate != cstate and gateflag != 'gate11': #this is for leading edge being within the reward gate in the y plane
        if nstate[0] >= rewardgate11.hitbox[0] and nstate[0] <= rewardgate11.hitbox[0] + rewardgate11.hitbox[2] and nstate != cstate: # this is for the outer edges of the car having to be completley within the reward gate to receive a reward
            if gateflag == 'gate10' and corr_seq == True:
                #reward = 100.0
                num_gates += 1
                reward = 10.0*num_gates
                cnt = 0
            else: 
                reward = 0.5
                corr_seq = False
            gateflag = 'gate11'
            tot_reward += reward
            reward_episode += reward
            
    if nstate[1] <= rewardgate12.hitbox[1] + rewardgate12.hitbox[3] and nstate[1] >= rewardgate12.hitbox[1] and nstate != cstate and gateflag != 'gate12': #this is for leading edge being within the reward gate in the y plane
        if nstate[0] >= rewardgate12.hitbox[0] and nstate[0] <= rewardgate12.hitbox[0] + rewardgate12.hitbox[2] and nstate != cstate: # this is for the outer edges of the car having to be completley within the reward gate to receive a reward
            if gateflag == 'gate11' and corr_seq == True:
                #reward = 100.0
                num_gates += 1
                reward = 10.0*num_gates
                cnt = 0
            else: 
                reward = 0.5
                corr_seq = False
            gateflag = 'gate12'
            tot_reward += reward
            reward_episode += reward
    
    if nstate[1] <= rewardgate13.hitbox[1] + rewardgate13.hitbox[3] and nstate[1] >= rewardgate13.hitbox[1] and nstate != cstate and gateflag != 'gate13': #this is for leading edge being within the reward gate in the y plane
        if nstate[0] >= rewardgate13.hitbox[0] and nstate[0] <= rewardgate13.hitbox[0] + rewardgate13.hitbox[2] and nstate != cstate: # this is for the outer edges of the car having to be completley within the reward gate to receive a reward
            if gateflag == 'gate12' and corr_seq == True:
                #reward = 100.0
                num_gates += 1
                reward = 10.0*num_gates
                cnt = 0
            else: 
                reward = 0.5
                corr_seq = False
            gateflag = 'gate13'
            tot_reward += reward
            reward_episode += reward
    
    if nstate[1] <= rewardgate14.hitbox[1] + rewardgate14.hitbox[3] and nstate[1] >= rewardgate14.hitbox[1] and nstate != cstate and gateflag != 'gate14': #this is for leading edge being within the reward gate in the y plane
        if nstate[0] >= rewardgate14.hitbox[0] and nstate[0] <= rewardgate14.hitbox[0] + rewardgate14.hitbox[2] and nstate != cstate: # this is for the outer edges of the car having to be completley within the reward gate to receive a reward
            if gateflag == 'gate13' and corr_seq == True:
                #reward = 100.0
                num_gates += 1
                reward = 10.0*num_gates
                cnt = 0
            else: 
                reward = 0.5
                corr_seq = False
            gateflag = 'gate14'
            tot_reward += reward
            reward_episode += reward
            
    if nstate[1] <= rewardgate15.hitbox[1] + rewardgate15.hitbox[3] and nstate[1] >= rewardgate15.hitbox[1] and nstate != cstate and gateflag != 'gate15': #this is for leading edge being within the reward gate in the y plane
        if nstate[0] >= rewardgate15.hitbox[0] and nstate[0] <= rewardgate15.hitbox[0] + rewardgate15.hitbox[2] and nstate != cstate: # this is for the outer edges of the car having to be completley within the reward gate to receive a reward
            if gateflag == 'gate14' and corr_seq == True:
                #reward = 100.0
                num_gates += 1
                reward = 10.0*num_gates
                cnt = 0
            else: 
                reward = 0.5
                corr_seq = False
            gateflag = 'gate15'
            tot_reward += reward
            reward_episode += reward
    
    if nstate[1] <= rewardgate16.hitbox[1] + rewardgate16.hitbox[3] and nstate[1] >= rewardgate16.hitbox[1] and nstate != cstate and gateflag != 'start': #this is for leading edge being within the reward gate in the y plane
        if nstate[0] >= rewardgate16.hitbox[0] and nstate[0] <= rewardgate16.hitbox[0] + rewardgate16.hitbox[2] and nstate != cstate: # this is for the outer edges of the car having to be completley within the reward gate to receive a reward
            if gateflag == 'gate15'and corr_seq == True:
                #reward = 100.0
                num_gates += 1
                reward = 10.0*num_gates
                #lap_done = 1
                cnt = 0
            else: 
                #reward = 0.5
                corr_seq = False
            gateflag = 'start'
            corr_seq = True
            tot_reward += reward
            reward_episode += reward
    
    
    

    return cstate, nstate, reward, corr_seq, gateflag, cnt, tot_reward, reward_episode, num_gates

def get_distances_as_state(cstate, distance, rotater2, trackpil,screen):

    cdista,cdistl,cdistr,cdistfr,cdistfl,cdistb,cdistbr,cdistbl,cdistfmr,cdistfml = 0,0,0,0,0,0,0,0,0,0

    #list of pixel positions (lines) in different directions (forward, forward-right, behind, behind left, etc)
    cy_points_ahead = []
    cx_points_ahead = []   
    cy_points_right = []
    cx_points_right = []
    cy_points_left = []
    cx_points_left = []
    cy_points_fr = []
    cx_points_fr = []
    cy_points_fl = []
    cx_points_fl = []
    cy_points_fmr = []
    cx_points_fmr = []
    cy_points_fml = []
    cx_points_fml = []
    cy_points_behind = []
    cx_points_behind = []
    cy_points_br = []
    cx_points_br = []
    cy_points_bl = []
    cx_points_bl = []

    for i in range(0,distance+1):
        cy_points_ahead.append(min(cstate[1] - i*math.cos(int(rotater2)*math.pi/180),719))
        cx_points_ahead.append(min(cstate[0] - i*math.sin(int(rotater2)*math.pi/180),1279))
        cy_points_right.append(min(cstate[1] - i*math.cos(int(rotater2-90)*math.pi/180),719))
        cx_points_right.append(min(cstate[0] - i*math.sin(int(rotater2-90)*math.pi/180),1279))
        cy_points_left.append(min(cstate[1] - i*math.cos(int(rotater2+90)*math.pi/180),719))
        cx_points_left.append(min(cstate[0] - i*math.sin(int(rotater2+90)*math.pi/180),1279))
        cy_points_fr.append(min(cstate[1] - i*math.cos(int(rotater2-45)*math.pi/180),719))
        cx_points_fr.append(min(cstate[0] - i*math.sin(int(rotater2-45)*math.pi/180),1279))
        cy_points_fl.append(min(cstate[1] - i*math.cos(int(rotater2+45)*math.pi/180),719))
        cx_points_fl.append(min(cstate[0] - i*math.sin(int(rotater2+45)*math.pi/180),1279))
        cy_points_behind.append(min(cstate[1] - i*math.cos(int(rotater2+180)*math.pi/180),719))
        cx_points_behind.append(min(cstate[0] - i*math.sin(int(rotater2+180)*math.pi/180),1279))
        cy_points_br.append(min(cstate[1] - i*math.cos(int(rotater2-135)*math.pi/180),719))
        cx_points_br.append(min(cstate[0] - i*math.sin(int(rotater2-135)*math.pi/180),1279))
        cy_points_bl.append(min(cstate[1] - i*math.cos(int(rotater2+135)*math.pi/180),719))
        cx_points_bl.append(min(cstate[0] - i*math.sin(int(rotater2+135)*math.pi/180),1279))
        cy_points_fmr.append(min(cstate[1] - i*math.cos(int(rotater2-27)*math.pi/180),719))
        cx_points_fmr.append(min(cstate[0] - i*math.sin(int(rotater2-27)*math.pi/180),1279))
        cy_points_fml.append(min(cstate[1] - i*math.cos(int(rotater2+27)*math.pi/180),719))
        cx_points_fml.append(min(cstate[0] - i*math.sin(int(rotater2+27)*math.pi/180),1279))

    track_points = []
    #calculate distance to end of track in each direction, depending on pixel color (black is track)
    for i in range(0,distance+1):
        if trackpil[cx_points_ahead[i],cy_points_ahead[i]] != (0, 0, 0, 255):
            cdista = math.sqrt((cx_points_ahead[i] - cstate[0])**2 + (cy_points_ahead[i] - cstate[1])**2)
            track_points.append((cx_points_ahead[i],cy_points_ahead[i],10,10))
            break            
    for i in range(0,distance+1):
        if trackpil[cx_points_left[i],cy_points_left[i]] != (0, 0, 0, 255):
            cdistl = math.sqrt((cx_points_left[i] - cstate[0])**2 + (cy_points_left[i] - cstate[1])**2)
            track_points.append((cx_points_left[i],cy_points_left[i],10,10))
            break  
    for i in range(0,distance+1):
        if trackpil[cx_points_right[i],cy_points_right[i]] != (0, 0, 0, 255):
            cdistr = math.sqrt((cx_points_right[i]- cstate[0])**2 + (cy_points_right[i] - cstate[1])**2)
            track_points.append((cx_points_right[i],cy_points_right[i],10,10))
            break
    for i in range(0,distance+1):
        if trackpil[cx_points_fr[i],cy_points_fr[i]] != (0, 0, 0, 255):
            cdistfr = math.sqrt((cx_points_fr[i]- cstate[0])**2 + (cy_points_fr[i] - cstate[1])**2)
            track_points.append((cx_points_fr[i],cy_points_fr[i],10,10))
            break
    for i in range(0,distance+1):
        if trackpil[cx_points_fl[i],cy_points_fl[i]] != (0, 0, 0, 255):
            cdistfl = math.sqrt((cx_points_fl[i]- cstate[0])**2 + (cy_points_fl[i] - cstate[1])**2)
            track_points.append((cx_points_fl[i],cy_points_fl[i],10,10))
            break
    for i in range(0,distance+1):
        if trackpil[cx_points_behind[i],cy_points_behind[i]] != (0, 0, 0, 255):
            cdistb = math.sqrt((cx_points_behind[i]- cstate[0])**2 + (cy_points_behind[i] - cstate[1])**2)
            track_points.append((cx_points_behind[i],cy_points_behind[i],10,10))
            break
    for i in range(0,distance+1):
        if trackpil[cx_points_br[i],cy_points_br[i]] != (0, 0, 0, 255):
            cdistbr = math.sqrt((cx_points_br[i]- cstate[0])**2 + (cy_points_br[i] - cstate[1])**2)
            track_points.append((cx_points_br[i],cy_points_br[i],10,10))
            break
    for i in range(0,distance+1):
        if trackpil[cx_points_bl[i],cy_points_bl[i]] != (0, 0, 0, 255):
            cdistbl = math.sqrt((cx_points_bl[i]- cstate[0])**2 + (cy_points_bl[i] - cstate[1])**2)
            track_points.append((cx_points_bl[i],cy_points_bl[i],10,10))
            break
    for i in range(0,distance+1):
        if trackpil[cx_points_fmr[i],cy_points_fmr[i]] != (0, 0, 0, 255):
            cdistfmr = math.sqrt((cx_points_fmr[i]- cstate[0])**2 + (cy_points_fmr[i] - cstate[1])**2)
            track_points.append((cx_points_fmr[i],cy_points_fmr[i],10,10))
            break
    for i in range(0,distance+1):
        if trackpil[cx_points_fml[i],cy_points_fml[i]] != (0, 0, 0, 255):
            cdistfml = math.sqrt((cx_points_fml[i]- cstate[0])**2 + (cy_points_fml[i] - cstate[1])**2)
            track_points.append((cx_points_fml[i],cy_points_fml[i],10,10))
            break
                
                
    present_state = [cdista,cdistl,cdistr,cdistfr,cdistfl,cdistb,cdistbr,cdistbl,cdistfmr,cdistfml] 
    return present_state, track_points

class rewardgates(object):        
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        
        self.AIstate = 0
        self.hitbox =(self.x, self.y, self.width,self.height)
    
    def draw(self,win):
        pygame.draw.rect(win, (0,255,0), (self.x,self.y,self.width,self.height)) #draws reward gate
        self.hitbox =(self.x, self.y, self.width,self.height)
        pygame.draw.rect(win,(0,0,255),self.hitbox,2)
        