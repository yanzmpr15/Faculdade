import tkinter as tk
from tkinter import Canvas, messagebox
from PIL import Image, ImageDraw
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas as pdf_canvas

class telaLogin:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.master.geometry("300x200")
        
        self.label_username = tk.Label(master, text="Usuário:")
        self.label_username.pack()
        self.entry_username = tk.Entry(master)
        self.entry_username.pack()
        
        self.label_password = tk.Label(master, text="Senha:")
        self.label_password.pack()
        self.entry_password = tk.Entry(master, show="*")
        self.entry_password.pack()
        
        self.button_login = tk.Button(master, text="Login", command=self.login)
        self.button_login.pack()

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        # Validação das credenciais.
        # Usuário = "usuario" e a senha = "senha".
        if username == "usuario" and password == "senha":
            self.master.destroy()
            root = tk.Tk()
            app = assinaturaEletronica(root)
            root.mainloop()
        else:
            messagebox.showerror("Login falhou", "Usuário ou senha inválidos.")

class assinaturaEletronica:
    def __init__(self, master):
        self.master = master
        self.master.title("Assinatura Eletrônica")
        self.canvas = Canvas(master, width=500, height=250, bg="white")
        self.canvas.pack()

        self.canvas.bind("<B1-Motion>", self.desenhar)
        self.canvas.bind("<ButtonRelease-1>", self.salvar)

        self.botao_limpar = tk.Button(master, text="Limpar Assinatura", command=self.limpar_assinatura)
        self.botao_limpar.pack()

        self.botao_salvar = tk.Button(master, text="Salvar Assinatura", command=self.salvar_assinatura)
        self.botao_salvar.pack()

        self.imagem = Image.new("RGB", (400, 200), "white")
        self.draw = ImageDraw.Draw(self.imagem)
        self.last_x = None
        self.last_y = None

    def desenhar(self, event):
        x, y = event.x, event.y
        if self.last_x is not None and self.last_y is not None:
            self.canvas.create_line(self.last_x, self.last_y, x, y, fill="black", width=1)
            self.draw.line([self.last_x, self.last_y, x, y], fill="black", width=1)
        self.last_x = x
        self.last_y = y

    def salvar(self, event):
        self.last_x = None
        self.last_y = None

    def limpar_assinatura(self):
        self.canvas.delete("all")
        self.imagem = Image.new("RGB", (400, 200), "white")
        self.draw = ImageDraw.Draw(self.imagem)

    def salvar_assinatura(self):
        nome_arquivo = "assinatura_eletronica.pdf"
        largura, altura = letter
        pdf = pdf_canvas.Canvas(nome_arquivo, pagesize=letter)
        self.imagem.save("assinatura_eletronica.png")  # Salvando a imagem da assinatura
        pdf.drawImage("assinatura_eletronica.png", 100, altura - 300, width=200, height=100)
        pdf.save()
        messagebox.showinfo("Assinatura Salva", f"A assinatura foi salva como '{nome_arquivo}'.")

def main():
    root = tk.Tk()
    tela_login = telaLogin(root)
    root.mainloop()

if __name__ == "__main__":
    main()
