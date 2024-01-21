import tkinter as tk

def action_1():
    print("Botão 1 pressionado!")

root = tk.Tk()
root.title("GUI with Buttons")

button1 = tk.Button(root, text="Button1", command=action_1)
button1.pack()

root.mainloop()