def idealGasLaw (x):
    R = int(input("""Which gas unit constant would you like to use?
Write 1 for units in L*Pa/(K*mol)
Write 2 for units in L*atm/(K*mol)
Enter here: """))
    match R:
        case R if R == 1:
            R = 8.314462175
            unitP = " Pa"
        case R if R == 2:
            R = 0.082057461
            unitP = " atm"
        case R if R != 1 or R != 2 or R != int:
            print("Please enter 1 or 2!")
            idealGasLaw()
    if x == "P":
        V = float(input("Volume: "))
        N = float(input("Number of moles: "))
        T = float(input("Temperature: "))
        x = (N*R*T)/V
        P = str(x)
        print ("The calculated value for Pressure is: " + P + unitP)
    if x == "V":
        P = float(input("Pressure: "))
        N = float(input("Number of moles: "))
        T = float(input("Temperature: "))
        x = (N*R*T)/P
        V = str(x)
        print ("The calculated value for Volume is: " + V + " L")
    if x == "N":
        P = float(input("Pressure: "))
        V = float(input("Volume: "))
        T = float(input("Temperature: "))
        x = (P*V)/(R*T)
        N = str(x)
        print ("The calculated value for Number of Moles is: " + N + " mol")
    if x == "T":
        P = float(input("Pressure: "))
        V = float(input("Volume: "))
        N = float(input("Number of moles: "))
        x = (P*V)/(R*N)
        T = str(x)
        print ("The calculated value for Temperature is: " + T + " mol")
if __name__ == '__main__':
    print ("""Welcome to the Ideal Gas Law Solver!
Which variable would you like to solve for today?""")
    x = input("Please choose from P, V, N or T: ")
    idealGasLaw(x)