class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        return self.number ** 2

    def cube(self):
        return self.number ** 3

def main():
    num = 5
    calc = Calculator(num)
    print(f"Square of {num} is {calc.square()}")
    print(f"Cube of {num} is {calc.cube()}")

if __name__ == "__main__":
    main()
