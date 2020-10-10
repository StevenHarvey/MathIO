#NOT FOR DISTRIBUTION UNDER ANY NAME THAN THE CREATOR OF THIS MODULE - "SWILLS" - ANY QUESTIONS OR ERRORS PLEASE MESSAGE ME(discord at bottom of module)
import datetime
import math
from fractions import Fraction
global errors
global timenow
timenow = datetime.datetime.now()
errors = []
logs = open('logs.txt', "a+")
logshh = open('logs.txt', "r")
logshand = logshh.readlines()
if len(logshand) < 1:
    starthand = ""
else:
    starthand = "\n"
class mathio():
    def avg(self):
        while True:
            try:
                sum = 0
                for i in self:
                    sum = sum + i
                final = sum/len(self)
                return final
            except TypeError as e:
                errors.append(starthand+'ERROR: '+str(TypeError)+" - "+str(e))
                logs.write(starthand+'ERROR: '+str(TypeError)+" - "+str(e)+" - "+str(timenow))
                return "Math Calculation Incomplete(Average) - Make sure the list is numbers only\n"+str(TypeError)+" - "+str(e)
    def prob(self, x, y):
        while True:
            try:
                if self == "data":
                    sum = 0
                    if x < y:
                        sum = (x/y)*100
                    elif x > y:
                        sum = (y/x)*100
                    elif x == y:
                        return 100
                    num = round(sum, 4)
                    if num == 0.0:
                        num = sum
                        return (num)
                    else:
                        return (num)
                elif self == "string":
                    sum = 0
                    if x < y:
                        sum = (x/y)*100
                    elif x > y:
                        sum = (y/x)*100
                    elif x == y:
                        return "100%"
                    num = round(sum, 4)
                    if num == 0.0:
                        num = sum
                        return str(num)+"%"
                    else:
                        return str(num)+"%"
                else:
                    return "ERROR: Please specify what type of output on the probability function (data or string)"
            except TypeError as e:
                errors.append(starthand+'ERROR: '+str(TypeError)+" - "+str(e))
                logs.write(starthand+'ERROR: '+str(TypeError)+" - "+str(e)+" - "+str(timenow))
                return "Math Calculation Incomplete(Average) - Make sure the list is numbers only\n"+str(TypeError)+" - "+str(e)
    def quadra(self, y, z):
        while True:
            try:
                a = self
                b = y
                c = z
                d = b**2-4*a*c
                if d < 0:
                    return "This equation has no real solution"
                elif d == 0:
                    x = (-b + math.sqrt(d)) / (2 * a)
                    return "This equation has one solutions: ", x
                else:
                    x2 = round((-b + math.sqrt(b**2 - 4*a*c)) / (2 * a),0)
                    x1 = round((-b - math.sqrt(b**2 - 4*a*c)) / (2 * a),0)

                return("Higher answer: {0}\nLower Answer: {1}").format(Fraction(x1), Fraction(x2))
            except TypeError as e:
                errors.append(starthand+'ERROR: '+str(TypeError)+" - "+str(e))
                logs.write(starthand+'ERROR: '+str(TypeError)+" - "+str(e)+" - "+str(timenow))
                return "Math Calculation Incomplete(Average) - Make sure the list is numbers only\n"+str(TypeError)+" - "+str(e)
    def distancexy(self,x1, x2, y1, y2):
        while True:
            try:
                if self == "data":
                    if (x2-x1) and (y2-y1) >= 0:
                        prt1 = math.sqrt((x2 - x1)*(x2 - x1))+((y2 - y1)*(y2 - y1))
                        return round(prt1)
                    elif (x2-x1) <= 0 and (y2-y1) > 0:
                        prt1 = math.sqrt((y2 - y1)*(y2 - y1))
                        return round(prt1)
                    elif (x2-x1) > 0 and (y2-y1) <= 0:
                        prt1 = math.sqrt(((x2 - x1)*(x2 - x1)))
                        return round(prt1)
                    else:
                        return "Failed - No clue why"
            except TypeError as e:
                errors.append(starthand+'ERROR: '+str(TypeError)+" - "+str(e))
                logs.write(starthand+'ERROR: '+str(TypeError)+" - "+str(e)+" - "+str(timenow))
                return "Math Calculation Incomplete(Average) - Make sure the list is numbers only\n"+str(TypeError)+" - "+str(e)