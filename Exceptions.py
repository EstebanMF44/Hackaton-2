class (Exception) :

    def __init__(self, message : str) -> None:
        self.message = message
        super().__init__(self.message)

    def ValueError(self) -> str:
        return self.message
    
    