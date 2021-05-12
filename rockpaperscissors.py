from tkinter import * 
import random

root=Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('Rock Paper Scissors')
root.config(bg='#856ff8')

Label(root,text = 'Rock, Paper, Scissors', font = 'arial 20 bold', bg = 'seashell2').pack()

user_take=StringVar()
Label(root, text = 'Choose any one:Rock, Paper, Scissors', font = 'arial 15 bold', bg = 'seashell2').place(x = 20,y = 70)
Entry(root, font = 'arial 15', textvariable = user_take, bg = 'antiquewhite2').place(x = 90, y = 120)

comp_pick=random.randint(1,3)
if comp_pick == 1:
    comp_pick='Rock'
elif comp_pick == 2:
    comp_pick='Paper'
else:
    comp_pick='Scissors'

Result = StringVar()

def play():
    user_pick = user_take.get()
    if user_pick == comp_pick:
        Result.set('Tie, U have both selected the same thing!')
    elif user_pick == 'Rock' and comp_pick == 'Paper':
        Result.set('You Loose, Computer Wins..Computer Selected Paper')
    elif user_pick == 'Rock' and comp_pick == 'Scissors':
        Result.set('You Win, Computer Looses..Computer Selected Scissors')
    elif user_pick == 'Paper' and comp_pick == 'Rock':
        Result.set('You Win, Computer Looses..Computer Selected Rock')
    elif user_pick == 'Paper' and comp_pick == 'Scissors':
        Result.set('You Loose, Computer Wins..Computer Selected Scissors')
    elif user_pick == 'Scissors' and comp_pick == 'Rock':
        Result.set('You Loose, Computer Wins..Computer Selected Rock')
    elif user_pick == 'Scissors' and comp_pick == 'Paper':
        Result.set('You Win, Computer Looses..Computer Selected Paper')
    else:
        Result.set('Invalid! Choose any one - Rock, Paper, Scissors')

def Reset():
    Result.set("")
    user_take.set("")

def Exit():
    root.destroy()

Entry(root, font='arial 10 bold', textvariable = Result, bg='antiquewhite2', width=50).place(x=25, y=250)

Button(root, font='arial 13 bold', text='PLAY',  padx=5, bg='seashell4', command = play).place(x=150, y=190)

Button(root, font='arial 13 bold', text='RESET', padx=5, bg='seashell4', command = Reset).place(x=70, y=310)

Button(root, font='arial 13 bold', text='EXIT',  padx=5, bg='seashell4', command = Exit).place(x=230, y=310)

root.mainloop()