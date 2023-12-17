from calculators.calculator_simplu import CalculatorSimplu

initial_value = float(input("Introdu valoarea initiala (initial este  0): "))
calculator = CalculatorSimplu(initial_value)

while True:
    user_input = input("> ")

    if user_input.lower() == "x":
        break

    try:
        user_input_parts = user_input.split()
        if user_input_parts:
            operation = user_input_parts[0]
            values = user_input_parts[1:]
            if values:
                value = float(values[0])
            else:
                value = None

        if "+" == operation :
            calculator.adunare(value)
        elif operation == "-":
            calculator.scadere(value)
        elif operation == "*":
            calculator.Inmultire(value)
        elif operation == "/":
            if value != 0:
                calculator.Impartire(value)
            else:
                print("Operatie invalida.Nu se poate imparti la 0.")
        elif operation == "=":
            calculator.set_value(value)
        else:
            print("Operatie invalida")

        calculator.display_result()

    except ValueError:
        print("Introdu un numar valid.")

    except KeyboardInterrupt:
        print("\nProgram terminated.")
