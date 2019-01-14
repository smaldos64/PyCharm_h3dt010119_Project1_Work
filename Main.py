import math
import MyInput

def arealFirkant(laengdeFunc, breddeFunc):
    arealFuncFirkant = laengdeFunc * breddeFunc
    return arealFuncFirkant

def arealCirkel(radiusFunc):
    # De 2 linjer herunder gør det samme. ** er en spciel Python syntaks,
    # der mener opløftet i anden.
    #arealFuncCirkel = radiusFunc ** 2 * math.pi
    arealFuncCirkel = radiusFunc * radiusFunc * math.pi
    return arealFuncCirkel


if __name__ == '__main__':
    print("Dette program kan beregne Arealer af figurer => æøå!!!")

    while True:
        print("Indtast Programvalg")
        print("0 : Stop program")
        print("1 : Beregn areal af Firkant")
        print("2 : Beregn areal af Cirkel")
        print("3 : Beregn areal af Trapez")

        #runAgain = int(input("Indtast Programvalg : "))
        runAgain = MyInput.MyInput_Class.InputInt("Indtast Programvalg (0 - 3) : ")

        if 0 == runAgain:
            break

        if 1 == runAgain:
            #laengde = float(input("Indtast Firkantens længde (m) : "))
            laengde = MyInput.MyInput_Class.InputFloat("Indtast Firkantens længde (m) : ")
            #bredde = float(input("Indtast Firkantens bredde (m) : "))
            bredde = MyInput.MyInput_Class.InputFloat("Indtast Firkantens bredde (m) : ")

            arealPaaFirkant = arealFirkant(laengde, bredde)

            print("Arealet af firkanten med længde %sm og bredde %sm er : %sm2" %(laengde, bredde, arealPaaFirkant))

        elif 2 == runAgain:
            #radius = float(input("Indtast cirklens radius (m) : "))
            radius = MyInput.MyInput_Class.InputFloat("Indtast cirklens radius (m) : ")

            arealPaaCirkel = arealCirkel(radius)

            print("Arealet af cirklen med radius %sm er : %sm2" % (radius, arealPaaCirkel))