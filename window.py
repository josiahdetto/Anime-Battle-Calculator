from tkinter import *

def set_parameters():
    """Receives user input for the necessary values of the diagram and assigns them to variables"""
    root = Tk()
    
    char_role = IntVar()
    enemy_role = IntVar()
    CheckVar1 = IntVar()
    CheckVar2 = IntVar()
    CheckVar3 = IntVar()
    
    root.title("Anime Battle Calculator")
    root.geometry("500x320+0+0")

    Label(root, text="Is the character a:", font=("time new roman",10)).place(x=20,y=10)
    Label(root, text="Has the character trained prior to this battle?", font=("time new roman",10)).place(x=20,y=70)
    Label(root, text="Is the enemy a:", font=("time new roman",10)).place(x=20,y=110)
    Label(root, text="Has the character lost to this enemy before?", font=("time new roman",10)).place(x=20,y=170)
    Label(root, text="If so, how many times?", font=("time new roman",10)).place(x=142,y=193)
    Label(root, text="Is the character fighting to protect his friends?",font=("time new roman",10)).place(x=20,y=235)

    protagonist=Radiobutton(root, 
              text="Protagonist",
              padx = 20, 
              variable=char_role, 
              value=1).place(x=5,y=30)
    side_char=Radiobutton(root, 
              text="Side Character",
              padx = 20, 
              variable=char_role, 
              value=2).place(x=125,y=30)
    random_char=Radiobutton(root, 
              text="Random Character",
              padx = 20, 
              variable=char_role, 
              value=3).place(x=245,y=30)

    C1 = Checkbutton(root, variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 5).place(x=290, y=69)

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

    C2 = Checkbutton(root, variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 5).place(x=290, y=168)

    C3 = Checkbutton(root, variable = CheckVar3, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 5).place(x=290, y=233)
    
    times_lost=Entry(root) 

    times_lost.place(x=295,y=195)
     
    Button(root, text='Quit', width = 5,command=root.quit).place(x=20,y=280)
    Button(root, text='Submit',width=5, command=root.destroy).place(x=100,y=280)

    mainloop()

set_parameters()
