from tkinter import*
import tkinter.font as font
import random
screen = Tk()
screen.geometry("800x500")

title_label = Label(screen,text="Rock Paper Scissors",font=font.Font(size=30)).place(x=200,y=20)
start_game = Label(screen,text="Let's start the Game",font=font.Font(size=20)).place(x=200,y=100)
options_label = Label(screen,text="Your Options: ",font=font.Font(size=15)).place(x=200,y=150)
score_label = Label(screen,text="Score: ",font=font.Font(size=15)).place(x=200,y=300)
options = [("rock",0),("paper",1),("scissors",2)]
computer_score = 0
player_score = 0

def computer_win():
    global computer_score,player_score
    computer_score += 1
    start_game.config(text="Computer Won")
    you_score.config(text="Your score: " + str(player_score))
    comp_score.config(text="Computer Score: " + str(computer_score))

def computer_sel():
    return random.choice(options)

def player_sel(choice):
    computer_choice = computer_sel()
    you_sel.config(text="You selected: " + choice[0])
    comp_sel.config(text="Computer Selected: " + computer_choice[0] )





rock_button = Button(screen,text="Rock",width=5)
rock_button.place(x=300,y=200)
paper_button = Button(screen,text="Paper",width=5)
paper_button.place(x=400,y=200)
scissors_button = Button(screen,text="Scissors",width=5)
scissors_button.place(x=500,y=200)

you_sel = Label(screen,text="You Selected: ").place(x=300,y=350)
comp_sel = Label(screen,text="Computer Selected: ").place(x=300,y=400)

you_score = Label(screen,text="Your score: ").place(x=500,y=350)
comp_score = Label(screen,text="Computer score: ").place(x=500,y=400)

