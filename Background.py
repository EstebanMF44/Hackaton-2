fron .GameObject import GameObject
class Background (GameObject) :
    def __init__(self, name, position, size, background_type) -> None:
        super(Background, self).__init__(name, position, size)
        self.background_type = background_type
    
    def attach(self, game_object) -> None:
        pass