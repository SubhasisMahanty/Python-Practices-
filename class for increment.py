'''
class CountFromBy:
    def __init__(self,v:int,i:int) -> None:
        self.val = v
        self.incr = i

    def increase(self) -> None:
        self.val += self.incr
'''
class CountFromBy():
    #def __init__(x,v:int,i:int) -> None:
     #   x.val = v
      #  x.incr = i
    def __init__(x,a:int,b:int) -> None:
        x.val = a
        x.incr = b
    def increase(x) -> None:
        x.val += x.incr
