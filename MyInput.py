class MyInput_Class:
    def InputFloat(Message):
        while True:
            try:
                UserInput = float(input(Message))
            except ValueError:
                print("Du skal indtast et helt tal eller et decimal tal (brug .) her !!!")
                continue
            else:
                return UserInput

    def InputInt(Message):
        while True:
            try:
                UserInput = int(input(Message))
            except ValueError:
                print("Du skal indtast et helt tal her !!!")
                continue
            else:
                return UserInput

    def InputIntUpperAndLowerLimit(Message, LowerLimit, UpperLimit):
        while True:
            UserInput = MyInput_Class.InputInt(Message)
            if UserInput >= LowerLimit and UserInput <= UpperLimit:
                break
            else:
                print("Husk at indtaste et tal i intervallet (%d - %d) !!!" % (LowerLimit, UpperLimit))
                continue
        return UserInput

    def InputAnything(Message):
        UserInput = input(Message)
        return UserInput