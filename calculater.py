import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(screen.get())
            screen.set(result)
        except:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="Arial 20")
entry.pack(fill=tk.X, padx=10, pady=10)

buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+",
    "C"
]

frame = tk.Frame(root)
frame.pack()

for btn in buttons:
    b = tk.Button(frame, text=btn, font="Arial 15", width=5, height=2)
    b.pack(side=tk.LEFT, padx=2, pady=2)
    b.bind("<Button-1>", click)

root.mainloop()
