def arealFirkant(laengdeFunc, breddeFunc):
    arealFuncFirkant = laengdeFunc * breddeFunc
    return arealFuncFirkant


if __name__ == '__main__':
    print("Dette program kan beregne Arealer af figurer => æøå!!!")

    laengde = float(input("Indtast Firkantens længde (m) : "))
    bredde = float(input("Indtast Firkantens bredde (m) : "))
    #laengde = 10
    #bredde = 6

    #areal = laengde * bredde
    areal = arealFirkant(laengde, bredde)

    print("Arealet af firkanten med længde %sm og bredde %sm er %sm2" %(laengde, bredde, areal))
