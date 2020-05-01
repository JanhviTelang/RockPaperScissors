from tkinter import *

import random

root = Tk()
root.title("Rock Paper Scissor")
width = 570
height = 520
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="#99ff99")

#IMAGES
blank_img=PhotoImage(file="images/blank.png")
user_rock=PhotoImage(file="images/user_rock.png")
sm_user_rock=user_rock.subsample(3, 3)
user_paper=PhotoImage(file="images/user_paper.png")
sm_user_paper=user_paper.subsample(3, 3)
user_scissors=PhotoImage(file="images/user_scissors.png")
sm_user_scissors=user_scissosr.subsample(3, 3)
comp_rock=PhotoImage(file="images/comp_rock.png")
comp_paper=PhotoImage(file="images/comp_paper.png")
comp_scissors=PhotoImage(file="images/comp_scissors.png")

#PROCEDURE
def Rock():
    global user_choice
    user_choice = 1
    user_img.configure(image=user_rock)
    MatchProcess()
 
def Paper():
    global user_choice
    user_choice = 2
    user_img.configure(image=user_paper)
    MatchProcess()
    
def Scissor():
    global user_choice
    user_choice = 3
    user_img.configure(image=user_scissor)
    MatchProcess()

def MatchProcess():
    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_img.configure(image=comp_rock)
        ComputerRock()
    elif comp_choice == 2:
        comp_img.configure(image=comp_paper)
        ComputerPaper() 
    elif comp_choice == 3:
        comp_img.configure(image=comp_scissors)
        CompututerScissors()

def ComputerRock():
    if user_choice == 1:
        lbl_status.config(text="Game Tie")
    elif user_choice == 2:
        lbl_status.config(text="Player Win")
    elif user_choice == 3:
        lbl_status.config(text="Computer Win")
           
def ComputerPaper():
    if user_choice == 1:
        lbl_status.config(text="Computer Win")
    elif user_choice == 2:
        lbl_status.config(text="Game Tie")
    elif user_choice == 3:
        lbl_status.config(text="Player Win")
    
def CompututerScissors():
    if user_choice == 1:
        lbl_status.config(text="Player Win")
    elif user_choice == 2:
        lbl_status.config(text="Computer Win")
    elif user_choice == 3:
        lbl_status.config(text="Game Tie")

def ExitApp():
    root.destroy()
    exit()

#LABELS
user_img = Label(root,image=blank_img)
comp_img = Label(root,image=blank_img)
lbl_user = Label(root,text="PLAYER")
lbl_user.grid(row=1, column=1)
lbl_user.config(bg="#99ff99")
lbl_computer = Label(root,text="COMPUTER")
lbl_computer.grid(row=1, column=3)
lbl_computer.config(bg="#99ff99")
lbl_status=Label(root, text="", font=('arial', 8))
lbl_status.config(bg="#99ff99")
user_img.grid(row=2,column=1, padx=30, pady=20)
comp_img.grid(row=2,column=3, pady=20)
lbl_status.grid(row=3, column=2)

#BUTTONS
rock = Button(root, image=sm_user_rock, command=Rock)
paper = Button(root, image=sm_user_paper, command=Paper)
scissors = Button(root, image=sm_user_scissors, command=Scissors)
btn_quit = Button(root, text="Quit", command=ExitApp)
rock.grid(row=4,column=1, pady=30)
paper.grid(row=4,column=2, pady=30)
scissors.grid(row=4,column=3, pady=30)
btn_quit.grid(row=5, column=2)

#INITIALIZE
if __name__ == '__main__':
    root.mainloop()

