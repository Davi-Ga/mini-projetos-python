class Pessoa:
    def __init__(self):
        self.pessoas=['Ana', 'Maria', 'João']

    def __eq__(self, p2):
        if len(self.pessoas) == len(p2):
            x=[self.pessoas[i] == p2[i] for i in range(len(self.pessoas))]
            return all(x)
        else:
            return False
        
x = Pessoa()
y=Pessoa()
print(x==y)