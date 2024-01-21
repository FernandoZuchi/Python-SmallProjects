import tkinter as tk

def action_1():
    print("Botão 1 pressionado!")

def action_2():
    print("Botão 2 pressionado!")

def action_3():
    print("Botão 3 pressionado!")

root = tk.Tk()
root.title("GUI com botões")

button1 = tk.Button(root, text="Botão 1", command=action_1)
button1.pack()

button2 = tk.Button(root, text="Botão 2", command=action_2)
button2.pack()

button3 = tk.Button(root, text="Botão 3", command=action_3)
button3.pack()

root.mainloop()