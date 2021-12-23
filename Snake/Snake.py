from Config import GameConfig , AssetsConfig
import pygame

class Snake:
    def __init__(self):
        self.scale = GameConfig.scale
        self.icon = pygame.image.load(AssetsConfig.SnakeBlockAddress)
        self.head_icon = pygame.image.load(AssetsConfig.SnakeHeadBlockAddress)
        self.direction = "left"
        self.move_direction = "left"
        self.coordinates = GameConfig.Snake_Initial_Coordinate


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
