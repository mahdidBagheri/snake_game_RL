from Config import AIConfig
from collections import deque
from AI.AIGameController.AIGameController import AIGameController
import torch
from AI.model.model import Linear_QNet, QTrainer
import random
from AI.Helper.helper import plot
import pygame

class Agent:

    def __init__(self):
        self.n_game = 0
        self.epsilon = AIConfig.epsilon
        self.gamma = AIConfig.gamma
        self.batch_size = AIConfig.batch_size
        self.lr = AIConfig.LR
        self.memory =deque(maxlen=AIConfig.Max_Memory)
        self.model = Linear_QNet(AIConfig.input_size, AIConfig.hidden_size, AIConfig.output_size)
        self.trainer = QTrainer(self.model, AIConfig.LR, AIConfig.gamma, )

    def get_action(self,state):
        self.epsilon = AIConfig.epsilon - self.n_game
        final_move = [0,0,0]
        if(random.randint(0, AIConfig.epsilon*3) < self.epsilon):
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
        self.trainer.train_step(state, action, reward, next_state, done)

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

        agent.train_short_memory(old_state, final_move, new_state, reward, isEnd)

        agent.remember(old_state, final_move, new_state, reward, isEnd)

        if isEnd:
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
            plot(plot_score, mean_plot_score)


        game_controller.wait()

if(__name__ == '__main__'):
    train()