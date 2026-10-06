import customtkinter as ctk
import math

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.geometry("400x680")
app.title("Calculator")
app.resizable(False, False)


expression = ""
display = ctk.CTkEntry(app, width=380, height=50, font=("Arial", 24),justify="right")
display.pack(fill="x", padx=(10, 10), pady=(20, 20))

def press(key):
    global expression
    if key == "=":
        try:
            allowed_functions = {
                "sin": math.sin,
                "cos": math.cos,
                "tan": math.tan,
                "log": math.log10,
                "sqrt": math.sqrt,
            }
            expression = str(
                eval(
                    expression.replace("^", "**"),
                    {"__builtins__": {}},
                    allowed_functions,
                )
            )
        except Exception as e:
            expression = "Error"
    elif key == "C":
        expression = ""
    elif key in {"sin", "cos", "tan", "log", "sqrt"}:
        expression += f"{key}("
    else:
        expression += str(key)
    display.delete(0, ctk.END)
    display.insert(0, expression)
    
def handle_keypress(event):
    key = event.char
    if key in "0123456789+-*/=":
        press(key)
    elif key.lower() == "c":
        press("C")

app.bind("<KeyPress>", handle_keypress)
app.bind("<Return>", lambda event: press("="))
# keyboard bindings for enter on the numpad
app.bind("<KP_Enter>", lambda event: press("="))

app.bind("<BackSpace>", lambda event: press("C"))
app.bind("<Escape>", lambda event: press("C"))
app.bind("<Delete>", lambda event: press("C"))


frame = ctk.CTkFrame(app,fg_color="transparent")
frame.pack(expand=True,fill="both", padx=(10, 10), pady=(0,10))


buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],       
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"],
    ["sin", "cos", "tan", "log"],
    ["(", ")", "^", "sqrt"],
]

for i, row in enumerate(buttons):
    for j, button in enumerate(row):
        button_options = {}
        if button in "+-*/":
            button_options = {"fg_color": "#FF9500", "hover_color": "#FFB84D"}
        elif button == "C":
            button_options = {"fg_color": "#FF3B30", "hover_color": "#FF6B61"}
        elif button == "=":
            button_options = {"fg_color": "#34C759", "hover_color": "#5CD65C"}

        ctk.CTkButton(
            frame,
            text=button,
            width=80,
            height=80,
            font=("Arial", 24),
            command=lambda key=button: press(key),
            **button_options,
        ).grid(row=i, column=j, padx=(5, 5), pady=(5, 5))
        
app.mainloop()