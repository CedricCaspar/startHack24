import time


class Result:
    studentId: int
    examId: int
    objectiveId: int

    value: int

    def __init__(self, sId, eId, oId, value):
        self.studentId = sId
        self.examId = eId
        self.objectiveId = oId
        self.value = value

    def __str__(self):
        return "("+str(self.studentId) + ", " + str(self.examId) + ", " + str(self.objectiveId) + " => " + str(self.value)+")"

    def __repr__(self):
        return "( s:"+str(self.studentId) + ", e:" + str(self.examId) + ", o:" + str(self.objectiveId) + " => v:" + str(self.value) + ")"

    def __eq__(self, other):
        return self.studentId == other.studentId and self.examId == other.examId and self.objectiveId == other.objectiveId

    def __ne__(self, other):
        return not self.__eq__(other)


class Student:
    id: int
    name: str

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return self.name


class Objective:
    id: int
    subject: str
    objective: str
    competency: str
    objectiveClass: str

    def __init__(self, id, name, subject, competency, uid):
        self.id = id
        self.subject = subject
        self.objective = name
        self.competency = competency
        self.uid = uid

    def __eq__(self, other):
        return self.objective == other.objective

    def __ne__(self, other):
        return self.id != other.id

    def __repr__(self):
        return str(self.subject) + "|" + self.objective


class ExamQuestion:
    number: str
    objectiveId: int
    weight: float

    def __init__(self, nr: str, objId: int, weight: float):
        self.number = nr
        self.objectiveId = objId
        self.weight = weight

    def __str__(self):
        return "Aufgabe: " + self.number + ", Objective: " + str(self.objectiveId) + ", weight: " + str(self.weight)


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
