from GameObject import GameObject
class Tile (GameObject) :
    def __init__(self, x : int, y : int) -> None:
        self._x = x # Line index
        self._y = y # Column index
        
    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, value: int) -> None:
        if value < 0 or value > 2:
            raise ValueError("Invalid value for x, must be between 0 and 2")
        self._x = value

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, value: int) -> None:
        if value < 0 or value > 2:
            raise ValueError("Invalid value for y, must be between 0 and 2")
        self._y = value
    
    def Button(self) -> None:
        pass
    