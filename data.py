import time


class Student:
    id: int
    name: str

    def __init__(self, id, name):
        self.id = id
        self.name = name


class Objective:
    id: int
    subject: str
    name: str
    desc: str
    objectiveClass: str

    def __init__(self, id, subject, name):
        self.id = id
        self.subject = subject
        self.name = name

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        return self.id != other.id


class ExamQuestion:
    number: str
    objectiveId: int
    weight: float

    result: int = 0

    def __init__(self, nr: str, objId: int, weight: float):
        self.number = nr
        self.objectiveId = objId
        self.weight = weight

class Exam:
    id: int
    name: str
    level: int
    subject: str

    teacher: str
    classe: str
    creation: time

    objectives: [ExamQuestion]

    def __init__(self, _id, datum, subject, numbers: list, objectives: list, weights: list):
        self.id = _id
        self.creation = datum
        self.subject = subject
        self.objectives = []
        assert len(numbers) == len(objectives) == len(weights)
        for i in range(len(numbers)):
            self.objectives.append(ExamQuestion(numbers[i], objectives[i], weights[i]))

        return

    def __str__(self):
        return "{ Klasse: " + self.classe + " " + self.subject + " Exam vom " + str(
            self.creation) + "|" + self.name + "}"

    def __repr__(self):
        return str(self.__dict__)


if __name__ == "__main__":
    print("hello WOrld")
