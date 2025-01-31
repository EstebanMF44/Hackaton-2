import numpy as np
from .GameObject import GameObject
'''La classe Board doit être hashable, c'est-à-dire que l'on doit pouvoir la mettre dans un dictionnaire. Pour cela, on doit implémenter les méthodes __hash__ et __eq__.'''
class Board (GameObject) :
    def __init__(self,Tiles) -> None:
        self._Tiles = Tiles
        self._board = np.zeros((3,3))
        self._objects : list[GameObject] = []

        
    def __hash__(self) -> int:
        return hash(tuple(self.board))
    
    def __eq__(self, other) -> bool:
        return self.board == other.board
    
    def add_object(self, obj: GameObject) -> None:
        """Add an object to the board."""
        # Add object if not already there
        if obj not in self._objects:
            self._objects.append(obj)
            obj.attach_obs(self)

    def remove_object(self, obj: GameObject) -> None:
        """Remove an object from the board."""
        # Remove object if present
        if obj in self._objects:
            self._objects.remove(obj)
            obj.detach_obs(self)

    def get_objects_at(self, position: tuple[int, int]) -> list[GameObject]:
        """Get all objects at a given position."""
        return [obj for obj in self._objects if position in obj.tiles]
    
    
    

    

    
      
    

    

    



    
        
    


    
    




   

     



