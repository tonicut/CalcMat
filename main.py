import tkinter as tk


def click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            resultado = str(eval(screen.get()))
            screen.set(resultado)
        except Exception as e:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)


root = tk.Tk()
root.geometry("400x600")
root.title("Calculadora")

screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="lucida 40 bold")
entry.pack(fill=tk.X, ipadx=8, pady=10, padx=10)

frame = tk.Frame(root)
frame.pack()

buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "C", "0", "=", "/"
]

i = 0
for btn in buttons:
    button = tk.Button(frame, text=btn, font="lucida 20 bold", height=2, width=4)
    button.grid(row=i // 4, column=i % 4)
    button.bind("<Button-1>", click)
    i += 1

root.mainloop()

