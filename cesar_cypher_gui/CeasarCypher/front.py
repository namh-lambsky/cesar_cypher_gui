import tkinter as tk
import back

window = tk.Tk()
text = tk.StringVar(window)
step = tk.StringVar(window)

window.config(width=700, height=350)
window.resizable(False, False)
window.title("Cifrado y Descifrado de Cesar en python")

def isNum():
    if str_jump.get().isdigit() :
        return True
    else:
        return False


def capture(*args):
    if len(str_to_encrypt.get())>=1 and len(str_jump.get())>=1:
        bt_encrypt["state"] = "normal"
        bt_decrypt["state"] = "normal"
    else:
        bt_encrypt["state"] = "disabled"
        bt_decrypt["state"] = "disabled"

def encrypt():
    lbl_result["text"]+= back.encode(str_to_encrypt.get(),int(str_jump))

def decrypt():
    lbl_result["text"]+= back.decode(str_to_encrypt.get(),int(str_jump))


lb1 = tk.Label(
    window, text="Por favor ingrese la frase a tratar", font=("Consolas", 14)
).place(x=20, y=20)

str_to_encrypt = tk.Entry(window, font=("Consolas", 16), textvariable=text)
str_to_encrypt.place(x=20, y=50)

lb2 = tk.Label(
    window,
    text="Por favor ingrese la cantidad de espacios a saltar en el abecedario",
    font=("Consolas", 14),
).place(x=20, y=80)

str_jump = tk.Entry(window, font=("Consolas", 16), validate="all",validatecommand=isNum(),textvariable=step)
str_jump.place(x=20, y=110)

bt_encrypt = tk.Button(text="Encriptar", font=("Consolas", 16),command= encrypt,state="disabled")
bt_encrypt.place(x=180, y=150)

bt_decrypt = tk.Button(text="Desencriptar", font=("Consolas", 16),state="disabled")
bt_decrypt.place(x=360, y=150)

lbl_result=tk.Label(text="The result of the command is:",font=("Consolas", 14))
lbl_result.place(x=20,y=220)


text.trace("w", capture)
step.trace("w", capture)


window.mainloop()
