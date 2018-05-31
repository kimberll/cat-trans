"""
Start Screen
Takes In Player Name as typed input.
"""

from tkinter import *

def func1():    

    # Based off of tutorial on widgets 
    # http://www.tkdocs.com/tutorial/text.html

    root = Tk()

    # Get input from text box and then open home screen
    def getName():
        n=textBox.get("1.0","end-1c")
        root.destroy()
        # Runs Game.py
        from Game import run
        # Passes into the input which is the player name
        run(name = n)

    text = Label(text = "Hi, what is your name?", font = ("Calibri", 20), 
                    foreground = "black", background = "white")
    text.pack()
    textBox=Text(root, height=1, width=30, 
                    highlightbackground = "black", borderwidth=2)
    textBox.pack()
    button = Button(root, bg = 'black', text = 'Click to sign in', \
                    command=lambda: getName())
    button.pack()

    root.mainloop()

if __name__ == '__main__':
    func1()