class No:
    def __init__(self, data: any):
        self.data: any = data 
        self.proximo: any  = None 
        self.anterior: any = None 
    
class ListaEncadeadaDupla:

    def __init__(self):
        self.cabeca: any = None
        self.cauda: any = None
    

    def append(self, data: any):
        novo_no = No(data) 

        novo_no.proximo = None

        if self.cabeca == None:
            novo_no.anterior = None
            self.cabeca = novo_no
            return

        ultimo_no = self.cabeca
        
        while ultimo_no.proximo:
            ultimo_no = ultimo_no.proximo
        
        ultimo_no.proximo = novo_no

        novo_no.anterior = ultimo_no
        return
    

    def printList(self): 
        conteudo = self.cabeca 
        _str = ''
        if conteudo is None:
          print(False)
        while conteudo: 
            _str += f'<-- {conteudo.data} -->'
            conteudo = conteudo.proximo
        print(_str) 

    def inserirNoInicio(self, data: any):
        if self.cabeca == None:
            novo_no = No(data)
            self.cabeca = novo_no
            
            return
        novo_no = No(data)
        novo_no.proximo = self.cabeca
        self.cabeca.anterior = novo_no
        self.cabeca = novo_no

    def inserirNoFinal(self, data: any):
        if self.cabeca == None:
            novo_no = No(data)
            self.cabeca = novo_no
            return
        no_atual = self.cabeca
        while no_atual.proximo != None:
            no_atual = no_atual.proximo
        novo_no = No(data)
        no_atual.proximo = novo_no
        novo_no.anterior = no_atual
    
    def removerNoInicio(self: any):
        if self.cabeca == None:
            print(False)
            return 
        if self.cabeca.proximo == None:
            self.cabeca = None
            return
        self.cabeca = self.cabeca.proximo
        self.start_prev = None

    def removerNoFinal(self):
        if self.cabeca == None:
            print(False)
            return 
        if self.cabeca.proximo == None:
            self.cabeca = None
            return
        no_atual = self.cabeca
        while no_atual.proximo != None:
            no_atual = no_atual.proximo
        no_atual.anterior.proximo = None

    def removerItemDaLista(self, value: any):
        if self.cabeca == None:
            print(False)
            return 
        if self.cabeca.proximo == None:
            if self.cabeca.item == value:
                self.cabeca = None
            else:
                print(False)
            return 

        if self.cabeca.data == value:
            self.cabeca = self.cabeca.proximo
            self.cabeca.anterior = None
            return

        no_atual = self.cabeca
        while no_atual.proximo != None:
            if no_atual.data == value:
                break
            no_atual = no_atual.proximo
        if no_atual.proximo != None:
            no_atual.anterior.proximo = no_atual.proximo
            no_atual.proximo.anterior = no_atual.anterior
        else:
            if no_atual.data == value:
                no_atual.anterior.proximo = None
            else:
                print(False)

    def buscarItem(self, value: any):
        no_atual = self.cabeca
        while no_atual is not None:
            if no_atual.data == value:
                print(no_atual.data)
                return 
            no_atual = no_atual.proximo
            
