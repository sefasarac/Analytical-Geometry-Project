import math 

circleCount = input()
circles = []
a=0
totalArea=0
while(a<int(circleCount)):
    circle = input().split()
    circles.append(circle)
    a+=1


def findBounding(firstCircle,SecondCircle):
    uzaklik=math.sqrt((int(SecondCircle[0])-int(firstCircle[0]))**2 + (int(SecondCircle[1]) - int(firstCircle[1]))**2)
    totalRectangle=int(firstCircle[2])+int(SecondCircle[2])
    if(uzaklik<totalRectangle):
       return True
    return False

def calculateArea(circle):
    x=(int(circle[0])+int(circle[2])) - (int(circle[0]) - int(circle[2]))
    if(x<0):
        x=-x
    y=(int(circle[1])+int(circle[2])) - (int(circle[1]) - int(circle[2]))
    if(y<0):
        y=-y
    return x*y

def merge(first,second):
    rightX=0
    leftX=0
    upY=0
    botY=0
    firstRightX = int(first[0])+int(first[2])
    firstLeftX= int(first[0])- int(first[2])
    firstUpY=int(first[1])+int(first[2])
    firstBottomY=int(first[1]) - int(first[2])
    secondRightX= int(second[0])+int(second[2])
    secondLeftX= int(second[0])- int(second[2])
    secondUpY = int(second[1])+int(second[2])
    secondBottomY =int(second[1]) - int(second[2])
    if(firstRightX>secondRightX):
        rightX=firstRightX
    else:
        rightX=secondRightX
    if(firstLeftX<secondLeftX):
        leftX=firstLeftX
    else:
        leftX=secondLeftX
    if(firstUpY>secondUpY):
        upY=firstUpY
    else:
        upY=secondUpY
    if(firstBottomY<secondBottomY):
        botY=firstBottomY
    else:
        botY=secondBottomY
    x=rightX-leftX
    if(x<0):
        x=-x
    y=upY-botY
    if(y<0):
        y=-y
    return x*y

isBounded=False
for first in range(0,len(circles)):
    if(len(circles[first])>3):
        continue
    for second in range(first+1,len(circles)):
        if(findBounding(circles[first],circles[second])==True):
            isBounded=True
            totalArea+= merge(circles[first],circles[second])
            circles[second].append("0")
            break
    if(isBounded==False):
        totalArea+=calculateArea(circles[first])
    isBounded=False

for circle in circles:
    print("( "+ circle[0] + " " + circle[1] + " ) rad: " + circle[2])
print("Total rect area: "+ str(totalArea))
