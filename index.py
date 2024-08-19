import math


points=((2,2),(4,2),(4,4))
side1 = 0
side2 = 0

# X değerleri eşit olan iki nokta bulalım ve y değerlerinin farkını alalım
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        if points[i][0] == points[j][0]:
            side1 = abs(points[i][1] - points[j][1])

#aynısı Y değerlerei için bunun la x değerlerinin farkını bulacağız
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        if points[i][1] == points[j][1]:
            side2 = abs(points[i][1] - points[j][1])

sonuc=math.sqrt(side1**2 + side2**2)
print(sonuc)





"""
for i in range(len(points)):
    for j in range(i+1,len(points)):
        for c in range(2):
            if points[i][c]==points[j][]"""
