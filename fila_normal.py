class FilaNormal:
    cogido: int = 0
    fila = []
    clientesatendidos = []
    senhaatual = ""

    def gerasenhaatual(self)->None:
        self.senhaatual = f'NM{self.cogido}'

    def resetafila(self):
        if self.cogido >= 100:
            sefl.codigo=0
        else:
            self.cogido+=1
    def atualizafila(self):
        self.resetafila()
        self.gerasenhaatual()
        self.fila.append(self.senhaatual)
    def chamacliente(self, caixa:int)->str:
        cliente_atual:str = self.fila.pop(0)
        self.clientesatendidos.append(cliente_atual)
        return (f'Cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}')