import tkinter as tk

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""

expression = ""

# Creating a basic window
window = tk.Tk()
window.title("Calculator")
window.configure(bg='grey')  # Set background color to grey

# StringVar() is used to get the instance of input field
input_text = tk.StringVar()

# Creating the entry field
entry_field = tk.Entry(window, textvariable=input_text, font=('Arial', 18, 'bold'), bd=20, insertwidth=4, width=14, bg="green", fg="white", justify='right')  # Set text color to white and background color to green
entry_field.grid(columnspan=4)

# Buttons
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

# Adding buttons to the window
row = 1
for button_row in buttons:
    col = 0
    for button_text in button_row:
        tk.Button(window, text=button_text, padx=20, pady=20, font=('Arial', 18, 'bold'), fg="white", bg="grey",  # Set text color to white and background color to grey
                  command=lambda button_text=button_text: btn_click(button_text) if button_text != '=' else btn_equal() if button_text == '=' else btn_clear()).grid(row=row, column=col)
        col += 1
    row += 1

# Running the application
window.mainloop()