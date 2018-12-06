
from tkinter import *

class App(Tk):
  def __init__(self):
    Tk.__init__(self)

    self.headerFont = ("Helvetica", "16", "bold italic")
    
    self.title("Grade Calculator")
    self.addLabs()
    self.addQuiz()
    self.addExams()
    self.addProj()
    self.addOutput()
    
  def addLabs(self):    
    """ add lab elements """
    # Labels can be anonymous (no variable created)
    # just 'chain' the grid command
    # use columnspan to span multiple columns
    # use font to adjust the font size
    Label(self, text = "Lab Assignments",
          font = self.headerFont).grid(columnspan = 2)

    #explicitly set row and column
    Label(self, text = "Percentage").grid(row = 1, column = 0)
    self.txtpcl = Entry(self)
    self.txtpcl.grid(row = 1, column = 1)
    # Entry's insert() method adds default text.
    # first parameter is position of cursor
    # second parameter is value to add
    self.txtpcl.insert(0, "0")

    Label(self, text = "%",).grid( row = 1, column = 3)

    Label(self, text = "Lab 1").grid(row = 2, column = 0)
    self.txtLab1 = Entry(self)
    self.txtLab1.grid(row = 2, column = 1)
    self.txtLab1.insert(0, "0")
    
    Label(self, text = "Lab 2").grid(row = 3, column = 0)
    self.txtLab2 = Entry(self)
    self.txtLab2.grid(row = 3, column = 1)
    self.txtLab2.insert(0, "0")
    
    Label(self, text = "Lab 3").grid(row = 4, column = 0)
    self.txtLab3 = Entry(self)
    self.txtLab3.grid(row = 4, column = 1)
    self.txtLab3.insert(0, "0")

  def addQuiz(self):
    """ add quiz elements """
    Label(self, text = "Quiz",
          font = self.headerFont).grid(row = 5, columnspan = 2)

    Label(self, text = "Percentage").grid(row = 6, column = 0)
    self.txtpcq = Entry(self)
    self.txtpcq.grid(row = 6, column = 1)
    self.txtpcq.insert(0, "0")
    Label(self, text = "%",).grid( row = 6, column = 3)

    Label(self, text = "Quiz 1").grid(row = 7, column = 0)
    self.txtQuiz1 = Entry(self)
    self.txtQuiz1.grid(row = 7, column = 1)
    self.txtQuiz1.insert(0, "0")

    Label(self, text = "Quiz 2").grid(row = 8, column = 0)
    self.txtQuiz2 = Entry(self)
    self.txtQuiz2.grid(row = 8, column = 1)
    self.txtQuiz2.insert(0, "0")

    Label(self, text = "Quiz 3").grid(row = 9, column = 0)
    self.txtQuiz3 = Entry(self)
    self.txtQuiz3.grid(row = 9, column = 1)
    self.txtQuiz3.insert(0, "0")

  def addExams(self):
    """ add exam elements """
    Label(self, text = "Exams",
          font = self.headerFont).grid(row = 10, columnspan = 2)

    Label(self, text = "Percentage").grid(row = 11, column = 0)
    self.txtpce = Entry(self)
    self.txtpce.grid(row = 11, column = 1)
    self.txtpce.insert(0, "0")
    Label(self, text = "%",).grid( row = 11, column = 3)

    Label(self, text = "Midterm Exam").grid(row = 12, column = 0)
    self.txtMT = Entry(self)
    self.txtMT.grid(row = 12, column = 1)
    self.txtMT.insert(0, "0")

    Label(self, text = "Final Exam").grid(row = 13, column = 0)
    self.txtFE = Entry(self)
    self.txtFE.grid(row = 13, column = 1)
    self.txtFE.insert(0, "0")

  def addProj(self):
    """ add project """
    Label(self, text = "Final Project",
          font = self.headerFont).grid(row = 14, columnspan = 2)

    Label(self, text = "Percentage").grid(row = 15, column = 0)
    self.txtpcp = Entry(self)
    self.txtpcp.grid(row = 15, column = 1)
    self.txtpcp.insert(0, "0")

    Label(self, text = "%",).grid( row = 16, column = 3)

    Label(self, text = "Project").grid(row = 16, column = 0)
    self.txtFP = Entry(self)
    self.txtFP.grid(row = 16, column = 1)
    self.txtFP.insert(0, "0")

  def addOutput(self):
    """ add button and output elements """
    self.btnCalc = Button(self, text = "Show me hell!")
    self.btnCalc.grid(row = 17, columnspan = 2)
    self.btnCalc["command"] = self.calculate
    
    Label(self, text = "Lab Percent").grid(row = 18, column = 0)
    # more attributes can be set in constructor:
    # bg = background color, fg = foreground color
    # anchor determines alignment ("nsew")
    # relief is border
    self.lblLabs = Label(self, bg = "#fff", anchor = "w", relief = "groove")
    #sticky propery in grid changes width and height
    self.lblLabs.grid(row = 18, column = 1, sticky = "we")

    Label(self, text = "Quiz Percent").grid(row = 19, column = 0)
    self.lblQuizes = Label(self, bg = "#fff", anchor = "w", relief = "groove")
    self.lblQuizes.grid(row = 19, column = 1, sticky = "we")
    
    Label(self, text = "Exam Percent").grid(row = 20, column = 0)
    self.lblExams = Label(self, bg = "#fff", anchor = "w", relief = "groove")
    self.lblExams.grid(row = 20, column = 1, sticky = "we")
    
    Label(self, text = "Overall Percent").grid(row = 21, column = 0)
    self.lblTotal = Label(self, bg = "#fff", anchor = "w", relief = "groove")
    self.lblTotal.grid(row = 21, column = 1, sticky = "we")
    
  def calculate(self):
    """ calculate the grades """
    
    #get lab average
    pcL  = int(self.txtpcl.get())
    lab1 = int(self.txtLab1.get())
    lab2 = int(self.txtLab2.get())
    lab3 = int(self.txtLab3.get())
    
    labTot = lab1 + lab2 + lab3
    labPerc = labTot / 3.0
    
    self.lblLabs["text"] = "%.2f" % labPerc

    #get quiz average
    pcQ = int(self.txtpcq.get())
    quiz1 = int(self.txtQuiz1.get())
    quiz2 = int(self.txtQuiz2.get())
    quiz3 = int(self.txtQuiz3.get())

    quizTot = quiz1 + quiz2 + quiz3
    quizPerc = quizTot / 3.0

    self.lblQuizes["text"] = "%.2f" % quizPerc
    
    #get exam average
    pcE  = int(self.txtpce.get())
    mt = int(self.txtMT.get())
    fe = int(self.txtFE.get())
    
    examPerc = (mt + fe) / 2.0
    self.lblExams["text"] = "%.2f" % examPerc
    
    #project percentage needs no more calculation
    projPerc = int(self.txtFP.get())
    pcP  = int(self.txtpcp.get())
    #calculate total percentage
    total = (labPerc * pcL/100) + (examPerc * pcE/100) + (projPerc * pcP/100) + (quizPerc *pcQ/100)
    self.lblTotal["text"] = "%.2f" % total

    
def main():
  app = App()
  app.mainloop()

if __name__ == "__main__":
  main()
