class Company:
    levels = {1: "junior", 2: "middle", 3: "senior", 4: "lead"}

    def __init__(self, index):
        self._index = index
        self._level = Company.levels[index]

    def _level_up(self):
        if self._index < len(Company.levels):
            self._index += 1
            self._level = Company.levels[self._index]

    def is_lead(self):
        return self._index == len(Company.levels)

class Programmer(Company):
    def __init__(self, name, age, level):
        super().__init__(level)
        self.name = name
        self.age = age

    def work(self):
        self._level_up()

    def info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Level: {self._level}")

    @staticmethod
    def knowledge_base():
        print("This is a programming knowledge base.")


Programmer.knowledge_base()

programmer = Programmer("Mike", 25, 1)

while not programmer.is_lead():
    programmer.work()

programmer.info()