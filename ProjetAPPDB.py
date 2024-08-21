import tkinter as tk

def usuarios_action():
    print("Usuários")

def cidades_action():
    print("Cidades")

def clientes_action():
    print("Clientes")

def fechar_action():
    root.destroy()


root = tk.Tk()
root.title("Menu Principal")


root.geometry("300x200")


frame = tk.Frame(root)
frame.pack(pady=20)


btn_usuarios = tk.Button(frame, text="Usuários", command=usuarios_action, borderwidth=2, relief="solid")
btn_usuarios.grid(row=0, column=0, padx=10, pady=5)

btn_cidades = tk.Button(frame, text="Cidades", command=cidades_action, borderwidth=2, relief="solid")
btn_cidades.grid(row=1, column=0, padx=10, pady=5)

btn_clientes = tk.Button(frame, text="Clientes", command=clientes_action, borderwidth=2, relief="solid")
btn_clientes.grid(row=2, column=0, padx=10, pady=5)

btn_fechar = tk.Button(frame, text="Fechar", command=fechar_action, borderwidth=2, relief="solid")
btn_fechar.grid(row=3, column=0, padx=10, pady=5)


root.mainloop()
