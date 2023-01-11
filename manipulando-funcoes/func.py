from functools import singledispatch,singledispatchmethod,partial

@singledispatch
def func(args):
    pass

@func.register
def _(args: int):
    print("Inteiro chamado")
    
@func.register
def _(args: str):
    print("String chamada")
    
    
class NeuralNetwork:
    
    @singledispatchmethod
    def neg(self, args):
        raise NotImplementedError('Not implemented')
    
    @neg.register
    def _(self, args: int):
        return -args
    
    @neg.register
    def _(self, args: bool):
        return not args
    
def mult(x,y):
    return x * y

dobro = partial(mult,y=2)