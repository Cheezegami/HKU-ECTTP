from GenericObject import GenericObject

class ObjectRunner():
    objectList = []
    def createObjects(self): # Object Creation.
        # Array in which the objects are contained.
        self.objectList.append(GenericObject(50,50,int_border+random(width-int_border),+random(height-int_border),5,"rectangle",0,60,127,255,int_border)) # First Object, bouncing rectangle.
        self.objectList.append(GenericObject(50,50,int_border+random(width-int_border),int_border+random(height-int_border),4,"ellipse",0,255,127,60,int_border)) # Second Object, bouncing ellipse.
        self.objectList.append(GenericObject(100,100,int_border+random(width-int_border),int_border+random(height-int_border),10,"rectangle",1,127,60,255,int_border)) # Third, Movable Object
        self.objectList.append(GenericObject(100,100,int_border+random(width-int_border),int_border+random(height-int_border),10,"ellipse",2,127,60,255,int_border)) # Fourth, Time Based Object.