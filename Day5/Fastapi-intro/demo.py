class rectangle:
    def __init__(self,w:int, h:int)->None:
        self.width = w
        self.height = h

def area(r:rectangle)->int:
    return r.width*r.height

r1 = rectangle(10,20)
print(area(r1))