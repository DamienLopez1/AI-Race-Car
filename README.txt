####################### DQN Learning #########################
To run the training for the DQN learning run the command:
    python race_DQN.py

####################### Q-Table Learning #####################
To run the training for the Q-table learning run the command:
    python race_q_table.py

####################### Key Commands #########################
During the game you can use certain key commands:
    'r' : sets the exploration rate threshold of the episode to 0.1
    't' : sets the exploration rate back to the decaying exploration used in training
    'w','a','d' : command to force manual movement of the car (forward, left, right respectively)
    'esc' : exit the game
    
####################### Training Parameters ##################
To change the training parameters for the DQN training, edit the appropriate lines in 'race_DQN.py' (lines 19-25) or 'race_q_table.py' (lines 19-22)

To change the track on which the car trains, edit line 4 of 'init_race.py'*
    'oval' is the classic race track of a oval shape (it can be found in the res/ directory).
    'polar' refers to a more complicated race track with both left and right turns.

####################### Loading pretrained models #############
You can load a pretrained model by uncommenting the appropriate section in the beginning of 'race_DQN.py' and 'race_q_table.py'
    'good q_tbl.np' is an agent trained with Q-table on the oval track
    'good targetnet.pck' is an agent trained with DQN on the oval track
    'PBPT targetnet.pck' is an agent trained with DQN on the ploar bear track

####################### other files ##########################
init_race.py - contains the game mechanics and the necessary settings for the creation of the race environment (mostly pygame dependant)
utils.py - helper funtions needed to interact with the environment (car movement, rewards, calculating distances, etc)
dqn_utils.py - classes and methods needed specifically for the usage in DQN learning (network class, replay memory, etc)



