# function to calculate the area of circle
import math


def calculateAreaOfCircle(myradius):
    myarea = math.pi * myradius ** 2
    return myarea

 # function to convert from fahrenheit to celsius
 # f is degree in fahrenheit
    def convertFahrenheitToCelsius(fahrenheit):
        celsius = (5.0 / 9) * (fahrenheit- 32)
        return celsius


# fuction to calculate miles per gallons
def caculateMpg(galons_used, miles_driven):
    mpg = galons_used * miles_driven
    return mpg


# function calculateDistanceBetweenPoints 

# Distance Formula
# A(x1 , y1)
# B(x2 ,y2)	

# distance = sqrt((x1-x2)^2  + (y1-y2) ^2 ),y2
def distance(x1, y1, x2, y2):
    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** .5
    return dist
