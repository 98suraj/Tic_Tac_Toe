from tkinter import *
import tkinter.messagebox    

click = True
tk = None
b=0
c=0
def start():
    global tk
    tk = Tk()
    tk.title("Tic Tac Toe")
    
    
    def play(button):
        global click, tk,c,b
        if button["text"] == " " and click:
            button["text"] = "X"
            click = False
        elif button["text"] == " ":
            button['text'] = "O"
            click = True
        if button["text"] == "X":
            button["bg"] = "red"
        if button["text"] == "O":
            button["bg"] = "yellow"

            
        if (button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
            button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or
            button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
            button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
            button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
            button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X" or
            button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
            button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X"):
            c=c+1
            answer = tkinter.messagebox.askquestion('X Player wins!!!', 'X='+str(c)+'   O='+str(b)+'\rDo you want to play again')
            if answer == 'yes': start()
            else:   tk.destroy()

        elif (button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or
            button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or
            button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or
            button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or
            button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
            button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O" or
            button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or
            button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O"):
            b=b+1
            answer = tkinter.messagebox.askquestion('O Player wins!!!', 'X='+str(c)+'   O='+str(b)+'\rDo you want to play again')
            if answer == 'yes': start()
            else:
                tk.destroy()
        elif(button1["text"]!=" " and button2["text"]!=" " and button3["text"]!=" " and button4["text"]!=" " and button5["text"]!=" " and button6["text"]!=" " and
             button7["text"]!=" " and button8["text"]!=" " and button9["text"]!=" "):
            answer=tkinter.messagebox.askquestion('Draw match', 'X='+str(c)+'   O='+str(b)+'\rDo you want to play again')
            if answer=="yes":
                start()
            else:
                tk.destroy()
            

    button1 = Button(tk,text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button1), bg='sky blue')
    button1.grid(row=0, column=0)

    button2 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button2),bg='sky blue')
    button2.grid(row=0, column=1)

    button3 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button3),bg='sky blue')
    button3.grid(row=0, column=2)

    button4 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button4),bg='sky blue')
    button4.grid(row=1, column=0)

    button5 = Button(tk, text=" ", font=("Times 26 bold"), height=4, width=8, command=lambda:play(button5),bg='sky blue')
    button5.grid(row=1, column=1)

    button6 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button6),bg='sky blue')
    button6.grid(row=1, column=2)

    button7 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button7),bg='sky blue')
    button7.grid(row=2, column=0)

    button8 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button8),bg='sky blue')
    button8.grid(row=2, column=1)

    button9 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button9),bg='sky blue')
    button9.grid(row=2, column=2)


    tk.mainloop()

start()
