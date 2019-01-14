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

    def InputAnything(Message):
        UserInput = input(Message)
        return UserInput