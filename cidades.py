import tkinter as tk
from tkinter import messagebox


def inserir_dados():
    
    messagebox.showinfo("Inserir", "Dados inseridos com sucesso!")

def alterar_dados():
  
    messagebox.showinfo("Alterar", "Dados alterados com sucesso!")

def excluir_dados():
  
    messagebox.showinfo("Excluir", "Dados excluídos com sucesso!")

def buscar_cidade():
    id_cidade = entry_idcidade.get()
    
    encontrado = False 

    if encontrado:
       
        pass
    else:
        messagebox.showwarning("Buscar", f"Cidade com ID {id_cidade} não encontrada.")
     
        entry_nome.delete(0, tk.END)
        entry_uf.delete(0, tk.END)


root = tk.Tk()
root.title("Formulário de Cidade")
root.geometry("300x250")


lbl_title = tk.Label(root, text="Informe os dados", font=("Helvetica", 14))
lbl_title.pack(pady=10)


frame_idcidade = tk.Frame(root)
frame_idcidade.pack(pady=5)

lbl_idcidade = tk.Label(frame_idcidade, text="Id da Cidade:")
lbl_idcidade.pack(side=tk.LEFT)

entry_idcidade = tk.Entry(frame_idcidade)
entry_idcidade.pack(side=tk.LEFT, padx=5)

btn_buscar = tk.Button(frame_idcidade, text="Buscar", command=buscar_cidade)
btn_buscar.pack(side=tk.LEFT)


lbl_nome = tk.Label(root, text="Nome:")
lbl_nome.pack()
entry_nome = tk.Entry(root)
entry_nome.pack()


lbl_uf = tk.Label(root, text="UF:")
lbl_uf.pack()
entry_uf = tk.Entry(root)
entry_uf.pack()


btn_inserir = tk.Button(root, text="Inserir", command=inserir_dados)
btn_inserir.pack(pady=5)

btn_alterar = tk.Button(root, text="Alterar", command=alterar_dados)
btn_alterar.pack(pady=5)

btn_excluir = tk.Button(root, text="Excluir", command=excluir_dados)
btn_excluir.pack(pady=5)


root.mainloop()
