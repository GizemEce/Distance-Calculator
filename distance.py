#Gizem Ece Yılmaz
from math import *

#Contract:
#tuple tuple -> number
#Purpose: find distance between two points
#Examples:
#distance((2,3),(5,4))-> 3.16227766017
def euclideandistance(p1,p2):
	#Take the square root of the sum of the squares of the differences of the coordinates.
	dist=sqrt(pow((p2[0]-p1[0]),2)+pow((p2[1]-p1[1]),2))
	return dist
#test
print euclideandistance((2,3),(5,4))


#Contract:
#tuple tuple -> number
#Purpose: find distance between two points
#Examples:
#distance((2,3),(5,4))-> 4
def manhattendistance(p1,p2):
	#Take the sum of the absolute values of the differences of the coordinates.
	dist=abs(p2[0]-p1[0])+abs(p2[1]-p1[1])
	return dist
#test
print manhattendistance((2,3),(5,4))


#Contract:
#It returns distance calculation of two points
#Purpose:to decide which algorithm will be used 
def choosealgorithm():
	userinput=raw_input("If you want to use Manhatten Distance type M,otherwise type E for Euclidean Distance: ")
	x1=raw_input("Please write first point's x:")
	y1=raw_input("Please write first point's y:")
	x2=raw_input("Please write second point's x:")
	y2=raw_input("Please write second point's y:")
	point1=(float(x1),float(y1))
	point2=(float(x2),float(y2))
	if(userinput=="M"):
		print manhattendistance(point1,point2)
	elif(userinput=="E"):
		print euclideandistance(point1,point2)

choosealgorithm()