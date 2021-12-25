import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import os
from Config import AIConfig

class Linear_QNet(nn.Module):
    def __init__(self, input_size, hidden1_size, hidden2_size  , output_size):
        super().__init__()
        self.Linear1 = nn.Linear(input_size, hidden1_size)
        self.Linear2 = nn.Linear(hidden1_size, output_size)
        #self.Linear3 = nn.Linear(hidden1_size, output_size)

    def forward(self, x):
        x = F.relu(self.Linear1(x))
        #x = F.relu(self.Linear2(x))
        x = self.Linear2(x)
        return x

    def save(self,root_path,file_name="model.pth" ):
        file_path = root_path + "models/"
        if not os.path.exists(file_path):
            os.mkdir(file_path)

        file_name = os.path.join(file_path, file_name)
        torch.save(self.state_dict(), file_name)

class QTrainer:
    def __init__(self, model, lr, gamma):
        self.lr = lr
        self.gamma = gamma
        self.model = model
        self.optimizer = optim.Adam(model.parameters(), lr=self.lr)
        self.criterion = nn.MSELoss()
        self.scheduler = torch.optim.lr_scheduler.ExponentialLR(self.optimizer, gamma=AIConfig.lr_gamma)


    def train_step(self,state, action, new_state, reward, isEnd):
        state = torch.tensor(state, dtype=torch.float)
        action = torch.tensor(action, dtype=torch.float)
        new_state = torch.tensor(new_state, dtype=torch.float)
        reward = torch.tensor(reward, dtype=torch.float)

        if( len(state.shape) == 1):
            state = torch.unsqueeze(state, 0)
            action = torch.unsqueeze(action, 0)
            new_state = torch.unsqueeze(new_state, 0)
            reward = torch.unsqueeze(reward, 0)
            isEnd = (isEnd,)

        pred = self.model(state)
        target = pred.clone()
        for idx in range(len(isEnd)):
            Q_new = reward[idx]
            if not isEnd[idx]:
                Q_new = reward[idx] + self.gamma * torch.max(self.model(new_state[idx]))

            target[idx][torch.argmax(action).item()] = Q_new

        self.optimizer.zero_grad()
        loss = self.criterion(target, pred)
        loss.backward()

        self.optimizer.step()
        #self.scheduler.step()

        lr = self.optimizer.param_groups[0]['lr']

        return loss , lr



