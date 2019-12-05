class Studentinfo:

    def __init__(self,ID,firstName,lastName,gender,birthdate,gradeHW,gradeParticipation,gradeQuiz,gradeFinalExam):
        self.ID = ID
        self.fullName = firstName + " " + lastName
        self.email = firstName + "." + lastName + "@edu.aua.am"
        self.birthdate = birthdate
        self.gender = gender
        self.gradeHW = gradeHW
        self.gradeParticipation = gradeParticipation
        self.gradeQuiz = gradeQuiz
        self.gradeFinalExam = gradeFinalExam

    def getPersonalInfo(self):
        print(self.fullName)
        print(self.ID)
        print(self.email)
        print(self.gender)
        print(self.birthdate)
        print("__________________________ \n|||||||||||||||||||||||||| \n" )
    def getCurrentGrade(self):
        print(self.fullName)
        self.gradeHW = (self.gradeHW * 0.10)
        print("HW: ",self.gradeHW,"%")
        self.gradeParticipation = (self.gradeParticipation * 0.20)
        print("Participation: ",self.gradeParticipation,"%")
        self.gradeQuiz = (self.gradeQuiz * 0.30)
        print("Quiz: ", self.gradeQuiz,"%")
        self.gradeFinalExam = (self.gradeFinalExam*0.40)
        print("Final Exam: ", self.gradeFinalExam,"%")
        self.finalGrade = round(self.gradeHW+self.gradeQuiz+self.gradeParticipation+self.gradeFinalExam)
        print("Full Grade: ",self.finalGrade,"%")
        print("__________________________ \n|||||||||||||||||||||||||| \n" )

def main():
    st1 = Studentinfo("789456", "Hayk", "Tamazyan", "Male", "15/01/1999", 92, 80, 72, 85)
    st2 = Studentinfo("858797", "Ashot", "Erkat", "Male", "01/01/2018", 84, 99, 92, 89)

    st1.getPersonalInfo()
    st2.getPersonalInfo()

    st1.getCurrentGrade()
    st2.getCurrentGrade()

main()
