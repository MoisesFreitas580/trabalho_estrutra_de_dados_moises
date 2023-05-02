class Pilha:
    def __init__(self, size: int) -> None:
        self.pilha : list = []
        self.size : int = size 
    
    def addTop(self, data: any) -> None:

        if len(self.pilha) == self.size:
            print( False )
            return

        self.pilha.append(data)
        return
    
    def removeTop(self) -> None:

        if len(self.pilha) == 0:
            print( False )
            return

        self.pilha.pop()

        return

    def __str__(self) -> str:
        return f'{self.pilha}'