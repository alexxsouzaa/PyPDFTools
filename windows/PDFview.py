import os
from PIL import Image
import customtkinter as ctk
from modules.colors.palette_color import palette_color_dark, palette_color_light

class PDFview(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master, fg_color="#F8F8F8")
        
        # Configuração da janela principal
        self.geometry("600x600+400+50")
        self.title("PDF View")
        self.overrideredirect(False)  # Permitir controle da janela
        self.resizable(False, False)  # Desabilitar redimensionamento
        self.grab_set()
        self.lift()

        # Ícone da Janela
        self.iconbitmap(False, "assets/icons/icon_16x16.ico")

        # Paleta de cores
        self.color_palette = palette_color_light

        # Frame de visualização do PDF
        self.pdf_frame = ctk.CTkFrame(
            master=self,
            width=568,
            height=504,
            fg_color=self.color_palette["white"],
            corner_radius=10,
            border_width=1.2,
            border_color="#DEDEDE"
        )
        self.pdf_frame.place(x=16, y=16)

        # Botões
        self.cancel_button = ctk.CTkButton(
            master=self,
            width=229,
            height=32,
            corner_radius=20,
            text="Cancelar",
            font=('Segoe UI', 12, 'bold'),
            fg_color=self.color_palette["light_gray"],
            hover_color=self.color_palette["light_gray"],
            text_color=self.color_palette["gray"]
        )
        self.cancel_button.place(x=51, y=544)

        self.save_button = ctk.CTkButton(
            master=self,
            width=229,
            height=32,
            corner_radius=20,
            text="Salvar",
            font=('Segoe UI', 12, 'bold'),
            fg_color=self.color_palette["purple"],
            hover_color=self.color_palette["purple"],
            text_color=self.color_palette["white"]
        )
        self.save_button.place(x=320, y=544)
