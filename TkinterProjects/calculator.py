import tkinter as tk

root = tk.Tk()
root.title("CALCULATOR")
root.geometry("300x400")

expression = ""
input_text = tk.StringVar()

bg_color = "#2d2d2d"
btn_color = '#f39c12'
text_color = '#ffffff'
btn_hover_color = '#e67e22'

input_frame = tk.Frame(root, width=312, height=50, bd=0, highlightbackground=bg_color, highlightcolor=bg_color, highlightthickness=2)
input_frame.pack(side=tk.TOP)

input_field = tk.Entry(input_frame, font=('arial', 20, 'bold'), textvariable=input_text, width=50, bg="#1c1c1c", fg=text_color, bd=0, justify=tk.RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10) 

def btn_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_equal():
    global expression
    try:
        result = str(eval(expression)) 
        input_text.set(result)
        expression = result
    except Exception as e:
        input_text.set("Error")
        expression = ""

btns_frame = tk.Frame(root, width=312, height=272.5, bg=bg_color)
btns_frame.pack()

def create_btn(text, row, column, columnspan=1, command=None, width=10):
    btn = tk.Button(btns_frame, text=text, fg=text_color, width=width, height=3, bd=0, bg=btn_color, activebackground=btn_hover_color, cursor="hand2", command=command)
    btn.grid( row=row, column=column, columnspan=columnspan, padx=1, pady=1 )
    return btn

clear = create_btn("C", 0, 0, columnspan=3, command=btn_clear, width=32)
divide = create_btn("/", 0, 3, command=lambda: btn_click("/"))

seven = create_btn("7", 1, 0, command=lambda: btn_click("7"))
eight = create_btn("8", 1, 1, command=lambda: btn_click("8"))
nine = create_btn("9", 1, 2, command=lambda: btn_click("9"))
multiply = create_btn("*", 1, 3, command=lambda: btn_click("*"))

four = create_btn("4", 2, 0, command=lambda: btn_click("4"))
five = create_btn("5", 2, 1, command=lambda: btn_click("5"))
six = create_btn("6", 2, 2, command=lambda: btn_click("6"))
minus = create_btn("-", 2, 3, command=lambda: btn_click("-"))

one = create_btn("1", 3, 0, command=lambda: btn_click("1"))
two = create_btn("2", 3, 1, command=lambda: btn_click("2"))
three = create_btn("3", 3, 2, command=lambda: btn_click("3"))
plus = create_btn("+", 3, 3, command=lambda: btn_click("+"))

zero = create_btn("0", 4, 0, columnspan=2, command=lambda: btn_click("0"), width=21)
point = create_btn(".", 4, 2, command=lambda: btn_click("."))
equals = create_btn("=", 4, 3, command=lambda: btn_equal())

root.mainloop()