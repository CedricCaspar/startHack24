import time


class Student:
    name: str
    id: int


class Objective:
    name: str
    desc: str


class Exam:
    id: int
    name: str
    level: int
    subject: str

    classe: str
    creation: time

    objectives: [Objective]

    def __init__(self, _id):
        self.id = _id
        self.creation = time.time()
        return

    def __str__(self):
        return "{ Klasse: " + self.classe + " " + self.subject + " Exam vom " + str(
            self.creation) + "|" + self.name + "}"

    def __repr__(self):
        return str(self.__dict__)


if __name__ == "__main__":
    print("hello WOrld")
