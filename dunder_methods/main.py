class Pessoa:
    #Método inicializador
    def __init__(self):
        self.pessoas=['Ana', 'Maria', 'João']
    
    #Método que retorna um objeto em forma de string
    def __str__(self):
        return f'Pessoa(pessoas={self.pessoas})'
    
    #Método que retorna um objeto de uma lista de objetos
    def __getitem__(self, index):
        return self.pessoas[index]
    
    def __len__(self):
        x=0
        while True:
            try:
                y=self.pessoas[x]
                x+=1
            except:
                break    
        return x
    
    def __add__(self,p2):
        return self.pessoas+p2
    
    def __mul__(self,n):
        return self.pessoas*n
    
    def __delitem__(self, index):
        del self.pessoas[index]
        
    def __reversed__(self):
        return [self.pessoas[i] for i in range(len(self.pessoas)-1,-1,-1)]
        #return self.pessoas[::-1]
        
    def __eq__(self, p2):
        if len(self.pessoas) == len(p2):
            x=[self.pessoas[i] == p2[i] for i in range(len(self.pessoas))]
            return all(x)
        else:
            return False
    
    def __iter__(self):
        i=0
        while i< len(self.pessoas):
            yield self.pessoas[i]
            i+=1
        
x = Pessoa()
print(reversed(x))