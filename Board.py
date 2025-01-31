import numpy as np
from .GameObject import GameObject
from .Background import Background
'''La clase Board doit être hashable, c'est-à-dire que l'on doit pouvoir la mettre dans un dictionnaire. Pour cela, on doit implémenter les méthodes __hash__ et __eq__.'''
class Board (GameObject,Background) :
    def __init__(self,Tiles) -> None:
        self.Tiles = Tiles
        self.board = np.zeros((3,3))
        
    def __hash__(self):
        return hash(tuple(self.board))
    
    def __eq__(self, other):
        return self.board == other.board
    

    
        
    


    
    




   

     



