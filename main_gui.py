import tkinter as tk
from tkinter import messagebox, simpledialog
from controller.login_controller import login, sessao
from model.usuario_model import criar_usuario, listar_usuarios, deletar_usuario

# --- Funções do Controlador/Modelo (Adaptadas para GUI) ---

def criar_usuario_gui():
    """Abre uma janela para criar um novo usuário."""
    janela_criar = tk.Toplevel()
    janela_criar.title("Criar Usuário")
    janela_criar.geometry("400x300")

    tk.Label(janela_criar, text="Nome:").pack(pady=5)
    entry_nome = tk.Entry(janela_criar)
    entry_nome.pack(pady=5)

    tk.Label(janela_criar, text="Email:").pack(pady=5)
    entry_email = tk.Entry(janela_criar)
    entry_email.pack(pady=5)

    tk.Label(janela_criar, text="Senha:").pack(pady=5)
    entry_senha = tk.Entry(janela_criar, show="*") # Máscara para senha
    entry_senha.pack(pady=5)
    
     
    def salvar_usuario(event=None):
        nome = entry_nome.get()
        email = entry_email.get()
        senha = entry_senha.get()
        if not nome or not email or not senha:
            messagebox.showwarning("Atenção", "Todos os campos são obrigatórios!")
            return
        try:
            criar_usuario(nome, email, senha)
            messagebox.showinfo("Sucesso", "Usuário criado com sucesso!")
            janela_criar.destroy() # Fecha a janela após criar
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao criar usuário: {e}")
        
    tk.Button(janela_criar, text="Salvar", command=salvar_usuario).pack(pady=10)
    # Bind do Enter para a janela
    janela_criar.bind('<Return>', salvar_usuario)
  

def listar_usuarios_gui():
    """Exibe uma lista de usuários em uma nova janela."""
    janela_listar = tk.Toplevel()
    janela_listar.title("Lista de Usuários")
    janela_listar.geometry("400x300")

    try:
        usuarios = listar_usuarios()
        if not usuarios:
            tk.Label(janela_listar, text="Nenhum usuário cadastrado.").pack(pady=20)
            return

        for u in usuarios:
            tk.Label(janela_listar, text=f"ID: {u['id']} | Nome: {u['nome']} | Email: {u['email']}").pack(anchor="w", padx=10)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao listar usuários: {e}")

def deletar_usuario_gui():
    """Solicita o ID e deleta um usuário."""
    id_usuario = simpledialog.askstring("Deletar Usuário", "Digite o ID do usuário a deletar:")
    if id_usuario:
        try:
            deletar_usuario(id_usuario)
            messagebox.showinfo("Sucesso", "Usuário deletado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao deletar usuário: {e}")

# --- Janela de Login ---

class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("300x200")
        self.centralizar_janela()

        tk.Label(self, text="Email:").pack(pady=5)
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)

        tk.Label(self, text="Senha:").pack(pady=5)
        self.senha_entry = tk.Entry(self, show="*") # Máscara para senha
        self.senha_entry.pack(pady=5)

        tk.Button(self, text="Login", command=self.tentar_login).pack(pady=10)
        # Atalho de teclado: Enter
        self.bind('<Return>', self._atalho_enter)
    
    def _atalho_enter(self, event):
        self.tentar_login()
 
    def centralizar_janela(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')

    def tentar_login(self):
        email = self.email_entry.get()
        senha = self.senha_entry.get()
        sucesso, mensagem = login(email, senha)
        messagebox.showinfo("Login", mensagem)
        if sucesso:
            self.destroy() # Fecha a janela de login
            root_menu = MenuWindow() # Abre a janela do menu
            root_menu.mainloop()
        else:
            self.email_entry.delete(0, tk.END)
            self.senha_entry.delete(0, tk.END)

# --- Janela do Menu Principal ---

class MenuWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Menu Principal")
        self.geometry("400x300")
        self.centralizar_janela()

        tk.Label(self, text="Bem-vindo ao sistema!", font=("Arial", 16)).pack(pady=20)

        tk.Button(self, text="Criar Usuário", command=criar_usuario_gui, width=20).pack(pady=5)
        tk.Button(self, text="Listar Usuários", command=listar_usuarios_gui, width=20).pack(pady=5)
        tk.Button(self, text="Deletar Usuário", command=deletar_usuario_gui, width=20).pack(pady=5)
        tk.Button(self, text="Logout", command=self.fazer_logout, width=20).pack(pady=5)
        tk.Button(self, text="Sair", command=self.sair_aplicacao, width=20).pack(pady=5)

    def centralizar_janela(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')

    def fazer_logout(self):
        sessao.clear()
        messagebox.showinfo("Logout", "Logout realizado com sucesso!")
        self.destroy() # Fecha a janela do menu
        LoginWindow().mainloop() # Abre a janela de login novamente

    def sair_aplicacao(self):
        self.destroy() # Fecha a janela do menu e encerra a aplicação

# --- Iniciar a Aplicação ---

if __name__ == "__main__":
    app = LoginWindow()
    app.mainloop()