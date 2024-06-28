import math

def euclidean_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

def area(shape, *param):
    if(shape.lower() == 'circle'):
        radius = param[0]
        return math.pi * radius**2
       
    if(shape.lower() == 'rectangle'):
        length = param[0]
        width = param[1]
        return length * width
    
    if(shape.lower() == 'square'):
        side = param[0]
        return side * side
    
        
