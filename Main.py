import math
import MyInput

def arealFirkant(laengdeFunc, breddeFunc):
    arealFuncFirkant = laengdeFunc * breddeFunc
    return arealFuncFirkant

def arealCirkel(radiusFunc):
    # De 2 linjer herunder gør det samme. ** er en speciel Python syntaks,
    # der mener opløftet i anden.
    #arealFuncCirkel = radiusFunc ** 2 * math.pi
    arealFuncCirkel = radiusFunc * radiusFunc * math.pi
    return arealFuncCirkel

def printStringsInList(currentList):
    for value in currentList:
        print(value)


if __name__ == '__main__':
    printout_List = []
    printout_List.append("0 : Stop program")
    printout_List.append("1 : Beregn areal af Firkant")
    printout_List.append("2 : Beregn areal af Cirkel")
    printout_List.append("3 : Beregn areal af Trapez")

    print("Dette program kan beregne Arealer af figurer => æøå!!!")

    while True:
        text = input("Tryk <Enter> key for at komme videre !!!")
        if text == "":
            break
        else:
            print("Tryk nu <Enter> !!!")
            continue

    while True:
        print("Indtast Programvalg")
        printStringsInList(printout_List)

        informationString = "Indtast Programvalg (0 - " + str(len(printout_List) - 1) + ") : "
        runAgain = MyInput.MyInput_Class.InputIntUpperAndLowerLimit(informationString, 0, len(printout_List) - 1)

        if 0 == runAgain:
            break

        if 1 == runAgain:
            laengde = MyInput.MyInput_Class.InputFloat("Indtast Firkantens længde (m) : ")
            bredde = MyInput.MyInput_Class.InputFloat("Indtast Firkantens bredde (m) : ")

            arealPaaFirkant = arealFirkant(laengde, bredde)

            print("Arealet af firkanten med længde %sm og bredde %sm er : %sm2" %(laengde, bredde, arealPaaFirkant))

        elif 2 == runAgain:
            radius = MyInput.MyInput_Class.InputFloat("Indtast cirklens radius (m) : ")

            arealPaaCirkel = arealCirkel(radius)

            print("Arealet af cirklen med radius %sm er : %sm2" % (radius, arealPaaCirkel))