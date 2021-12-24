from Config import AIConfig
from collections import deque
from AI.AIGameController.AIGameController import AIGameController
import torch
from AI.model.model import Linear_QNet, QTrainer
import random
from AI.Helper.helper import plot
import pygame
import math
import numpy as np

class Agent:

    def __init__(self):
        self.n_game = 0
        self.epsilon = AIConfig.epsilon
        self.gamma = AIConfig.gamma
        self.batch_size = AIConfig.batch_size
        self.lr = AIConfig.LR
        self.memory =deque(maxlen=AIConfig.Max_Memory)
        self.model = Linear_QNet(AIConfig.input_size, AIConfig.hidden1_size, AIConfig.hidden2_size, AIConfig.output_size)
        self.trainer = QTrainer(self.model, AIConfig.LR, AIConfig.gamma, )

    def get_action(self,state):
        p = random.random() * math.exp(-self.n_game*(AIConfig.epsilon_decay))
        #print(math.exp(-self.n_game*(AIConfig.epsilon_decay)))
        final_move = [0,0,0]
        if(p > (1-AIConfig.random_move_prob)):
            move = random.randint(0,2)
            final_move[move] = 1

        else:
            state0 = torch.tensor(state, dtype=torch.float)
            prediction = self.model(state0)
            move = torch.argmax(prediction).item()
            final_move[move] = 1


        return final_move

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def train_short_memory(self, state, action, reward, next_state, done):
        loss = self.trainer.train_step(state, action, reward, next_state, done)
        return loss

    def train_long_memory(self):
        if(len(self.memory) > self.batch_size):
             mini_sample = random.sample(self.memory, self.batch_size)
        else:
            mini_sample = self.memory

        states, actions, rewards, next_states, dones = zip(*mini_sample)
        self.trainer.train_step(states, actions, rewards, next_states, dones)



def train():
    plot_score = []
    mean_plot_score = []
    loss_list = []
    loss_mean = []
    total_score = 0
    record = 0
    agent = Agent()
    game_controller = AIGameController()

    while True:
        pygame.display.update()

        old_state = game_controller.get_state()

        final_move = agent.get_action(old_state)

        reward, isEnd, score = game_controller.move_one_step(final_move)

        new_state = game_controller.get_state()

        loss = agent.train_short_memory(old_state, final_move, new_state, reward, isEnd)
        loss_list.append(loss.item())
        agent.remember(old_state, final_move, new_state, reward, isEnd)

        if isEnd:
            loss_mean.append(np.mean(loss_list))
            #print(len(game_controller.snake.coordinates))
            game_controller.reset()

            agent.n_game += 1
            agent.train_long_memory()


            if(score > record):
                record = score
                agent.model.save()
            
            print("Game: ", agent.n_game, "score: " , score , "Record: " ,record )
            plot_score.append(score)
            total_score += score
            mean_score = total_score / agent.n_game
            mean_plot_score.append(mean_score)
            plot(mean_plot_score, "score.png")
            plot(loss_mean, "ssloss.png")


        game_controller.wait()

if(__name__ == '__main__'):
    train()