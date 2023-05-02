class Fila:
    def __init__(self, size: int) -> None:
        self.fila: list = []
        self.size : int = size 

    def addStart(self, data: any) -> None:
        
        if len(self.fila) == self.size:
            print(False)
            return
        
        self.fila.insert(0, data)

    def removeStart(self) -> None:

        if len(self.fila) == 0:
            print(False)
            return
        
        self.fila.pop(0)


    def __str__(self) -> str:
        return f'{self.fila}'