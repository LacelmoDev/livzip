import customtkinter as ctk
from tkinter import filedialog, messagebox
import zipfile
import os

# Tenta importar rarfile para descompactação
try:
    import rarfile
except ImportError:
    rarfile = None

class LivZipApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurações da Janela (Baseado no seu Nome do Programa)
        self.title("LIVZIP - Gerenciador de Arquivos")
        self.geometry("500x700")
        ctk.set_appearance_mode("dark")
        
        self.arquivo_selecionado = None

        # --- Elementos da Interface (Seu Mockup) ---
        
        # Título Superior
        self.titulo = ctk.CTkLabel(self, text="LIVZIP", font=("Arial", 28, "bold"))
        self.titulo.pack(pady=20, anchor="w")

        # Área Central (Onde seria o Arraste)
        # No Tkinter padrão, usamos um botão de clique para simular a seleção
        self.frame_central = ctk.CTkFrame(self, width=400, height=250, corner_radius=20, border_width=2)
        self.frame_central.pack(pady=10, padx=20, fill="both")
        self.frame_central.pack_propagate(False)

        self.btn_selecionar = ctk.CTkButton(self.frame_central, text="+", font=("Arial", 40), 
                                           width=80, height=80, corner_radius=40,
                                           command=self.selecionar_arquivo)
        self.btn_selecionar.place(relx=0.5, rely=0.4, anchor="center")

        self.lbl_status = ctk.CTkLabel(self.frame_central, text="CLIQUE NO + PARA SELECIONAR\nOU ARRASTE (SIMULADO)", font=("Arial", 12))
        self.lbl_status.place(relx=0.5, rely=0.7, anchor="center")

        # Botões Inferiores (Com e Des)
        self.frame_botoes = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_botoes.pack(pady=20)

        self.btn_compactar = ctk.CTkButton(self.frame_botoes, text="COM", width=100, 
                                          command=self.acao_compactar, state="disabled")
        self.btn_compactar.grid(row=0, column=0, padx=10)

        self.btn_descompactar = ctk.CTkButton(self.frame_botoes, text="DES", width=100, 
                                             command=self.acao_descompactar, state="disabled")
        self.btn_descompactar.grid(row=0, column=1, padx=10)

        # Quadro de Histórico (Seu Retângulo de Histórico)
        self.lbl_hist = ctk.CTkLabel(self, text="Histórico de Atividades:")
        self.lbl_hist.pack(anchor="w", padx=50)
        
        self.historico = ctk.CTkTextbox(self, width=400, height=150, corner_radius=10)
        self.historico.pack(pady=10, padx=20)
        self.log("Sistema LIVZIP iniciado com sucesso.")

    # --- Lógica de Funcionamento ---

    def log(self, mensagem):
        self.historico.insert("end", f"> {mensagem}\n")
        self.historico.see("end")

    def selecionar_arquivo(self):
        caminho = filedialog.askopenfilename()
        if caminho:
            self.arquivo_selecionado = caminho
            nome = os.path.basename(caminho)
            self.lbl_status.configure(text=f"ARQUIVO: {nome}", text_color="#3b8ed0")
            self.log(f"Selecionado: {nome}")
            
            # Habilita botões baseado na extensão (Sua Lógica!)
            if nome.lower().endswith(('.zip', '.rar')):
                self.btn_descompactar.configure(state="normal")
                self.btn_compactar.configure(state="disabled")
            else:
                self.btn_compactar.configure(state="normal")
                self.btn_descompactar.configure(state="disabled")

    def acao_compactar(self):
        nome_final = filedialog.asksaveasfilename(defaultextension=".zip", filetypes=[("Arquivo ZIP", "*.zip")])
        if nome_final:
            try:
                with zipfile.ZipFile(nome_final, 'w', zipfile.ZIP_DEFLATED) as zipf:
                    zipf.write(self.arquivo_selecionado, arcname=os.path.basename(self.arquivo_selecionado))
                self.log(f"SUCESSO: {os.path.basename(nome_final)} criado.")
                messagebox.showinfo("LIVZIP", "Compactação concluída!")
            except Exception as e:
                self.log(f"ERRO: {e}")

    def acao_descompactar(self):
        pasta_destino = filedialog.askdirectory(title="Selecione onde extrair")
        if pasta_destino:
            try:
                ext = self.arquivo_selecionado.lower()
                if ext.endswith('.zip'):
                    with zipfile.ZipFile(nome_final, 'w', zipfile.ZIP_DEFLATED) as zipf:
                        if os.path.isdir(self.arquivo_selecionado):
        # Se for uma PASTA, precisamos "caminhar" por ela
                            for raiz, diretorios, arquivos in os.walk(self.arquivo_selecionado):
                                for arquivo in arquivos:
                                    caminho_completo = os.path.join(raiz, arquivo)
                # Calcula o caminho relativo para não criar pastas infinitas dentro do zip
                                    caminho_no_zip = os.path.relpath(caminho_completo, os.path.dirname(self.arquivo_selecionado))
                                    zipf.write(caminho_completo, arcname=caminho_no_zip)
                else:
        # Se for apenas um ARQUIVO solo (lógica antiga)
                    zipf.write(self.arquivo_selecionado, arcname=os.path.basename(self.arquivo_selecionado))
                    self.log(f"SUCESSO: Extraído em {pasta_destino}")
                    messagebox.showinfo("LIVZIP", "Extração concluída!")
            except Exception as e:
                self.log(f"ERRO: {e}")

if __name__ == "__main__":
    app = LivZipApp()
    app.mainloop()