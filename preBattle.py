from tkinter import *
from Calculations import Calculations

def set_parameters():
    """Receives user input for the necessary values of the diagram and assigns them to variables"""
    root = Tk()
    
    char_role = IntVar()
    CheckVar1 = IntVar()
    enemy_role = IntVar()
    CheckVar2 = IntVar()
    CheckVar3 = IntVar()
    CheckVar4 = IntVar()
    
    root.title("Anime Battle Calculator")
    root.geometry("510x400+0+0")

    Label(root, text="Is the character a:", font=("time new roman",10)).place(x=20,y=10)
    Label(root, text="Has the character trained prior to this battle?", font=("time new roman",10)).place(x=20,y=70)
    Label(root, text="Is the enemy a:", font=("time new roman",10)).place(x=20,y=110)
    Label(root, text="Has the character lost to this enemy before?", font=("time new roman",10)).place(x=20,y=185)
    Label(root, text="If so, how many times?", font=("time new roman",10)).place(x=142,y=208)
    Label(root, text="Has a timeskip recently occured?", font=("time new roman",10)).place(x=20,y=250)
    Label(root, text="If so, how many battles has the character fought since the timeskip?", font=("time new roman",10)).place(x=20,y=273)
    Label(root, text="Is the character fighting to protect his friends?",font=("time new roman",10)).place(x=20,y=315)

    protagonist=Radiobutton(root, 
              text="Protagonist",
              padx = 20, 
              variable=char_role, 
              value=3).place(x=5,y=30)
    side_char=Radiobutton(root, 
              text="Side Character",
              padx = 20, 
              variable=char_role, 
              value=2).place(x=125,y=30)
    random_char=Radiobutton(root, 
              text="Random Character",
              padx = 20, 
              variable=char_role, 
              value=1).place(x=245,y=30)

    C1 = Checkbutton(root, variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 1).place(x=290, y=69)

    boss=Radiobutton(root, 
              text="Final Boss",
              padx = 20, 
              variable=enemy_role, 
              value=1).place(x=5,y=130)
    strong_lackey=Radiobutton(root, 
              text="Top Subordinate",
              padx = 20, 
              variable=enemy_role, 
              value=2).place(x=115,y=130)
    weak_lackey=Radiobutton(root, 
              text="Low Level Lackey",
              padx = 20, 
              variable=enemy_role, 
              value=3).place(x=245,y=130)

    times_lost=Entry(root) 
    times_lost.place(x=295,y=210)

    battles_fought=Entry(root) 
    battles_fought.place(x=370,y=273)
    """C4 = Checkbutton(root, variable = CheckVar4, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 1).place(x=370, y=273)"""

    def hasTimeskip():
        if CheckVar3.get() == 0:
            battles_fought.delete(0, len(times_lost.get())+1)
            battles_fought.config(state=DISABLED)
            return False
        else:
            battles_fought.config(state="normal")
            return True

    def hasCharLost():
        if CheckVar2.get() == 0:
            times_lost.delete(0, len(times_lost.get())+1)
            times_lost.config(state=DISABLED)
            return False
        else:
            times_lost.config(state="normal")
            return True

    C2 = Checkbutton(root, variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 1, command=hasCharLost).place(x=290, y=183)

    C3 = Checkbutton(root, variable = CheckVar3, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 1, command=hasTimeskip).place(x=220, y=250)

    C4 = Checkbutton(root, variable = CheckVar4, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 1).place(x=290, y=313)           

    def calculate():
        if char_role.get() == 0 or enemy_role.get() == 0:
            Label(root, text="*Ensure a radiobutton has been selected",
                  font=("time new roman",10), fg='red').place(x=20,y=245)
            return
        
        if hasCharLost():
            try:
                lost = int(times_lost.get())
            except ValueError:
                Label(root, text="*Please use integer values.",
                      font=("time new roman",10), fg='red').place(x=20,y=245)
                return
        if hasTimeskip():
            try:
                fought = int(battles_fought.get())
            except ValueError:
                Label(root, text="*Please use integer values.",
                      font=("time new roman",10), fg='red').place(x=20,y=245)
                return
        
        calc = Calculations(False, [char_role.get(), CheckVar1.get(),
                                    enemy_role.get(), CheckVar2.get(),
                                    int(times_lost.get()), CheckVar3.get(),
                                    int(battles_fought.get()), CheckVar4.get()])
        verdict = calc.get_verdict()
        print(verdict) 
     
    Button(root, text='Quit', width = 5,command=root.destroy).place(x=20,y=360)
    Button(root, text='Submit',width=5, command=calculate).place(x=100,y=360)

    hasCharLost()
    hasTimeskip()
    mainloop()

set_parameters()
