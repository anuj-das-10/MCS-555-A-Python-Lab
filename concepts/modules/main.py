import geometry as g

pointA = (3, 4)
pointB = (7, 1)
print(f"""Distance: A(x:{pointA[0]}, y:{pointA[1]}) and B(x:{pointB[0]}, y:{pointB[1]}) is {g.euclidean_distance(pointA, pointB)} units.""")

side = 4
print(f'The area of square with side {side} is {g.area('square', side)} sq. unit.')

radius = 5
print(f'The area of circle with radius {radius} is {round(g.area('circle', radius), 2)} sq. unit.')