from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Usuarios import *
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class Application:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Formulário de Usuários")

        # Frame para o formulário
        self.janela1 = Frame(master)
        self.janela1.pack(padx=10, pady=10)

        # Título
        self.msg1 = Label(self.janela1, text="Informe os dados:")
        self.msg1["font"] = ("Verdana", "14", "bold")
        self.msg1.pack()

        # Frame para a busca
        self.janela2 = Frame(master)
        self.janela2["padx"] = 20
        self.janela2.pack()

        self.idusuario_label = Label(self.janela2, text="Id usuário:")
        self.idusuario_label.pack(side="left")
        self.idusuario = Entry(self.janela2, width=20)
        self.idusuario.pack(side="left")

        self.busca = Button(self.janela2, text="Buscar", command=self.buscarUsuario)
        self.busca.pack()

        # Frames para os campos de dados
        self.janela3 = Frame(master)
        self.janela3["padx"] = 20
        self.janela3.pack()

        self.nome_label = Label(self.janela3, text="Nome:")
        self.nome_label.pack(side="left")
        self.nome = Entry(self.janela3, width=30)
        self.nome.pack(side="left")

        self.janela5 = Frame(master)
        self.janela5["padx"] = 20
        self.janela5.pack(pady=5)

        self.telefone_label = Label(self.janela5, text="Telefone:")
        self.telefone_label.pack(side="left")
        self.telefone = Entry(self.janela5, width=28)
        self.telefone.pack(side="left")

        self.janela6 = Frame(master)
        self.janela6["padx"] = 20
        self.janela6.pack()

        self.email_label = Label(self.janela6, text="E-mail:")
        self.email_label.pack(side="left")
        self.email = Entry(self.janela6, width=30)
        self.email.pack(side="left")

        self.janela7 = Frame(master)
        self.janela7["padx"] = 20
        self.janela7.pack(pady=5)

        self.usuario_label = Label(self.janela7, text="Usuário:")
        self.usuario_label.pack(side="left")
        self.usuario = Entry(self.janela7, width=29)
        self.usuario.pack(side="left")

        self.janela4 = Frame(master)
        self.janela4["padx"] = 20
        self.janela4.pack(pady=5)

        self.senha_label = Label(self.janela4, text="Senha:")
        self.senha_label.pack(side="left")
        self.senha = Entry(self.janela4, width=30, show="*")
        self.senha.pack(side="left")

        # Frame para os botões
        self.janela10 = Frame(master)
        self.janela10["padx"] = 20
        self.janela10.pack()

        self.autentic = Label(self.janela10, text="")
        self.autentic["font"] = ("Verdana", "10", "italic", "bold")
        self.autentic.pack()

        self.janela11 = Frame(master)
        self.janela11["padx"] = 20
        self.janela11.pack()

        self.botao = Button(self.janela11, width=10, text="Inserir", command=self.inserirUsuario)
        self.botao.pack(side="left")

        self.botao2 = Button(self.janela11, width=10, text="Alterar", command=self.alterarUsuario)
        self.botao2.pack(side="left")

        self.botao3 = Button(self.janela11, width=10, text="Excluir", command=self.excluirUsuario)
        self.botao3.pack(side="left")

        # Frame para a tabela
        self.janela12 = Frame(master)
        self.janela12["padx"] = 20
        self.janela12.pack(pady=10)

        self.tree = ttk.Treeview(self.janela12, columns=("ID", "Nome", "Telefone", "E-mail", "Usuário", "Senha"),
                                 show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Telefone", text="Telefone")
        self.tree.heading("E-mail", text="E-mail")
        self.tree.heading("Usuário", text="Usuário")
        self.tree.heading("Senha", text="Senha")
        self.tree.pack()

        # Evento de clique na linha da tabela
        self.tree.bind("<ButtonRelease-1>", self.selecionar_linha)

        # Atualiza a tabela quando a aplicação é carregada
        self.atualizarTabela()

        self.janela13 = Frame(master)
        self.janela13["padx"] = 20
        self.janela13.pack(pady=10)

        self.botao4 = Button(self.janela13, width=10, text="Voltar", command=self.voltarmenu)
        self.botao4.pack(side="left")

        # Botão para exportar para PDF
        self.botao_exportar_pdf = Button(self.janela13, width=20, text="Exportar para PDF", command=self.exportarParaPDF)
        self.botao_exportar_pdf.pack(side="left")

    def atualizarTabela(self):
        user = Usuarios()
        usuarios = user.selectAllUsers()
        self.tree.delete(*self.tree.get_children())
        for u in usuarios:
            self.tree.insert("", "end", values=(u[0], u[1], u[2], u[3], u[4], u[5]))

    def selecionar_linha(self, event):
        """Preenche os campos de entrada com os dados da linha selecionada na tabela."""
        selected_item = self.tree.selection()  # Captura o item selecionado
        if selected_item:
            item = self.tree.item(selected_item[0])  # Obtém o primeiro item selecionado
            valores = item['values']  # Obtém os valores da linha selecionada

            if valores:
                self.idusuario.delete(0, END)
                self.idusuario.insert(END, valores[0])
                self.nome.delete(0, END)
                self.nome.insert(END, valores[1])
                self.telefone.delete(0, END)
                self.telefone.insert(END, valores[2])
                self.email.delete(0, END)
                self.email.insert(END, valores[3])
                self.usuario.delete(0, END)
                self.usuario.insert(END, valores[4])
                self.senha.delete(0, END)
                self.senha.insert(END, valores[5])

    def buscarUsuario(self):
        user = Usuarios()
        idusuario = self.idusuario.get()
        result = user.selectUser(idusuario)
        if result:
            self.autentic["text"] = "Usuário encontrado!"
        else:
            self.autentic["text"] = "Usuário não encontrado!"
        self.atualizarTabela()

    def inserirUsuario(self):
        user = Usuarios()
        user.nome = self.nome.get()
        user.telefone = self.telefone.get()
        user.email = self.email.get()
        user.usuario = self.usuario.get()
        user.senha = self.senha.get()
        self.autentic["text"] = user.insertUser()
        self.limparCampos()
        self.atualizarTabela()
        messagebox.showinfo("Inserir", "Usuário inserido com sucesso!")

    def alterarUsuario(self):
        user = Usuarios()
        user.idusuario = self.idusuario.get()
        user.nome = self.nome.get()
        user.telefone = self.telefone.get()
        user.email = self.email.get()
        user.usuario = self.usuario.get()
        user.senha = self.senha.get()
        user.updateUser()  # Atualiza o usuário
        messagebox.showinfo("Alterar", "Usuário alterado com sucesso!")
        self.limparCampos()
        self.atualizarTabela()

    def excluirUsuario(self):
        user = Usuarios()
        user.idusuario = self.idusuario.get()
        user.deleteUser()  # Exclui o usuário
        messagebox.showinfo("Excluir", "Usuário excluído com sucesso!")
        self.limparCampos()
        self.atualizarTabela()

    def limparCampos(self):
        self.idusuario.delete(0, END)
        self.nome.delete(0, END)
        self.telefone.delete(0, END)
        self.email.delete(0, END)
        self.usuario.delete(0, END)
        self.senha.delete(0, END)

    def voltarmenu(self):
        self.master.destroy()

    def exportarParaPDF(self):
        # Cria o arquivo PDF
        pdf = canvas.Canvas("usuarios.pdf", pagesize=letter)
        pdf.setTitle("Lista de Usuários")

        # Adiciona título
        pdf.drawString(100, 750, "Lista de Usuários")

        # Adiciona cabeçalhos da tabela
        pdf.drawString(50, 720, "ID")
        pdf.drawString(100, 720, "Nome")
        pdf.drawString(200, 720, "Telefone")
        pdf.drawString(300, 720, "E-mail")
        pdf.drawString(400, 720, "Usuário")
        pdf.drawString(500, 720, "Senha")

        # Adiciona os dados
        y = 700
        for item in self.tree.get_children():
            valores = self.tree.item(item, 'values')
            pdf.drawString(50, y, str(valores[0]))
            pdf.drawString(100, y, valores[1])
            pdf.drawString(200, y, valores[2])
            pdf.drawString(300, y, valores[3])
            pdf.drawString(400, y, valores[4])
            pdf.drawString(500, y, valores[5])
            y -= 20

        # Salva o PDF
        pdf.save()

        # Mensagem de sucesso
        messagebox.showinfo("Exportar para PDF", "Dados exportados com sucesso para o arquivo usuarios.pdf")

# Inicializa a aplicação
if __name__ == "__main__":
    root = Tk()
    app = Application(master=root)
    root.mainloop()