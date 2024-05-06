class Programmer:
    def __init__(self, name, language, experience):
        self.name = name
        self.language = language
        self.experience = experience

    def get_info(self):
        return f"Name: {self.name}, Language: {self.language}, Experience: {self.experience} years"

def main():
    programmers = [
        Programmer("Alice", "Python", 5),
        Programmer("Bob", "Java", 3),
        Programmer("Charlie", "C#", 7)
    ]

    for programmer in programmers:
        print(programmer.get_info())

if __name__ == "__main__":
    main()
