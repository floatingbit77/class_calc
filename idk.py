from tkinter import *

class window1():
    def __init__(self):
        self.master=Tk()
        self.master.title("Grade Calculator")
        self.label=Label(self.master, text="Enter your three test grades so far")
        self.label.grid(column=0, row=1)
        self.label1=Label(self.master, text="what is your goal grade to make?")
        self.label1.grid(column=0, row=0)
        self.ent0=Entry(self.master)
        self.ent0.grid(column=1, row=0)
        self.ent1=Entry(self.master)
        self.ent1.grid()
        self.lbl1 = Label(self.master, text="Test 1 Score")
        self.lbl1.grid(column=1, row=2)
        self.ent2 = Entry(self.master)
        self.ent2.grid()
        self.lbl2 = Label(self.master, text="Test 2 Score")
        self.lbl2.grid(column=1, row=3)
        self.ent3 = Entry(self.master)
        self.ent3.grid()
        self.lbl3 = Label(self.master, text="Test 3 Score")
        self.lbl3.grid(column=1, row=4)
        self.button1 = Button(self.master, text="go", command=self.on_click)
        self.button1.grid()
        self.master.mainloop()
    def on_click(self):
        self.result1=float(self.ent1.get())
        self.result2 = float(self.ent2.get())
        self.result3 = float(self.ent3.get())
        self.result0=float(self.ent0.get())
        print(self.result1, self.result2, self.result3, self.result0)
        self.v1=self.result1*0.25
        self.v2=self.result2*0.25
        self.v3=self.result3*0.25
        print(self.v1, self.v2, self.v3)
        self.add_3=self.v1 + self.v2 + self.v3
        print(self.add_3)
        self.small_grade=self.result0 - self.add_3
        print(self.small_grade)
        self.overall_aim_grade=self.small_grade * 4
        print(self.overall_aim_grade)
        self.flt=StringVar()
        self.flt.set(self.overall_aim_grade)
        self.new_label=Label(self.master, text="You need to make at least a: ")
        self.new_label1=Label(self.master, textvariable=self.flt)
        self.new_label.grid(column=1, row=10)
        self.new_label1.grid(column=3, row=10)



window1()
