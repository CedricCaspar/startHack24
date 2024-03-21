from src.data import Objective, Exam, Student, Result

data = {"objectives": {0: Objective(0, "Ich kann Flächeninhalte schätzen.", "Mathematik"),
                    1: Objective(1, "Ich kann Fläche, Umfang & Seitenlange von Rechtecken bestimmen.", "Mathematik"),
                    2: Objective(2, "Ich kann Flächenmasse umwandeln.", "Mathematik"),
                    3: Objective(3, "Ich kann Aussagen zu einem Sachtext mit richtig oder falsch beurteilen.",
                                 "Deutsch"),
                    4: Objective(4, "Ich kann in Sätzen Kommas korrekt setzen.", "Deutsch"),
                    5: Objective(5, "Ich kann in Sätzen Bindewörter passend einsetzen.", "Deutsch"),
                    6: Objective(6, "Ich setze Rechtschreibung und Grammatik korrekt um.", "Deutsch")},
        "exams": [Exam(0, "17.04.24", "Deutsch", ["1", "1-2", "3"], [4, 6, 5], [0.25, 0.5, 0.25])],
        "classes": [[Student(0, "Alex"), Student(1, "Naomi")]],
        "results": []}


def printResults():
    print(data["results"])

def getResults():
    return data["results"]


def getExam(id):
    return data["exams"][id]


def getClasse():
    return data["classes"][0]


def getObjectives():
    return data["objectives"]


def getResultId(data, eId, sId, oId):
    for i in range(len(data["results"])):
        if data["results"][i].examId == eId and data["results"][i].studentId == sId and data["results"][i].objectiveId == oId:
            return i
    data["results"].append(Result(sId, eId, oId, None))
    return len(data["results"])-1


def getResult(data, eId, sId, oId):
    for i in range(len(data["results"])):
        if data["results"][i].examId == eId and data["results"][i].studentId == sId and data["results"][i].objectiveId == oId:
            return data["results"][i]
    data["results"].append(Result(sId, eId, oId, None))
    return data["results"][-1]


def setResult(data, eId, sId, oId, value):
    for i in range(len(data["results"])):
        if data["results"][i].examId == eId and data["results"][i].studentId == sId and data["results"][i].objectiveId == oId:
            data["results"][i].value = value
            return data["results"][i]
