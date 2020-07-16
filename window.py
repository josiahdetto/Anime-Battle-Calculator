from tkinter import *

def set_parameters():
    """Receives user input for the necessary values of the diagram and assigns them to variables"""
    root = Tk()
    root.title("Telescope Simulation")
    root.geometry("500x320+0+0")

    Label(root, text="Enter the height of the object(cm)", font=("time new roman",10)).place(x=20,y=20)
    Label(root, text="Enter the object distance from the objective lens(cm)", font=("time new roman",10)).place(x=20,y=70)
    Label(root, text="Enter the focal point of the objective lens(cm)", font=("time new roman",10)).place(x=20,y=120)
    Label(root, text="Enter the focal point of the ocular lens(cm)", font=("time new roman",10)).place(x=20,y=170)
    Label(root, text="Enter the distance between the two lens(cm)",font=("time new roman",10)).place(x=20,y=220)

    height_object=Entry(root)
    distance_object=Entry(root)
    focal_objective=Entry(root)
    focal_ocular=Entry(root)
    len_distance=Entry(root) 

    height_object.place(x=225,y=20)
    distance_object.place(x=340, y=70)
    focal_objective.place(x=300,y=120)
    focal_ocular.place(x=275,y=170)
    len_distance.place(x=295,y=220)
     
    Button(root, text='Quit', width = 5,command=root.quit).place(x=20,y=270)
    Button(root, text='Submit',width=5, command=root.destroy).place(x=100,y=270)

    mainloop()

set_parameters()
