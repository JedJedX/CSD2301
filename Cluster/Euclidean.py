import math

def euclidean_distance(x1, y1, x2, y2):
  distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
  return distance

point1 = (55, 23) 
point2 = (40, 30)

result = euclidean_distance(point1[0], point1[1], point2[0], point2[1])
print("ค่า Euclidean:", result)