import tkinter as tk

def click(event):
    global expression
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(expression)
            display.set(result)
            expression = str(result)
        except Exception as e:
            display.set("Error")
            expression = ""
    elif text == "C":
        expression = ""
        display.set("")
    else:
        expression += text
        display.set(expression)

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.configure(bg="lightgray")

expression = ""
display = tk.StringVar()

# Entry for display
entry = tk.Entry(root, textvar=display, font="Arial 20", justify='right')
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn_text in row:
        button = tk.Button(frame, text=btn_text, font="Arial 18", relief="raised")
        button.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        button.bind("<Button-1>", click)

root.mainloop()
