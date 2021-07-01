import tkinter as tk

main = tk.Tk()
main.title('CALCULATOR')
main.config(bg='#cef9ff')
main.iconbitmap('calculator.ico')
main.geometry('250x200')
value1 = tk.IntVar()
value2 = tk.IntVar()
total_value = tk.IntVar()


# function to add two numbers
def display_value_1():
    integer_value1 = value1.get()
    integer_value2 = value2.get()
    result1 = integer_value1 + integer_value2
    value1.set('0')
    value2.set('0')
    total_value.set(result1)


# function to subtract two numbers
def display_value_2():
    integer_value1 = value1.get()
    integer_value2 = value2.get()
    result2 = integer_value1 - integer_value2
    value1.set('0')
    value2.set('0')
    total_value.set(result2)


# function to multiply two numbers
def display_value_3():
    integer_value1 = value1.get()
    integer_value2 = value2.get()
    result3 = integer_value1 * integer_value2
    value1.set('0')
    value2.set('0')
    total_value.set(result3)


# function to divide two numbers
def display_value_4():
    integer_value1 = value1.get()
    integer_value2 = value2.get()
    result4 = integer_value1 / integer_value2
    value1.set('0')
    value2.set('0')
    total_value.set(result4)


label_1 = tk.Label(main, text='NUMBER 1:', bg='#cef9ff', font=('Arial', 10)).grid(row=0, column=0, padx=5, pady=5)
label_2 = tk.Label(main, text='NUMBER 2:', bg='#cef9ff', font=('Arial', 10)).grid(row=1, column=0, padx=5, pady=5)
label_3 = tk.Label(main, text='RESULT:', bg='#cef9ff', font=('Arial', 10)).grid(row=8, column=0, padx=5, pady=5)

entry_1 = tk.Entry(main, textvariable=value1, font=('Arial', 10)).grid(row=0, column=1, padx=5)
entry_2 = tk.Entry(main, textvariable=value2, font=('Arial', 10)).grid(row=1, column=1, padx=5)

add_button = tk.Button(main, text='ADD', command=display_value_1, width='8', font=('Arial', 10), bg='#c6d1d8').grid(
    row=2,
    column=0,
    padx=10)
sub_button = tk.Button(main, text='SUBTRACT', command=display_value_2, width='9', font=('Arial', 10),
                       bg='#c6d1d8').grid(
    row=2, column=1, padx=6)

multi_button = tk.Button(main, text='MULTIPLY', command=display_value_3, width='8', font=('Arial', 10),
                         bg='#c6d1d8').grid(
    row=3, column=0, padx=6, pady=6)

divi_button = tk.Button(main, text='DIVIDE', command=display_value_4, width='9', font=('Arial', 10), bg='#c6d1d8').grid(
    row=3, column=1, padx=6, pady=6)

entry_3 = tk.Entry(main, textvariable=total_value, font=('Arial', 10)).grid(row=8, column=1, padx=5, pady=5)

main.mainloop()
