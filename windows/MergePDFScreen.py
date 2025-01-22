import os
from PIL import Image
import customtkinter as ctk
from modules.colors.palette_color import palette_color_dark, palette_color_light
from windows.PDFview import PDFview

class MergePDF(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master, fg_color="#FFF")
        
        # Configuração da janela principal
        self.geometry("580x370")
        self.title("Juntar PDFs")
        self.overrideredirect(False)  # Permitir controle da janela
        self.resizable(False, False)  # Desabilitar redimensionamento
        self.grab_set()
        self.lift()

        # Ícone da Janela
        self.iconbitmap(False, "assets/icons/icon_16x16.ico")

        # Paleta de cores
        self.color_palette = palette_color_light

        # Frame 
        self.files_frame = ctk.CTkFrame(
            master=self,
             width=532,
             height=226,
             corner_radius=10,
             bg_color=self.color_palette["white"],
             fg_color=self.color_palette["light_gray"]
        )
        self.files_frame.place(x=24, y=24)

        self.pdf_files_label = ctk.CTkLabel(
            master=self,
            font=('Segoe UI', 12, 'normal'),
            text="Selecionar arquivo(s) PDF",
            text_color=self.color_palette["gray"],
            bg_color=self.color_palette["light_gray"]
        )
        self.pdf_files_label.place(x=230, y=152)

        # Botões
        self.cancel_button = ctk.CTkButton(
            master=self,
            width=229,
            height=32,
            corner_radius=8,
            text="Cancelar",
            font=('Segoe UI', 12, 'bold'),
            fg_color=self.color_palette["light_gray"],
            hover_color=self.color_palette["light_gray"],
            text_color=self.color_palette["gray"],
            command=self.destroy_window
        )
        self.cancel_button.place(x=31, y=314)

        self.meger_button = ctk.CTkButton(
            master=self,
            width=229,
            height=32,
            corner_radius=8,
            text="Juntar",
            font=('Segoe UI', 12, 'bold'),
            fg_color=self.color_palette["purple"],
            hover_color=self.color_palette["purple"],
            text_color=self.color_palette["white"],
            command=self.pdf_view_open
        )
        self.meger_button.place(x=310, y=314)

    def pdf_view_open(self):
        pdf_view = PDFview(self)
    
    def destroy_window(self):
        self.destroy()