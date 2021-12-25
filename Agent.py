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
import os

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
        p = random.random()
        rnd_move_prob = math.exp(-self.n_game*(AIConfig.epsilon_decay)) * AIConfig.random_move_prob + 0.005
        #print(math.exp(-self.n_game*(AIConfig.epsilon_decay)))
        #p = random.random()
        final_move = [0,0,0]
        if(p < rnd_move_prob):
            move = random.randint(0,2)
            final_move[move] = 1

        else:
            state0 = torch.tensor(state, dtype=torch.float)
            prediction = self.model(state0)
            move = torch.argmax(prediction).item()
            final_move[move] = 1


        return final_move, rnd_move_prob

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def train_short_memory(self, state, action, reward, next_state, done):
        loss, lr = self.trainer.train_step(state, action, reward, next_state, done)
        return loss, lr

    def train_long_memory(self):
        self.trainer.scheduler.step()
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
    moving_average = []
    total_score = 0
    record = 0
    agent = Agent()
    game_controller = AIGameController()
    saver = Saver()

    while True:
        pygame.display.update()

        old_state = game_controller.get_state()

        final_move, p = agent.get_action(old_state)

        reward, isEnd, score = game_controller.move_one_step(final_move)

        new_state = game_controller.get_state()

        loss , lr = agent.train_short_memory(old_state, final_move, new_state, reward, isEnd)
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


            log_data = f"Game: {agent.n_game},score: {score} Record: {record} p: {p}, lr: {lr}"
            print(log_data)

            plot_score.append(score)
            total_score += score
            mean_score = total_score / agent.n_game
            mean_plot_score.append(mean_score)
            moving_average.append(np.mean(plot_score[:200]))

            saver.save(agent, [[mean_plot_score, "mean_plot_score"], [plot_score, "score"], [moving_average, "moving_average(200)"]], [[loss_mean, "mean_loss"]])
            #saver.save(agent, [[mean_plot_score, "mean_plot_score"], [plot_score, "score"]], [[loss_mean, "mean_loss"]])
            saver.log(log_data)

        game_controller.wait()

class Saver():
    def __init__(self):
        self.directory, self.log_dir = self.make_dir()
        self.init_log()

    def init_log(self):
        data = ""
        data += f"gamma , {AIConfig.gamma}, "
        data += f"epsilon , {AIConfig.epsilon}, "
        data += f"random_move_prob , {AIConfig.random_move_prob}, "
        data += f"epsilon_decay , {AIConfig.epsilon_decay}, "
        data += f"lr_schedular , {AIConfig.lr_schedular}, "
        data += f"LR , {AIConfig.LR}, "
        data += f"lr_constant , {AIConfig.lr_constant}, "
        data += f"LR_gamma , {AIConfig.lr_gamma}, "
        data += f"Max_Memory , {AIConfig.Max_Memory}, "
        data += f"batch_size , {AIConfig.batch_size}, "
        data += f"punish , {AIConfig.punish}, "
        data += f"long_stay_punish , {AIConfig.long_stay_punish}, "
        data += f"food_distance_reward , {AIConfig.food_distance_reward}, "
        data += f"border_reward , {AIConfig.border_reward}, "
        data += f"input_size , {AIConfig.input_size}, "
        data += f"hidden1_size , {AIConfig.hidden1_size}, "
        data += f"output_size , {AIConfig.output_size}, "
        data += f"negative_step , {AIConfig.negative_step}, "
        data += f"negative_step_growth , {AIConfig.negative_step_growth}, "
        data += f"max_step_per_length , {AIConfig.max_step_per_length}, "
        data += f"max_step_per_length , {AIConfig.max_step_per_length}, "
        data += f"save_freq , {AIConfig.save_freq}\n"

        log_file = open(self.log_dir, "a")
        log_file.write(data + "\n")
        log_file.close()



    def make_dir(self):
        root = "./runs/"
        save_number = 0
        while (os.path.isdir(root + f"run{save_number}")):
            save_number += 1
        dir = root + f"run{save_number}/"
        os.mkdir(dir)
        log_dir = dir + "log.txt"
        log_file = open(log_dir , "a")
        log_file.close()

        return dir , log_dir

    def save(self,agent, score_plots, loss_plots, save_freq = AIConfig.save_freq ):

        if (agent.n_game % save_freq == 1):
            agent.model.save(root_path = self.directory, file_name=f"model{agent.n_game}.pth")

        plot(score_plots,plot_path =self.directory , plot_name= "score.png",title = "score", y_axis="score", x_axis="episode")
        plot(loss_plots, plot_path =self.directory , plot_name="loss.png",title="loss", y_axis="loss", x_axis="episode", )

    def log(self, data):
        log_file = open(self.log_dir, "a")
        log_file.write(data + "\n")
        log_file.close()


if(__name__ == '__main__'):
    train()