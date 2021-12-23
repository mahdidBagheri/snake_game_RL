from Config import GameConfig, AssetsConfig
class Utils:
    def __init__(self):
        pass

    def border_coordinates(self):
        coordinate_list = []
        scale = GameConfig.scale
        for i in range(0, GameConfig.Game_Width):
            coordinate_list.append((0, i * scale))

        for i in range(GameConfig.Game_Hight):
            coordinate_list.append((i * scale, 0))

        for i in range(GameConfig.Game_Hight):
            coordinate_list.append((i * scale, (GameConfig.Game_Hight - 1) * scale))

        for i in range(GameConfig.Game_Width):
            coordinate_list.append(((GameConfig.Game_Width - 1) * scale, i * scale))

        return coordinate_list