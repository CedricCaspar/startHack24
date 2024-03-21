from data import Objective, Exam, Student

objectives: dict = {0: Objective(0, "Ich kann Flächeninhalte schätzen", "Mathematik"),
                    1: Objective(1, "Ich kann Fläche, Umfang & Seitenlange von Rechtecken bestimmen", "Mathematik"),
                    2: Objective(2, "Ich kann Flächenmasse umwandeln", "Mathematik"),
                    3: Objective(3, "Ich kann Aussagen zu einem Sachtext mit richtig oder falsch beurteilen", "Deutsch"),
                    4: Objective(4, "Ich kann in Sätzen Kommas korrekt setzen", "Deutsch"),
                    5: Objective(5, "Ich kann in Sätzen Bindewörter passend einsetzen", "Deutsch"),
                    6: Objective(6, "Ich setze Rechtschreibung und Grammatik korrekt um", "Deutsch")}

exams = [Exam(0, "17.04.24", "Deutsch", ["1", "1-2", "3"], [4, 6, 5], [0.25, 0.5, 0.25])]
classe = [Student]

def getExam(id):
    return exams[id]
