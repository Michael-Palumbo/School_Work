class Box:
    def __init__(self,width,height):
        self.widthB=width
        self.heightB=height
        self.isShape=True
    def getArea(self):
        return self.widthB*self.heightB
    def __str__(self):
        return str(self.widthB) +" "+ str(self.heightB)
box=Box(20,20)
print(box.getArea())
print (box)
