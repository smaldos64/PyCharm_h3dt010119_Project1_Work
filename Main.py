import math
import MyInput
import os
import sys
from enum import Enum

class MathOperation(Enum):
    AREA_SQUARE = 1,
    AREA_TRIANGLE = 2,
    AREA_TRAPEZ = 3,
    AREA_CIRCLE = 4

    def __int__(self):
        return self.value

def arealFirkant(laengdeFunc, breddeFunc):
    arealFuncFirkant = laengdeFunc * breddeFunc
    return arealFuncFirkant

def arealCirkel(radiusFunc):
    # De 2 linjer herunder gør det samme. ** er en speciel Python syntaks,
    # der mener opløftet i anden.
    #arealFuncCirkel = radiusFunc ** 2 * math.pi
    arealFuncCirkel = radiusFunc * radiusFunc * math.pi
    return arealFuncCirkel

def arealTrapez(side_a_Func, side_b_Func, heightFunc):
    arealTrapez = 0.5 * (side_a_Func + side_b_Func) * heightFunc
    return arealTrapez

def arealTrekant(baselineFunc, heightFunc):
    arealTrekant = 0.5 * baselineFunc * heightFunc
    return arealTrekant

def GetStringList():
    stringList = []
    stringList.append("0 : Stop program")
    stringList.append("1 : Beregn areal af Firkant")
    stringList.append("2 : Beregn areal af Cirkel")
    stringList.append("3 : Beregn areal af Trapez")
    stringList.append("4 : Beregn areal af Trekant")

    return (stringList)

def PrintStringsInList(currentList):
    for value in currentList:
        print(value)

def WaitForUserPressOnEnterKey():
    while True:
        text = input("Tryk <Enter> key for at komme videre !!!")
        if text == "":
            break
        else:
            print("Tryk nu <Enter> !!!")
            continue

def PerformMathOperation(thisMathOperation):
    if MathOperation.AREA_SQUARE.value[0] == thisMathOperation:
        laengde = MyInput.MyInput_Class.InputFloat("Indtast Firkantens længde (m) : ")
        bredde = MyInput.MyInput_Class.InputFloat("Indtast Firkantens bredde (m) : ")

        arealPaaFirkant = arealFirkant(laengde, bredde)

        print("Arealet af firkanten med længde %sm og bredde %sm er : %sm2" % (laengde, bredde, arealPaaFirkant))

    elif MathOperation.AREA_CIRCLE[0] == thisMathOperation:
        radius = MyInput.MyInput_Class.InputFloat("Indtast cirklens radius (m) : ")

        arealPaaCirkel = arealCirkel(radius)

        print("Arealet af cirklen med radius %sm er : %sm2" % (radius, arealPaaCirkel))

    elif MathOperation.AREA_TRAPEZ[0] == thisMathOperation:
        side_a = MyInput.MyInput_Class.InputFloat("Indtast trapez sidelængde a (m) : ")
        side_b = MyInput.MyInput_Class.InputFloat("Indtast trapez sidelængde b (m) : ")
        height = MyInput.MyInput_Class.InputFloat("Indtast trapez højde (m) : ")

        arealPaaTrapez = arealTrapez(side_a, side_b, height)

        print("Arealet af trapez med side a %sm og side b %sm og højde %sm er : %sm2" % (side_a, side_b, height, arealPaaTrapez))

    elif MathOperation.AREA_TRIANGLE[0] == thisMathOperation:
        baseline = MyInput.MyInput_Class.InputFloat("Indtast trekant grundlinjelængde(m) : ")
        height = MyInput.MyInput_Class.InputFloat("Indtast trekant højde (m) : ")

        arealPaaTrekant = arealTrekant(baseline, height)

        print("Arealet af trekant med grundlinje %sm og højde %sm er : %sm2" % (baseline, height, arealPaaTrekant))


if __name__ == '__main__':
    printout_List = GetStringList()

    print("Dette program kan beregne Arealer af figurer => æøå!!!")

    while True:
        print("Indtast Programvalg")
        PrintStringsInList(printout_List)

        informationString = "Indtast Programvalg (0 - " + str(len(printout_List) - 1) + ") : "
        runAgain = MyInput.MyInput_Class.InputIntUpperAndLowerLimit(informationString, 0, len(printout_List) - 1)

        if 0 == runAgain:
            sys.exit(0)
        else:
            PerformMathOperation(runAgain)

        WaitForUserPressOnEnterKey()

        os.system('cls')