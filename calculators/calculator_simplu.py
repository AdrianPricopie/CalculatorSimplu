class CalculatorSimplu:
    def __init__(self, initial_value=0.0):
        self.current_value = initial_value

    def adunare(self, num):
        self.current_value += num

    def scadere(self, num):
        self.current_value -= num

    def Inmultire(self, num):
        self.current_value *= num

    def Impartire(self, num):
        if num != 0:
            self.current_value /= num
        else:
            print("Operatie invalida. Nu se poate imparti la zero.")

    def set_value(self, num):
        self.current_value = num

    def display_result(self):
        print(self.current_value)

