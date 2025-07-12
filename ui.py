import tkinter as tk
from logic import load_choices, random_choice

def choose():
    result.set(random_choice(choices))

choices = load_choices("data/choices.txt")

root = tk.Tk()
root.title("ตัวสุ่มของคุณ")
root.geometry("300x200")

result = tk.StringVar()
label = tk.Label(root, textvariable=result, font=("Arial", 20))
label.pack(pady=20)

btn = tk.Button(root, text="สุ่ม!", command=choose)
btn.pack()

root.mainloop()
