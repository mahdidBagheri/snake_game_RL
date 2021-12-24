from Config import GameConfig , AssetsConfig
import pygame
from Utils.Utils import Utils

class Snake:
    def __init__(self):
        self.scale = GameConfig.scale
        self.game_width = GameConfig.Game_Width
        self.game_hight = GameConfig.Game_Hight
        self.icon = pygame.image.load(AssetsConfig.SnakeBlockAddress)
        self.head_icon = pygame.image.load(AssetsConfig.SnakeHeadBlockAddress)
        self.direction = "right"
        self.move_direction = "right"
        self.coordinates = [(int(GameConfig.Game_Width/2)*self.scale,int(GameConfig.Game_Hight/2)*self.scale), (int(GameConfig.Game_Width/2-1)*self.scale,int(GameConfig.Game_Hight/2)*self.scale)]
        self.walls = Utils.border_coordinates(self)


    def move(self):
        if(self.direction == "right"):
            if(self.move_direction == "right"):
                self.move_right_right()
            elif(self.move_direction == "down"):
                self.move_right_down()
                self.direction = self.move_direction
            elif(self.move_direction == "up"):
                self.move_right_up()
                self.direction = self.move_direction

        elif(self.direction == "up"):
            if (self.move_direction == "up"):
                self.move_up_up()
                self.direction = self.move_direction
            elif(self.move_direction == "right"):
                self.move_up_right()
                self.direction = self.move_direction
            elif(self.move_direction == "left"):
                self.move_up_left()
                self.direction = self.move_direction

        elif (self.direction == "left"):
            if (self.move_direction == "left"):
                self.move_left_left()
                self.direction = self.move_direction
            elif (self.move_direction == "up"):
                self.move_left_up()
                self.direction = self.move_direction
            elif (self.move_direction == "down"):
                self.move_left_down()
                self.direction = self.move_direction

        elif (self.direction == "down"):
            if (self.move_direction == "down"):
                self.move_down_down()
            elif (self.move_direction == "left"):
                self.move_down_left()
                self.direction = self.move_direction
            elif (self.move_direction == "right"):
                self.move_down_right()
                self.direction = self.move_direction


    def move_left_left(self):
        for i in range(len(self.coordinates)-1,0,-1):
            (self.coordinates)[i] = self.coordinates[i-1]
        (self.coordinates)[0] = ((self.coordinates)[0][0]-1*self.scale,(self.coordinates)[0][1])


    def move_up_up(self):
        for i in range(len(self.coordinates)-1,0,-1):
            (self.coordinates)[i] = self.coordinates[i-1]
        (self.coordinates)[0] = ((self.coordinates)[0][0],(self.coordinates)[0][1]-1*self.scale)


    def move_right_right(self):
        for i in range(len(self.coordinates)-1,0,-1):
            (self.coordinates)[i] = self.coordinates[i-1]
        (self.coordinates)[0] = ((self.coordinates)[0][0]+1*self.scale,(self.coordinates)[0][1])


    def move_down_down(self):
        for i in range(len(self.coordinates)-1,0,-1):
            (self.coordinates)[i] = self.coordinates[i-1]
        (self.coordinates)[0] = ((self.coordinates)[0][0],(self.coordinates)[0][1]+1*self.scale)


    def move_left_up(self):
        for i in range(len(self.coordinates)-1,0,-1):
            (self.coordinates)[i] = self.coordinates[i-1]
        (self.coordinates)[0] = ((self.coordinates)[0][0],(self.coordinates)[0][1]-1*self.scale)


    def move_left_down(self):
        for i in range(len(self.coordinates)-1,0,-1):
            (self.coordinates)[i] = self.coordinates[i-1]
        (self.coordinates)[0] = ((self.coordinates)[0][0],(self.coordinates)[0][1]+1*self.scale)


    def move_right_down(self):
        for i in range(len(self.coordinates)-1,0,-1):
            (self.coordinates)[i] = self.coordinates[i-1]
        (self.coordinates)[0] = ((self.coordinates)[0][0],(self.coordinates)[0][1]+1*self.scale)


    def move_right_up(self):
        for i in range(len(self.coordinates)-1,0,-1):
            (self.coordinates)[i] = self.coordinates[i-1]
        (self.coordinates)[0] = ((self.coordinates)[0][0],(self.coordinates)[0][1]-1*self.scale)


    def move_up_right(self):
        for i in range(len(self.coordinates)-1,0,-1):
            (self.coordinates)[i] = self.coordinates[i-1]
        (self.coordinates)[0] = ((self.coordinates)[0][0]+1*self.scale,(self.coordinates)[0][1])


    def move_up_left(self):
        for i in range(len(self.coordinates)-1,0,-1):
            (self.coordinates)[i] = self.coordinates[i-1]
        (self.coordinates)[0] = ((self.coordinates)[0][0]-1*self.scale,(self.coordinates)[0][1])


    def move_down_right(self):
        for i in range(len(self.coordinates)-1,0,-1):
            (self.coordinates)[i] = self.coordinates[i - 1]
        (self.coordinates)[0] = ((self.coordinates)[0][0]+1*self.scale,(self.coordinates)[0][1])


    def move_down_left(self):
        for i in range(len( self.coordinates)-1,0,-1):
            (self.coordinates)[i] = self.coordinates[i - 1]
        (self.coordinates)[0] = ((self.coordinates)[0][0]-1*self.scale,(self.coordinates)[0][1])

    def setMoveDirection(self,dir):
        if(self.areOppositeDirections(dir, self.direction)):
            return
        self.move_direction = dir

    def areOppositeDirections(self, s1, s2):
        if((s1 == "left" and s2 == "right") or (s1 == "right" and s2 == "left") ):
            return True
        if((s1 == "up" and s2 == "down") or (s1 == "down" and s2 == "up") ):
            return True
        return False

    def grow(self):
        t = tuple(map(lambda i, j: i - j, self.coordinates[-2], self.coordinates[-1]))
        newBlock = tuple(map(lambda i, j: j - i, t, self.coordinates[-1]))
        self.coordinates.append(newBlock)

    def detect_danger(self):
        danger = [0,0,0]
        (x, y) = self.coordinates[0]

        if(self.direction == "left"):

            for i in range(self.game_width):
                if((x-i*self.scale,y) in self.coordinates[1:] + self.walls):
                    danger[0] = i

            for i in range(self.game_hight):
                if((x,y-i*self.scale) in self.coordinates[1:] + self.walls):
                    danger[1] = 1

            if((x,y+self.scale) in self.coordinates[1:] + self.walls):
                danger[2] = 1

        elif(self.direction == "right"):
            if((x+self.scale,y) in self.coordinates[1:] + self.walls):
                danger[0] = 1
            if((x,y+self.scale) in self.coordinates[1:] + self.walls):
                danger[1] = 1
            if((x,y-self.scale) in self.coordinates[1:] + self.walls):
                danger[2] = 1

        elif(self.direction == "up"):
            if((x,y-self.scale) in self.coordinates[1:] + self.walls):
                danger[0] = 1
            if((x+self.scale,y) in self.coordinates[1:] + self.walls):
                danger[1] = 1
            if((x-self.scale,y) in self.coordinates[1:] + self.walls):
                danger[2] = 1

        elif(self.direction == "down"):
            if((x,y+self.scale) in self.coordinates[1:] + self.walls):
                danger[0] = 1
            if((x-self.scale,y) in self.coordinates[1:] + self.walls):
                danger[1] = 1
            if((x+self.scale,y) in self.coordinates[1:] + self.walls):
                danger[2] = 1

        return danger

    def get_direction(self):
        dir = [0,0,0,0]
        if(self.direction == "left"):
            dir[0] = 1
        elif(self.direction == "right"):
            dir[1] = 1
        elif(self.direction == "up"):
            dir[2] = 1
        elif(self.direction == "down"):
            dir[3] = 1
        return dir