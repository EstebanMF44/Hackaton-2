class GameObject ():
    def __init__(self, name, position, size) -> None:
        self.name = name
        self.position = position
        self.size = size

    
    def __contains__(self, other: object) -> bool:
        """Check if an game object intersects with another."""
        if not isinstance(other, GameObject):
            return False
        return any(t in self.tiles for t in other.tiles)

    def is_background(self) -> bool:
        """Tell if this object is a background object."""
        return False
    
    
    

