import customtkinter as ctk
import os
from PIL import Image
from modules.colors.palette_color import palette_color_dark, palette_color_light

class MergePDF(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master, fg_color="#FFF")
        
        # Configuração da janela principal
        self.geometry("580x480")
        self.title("Juntar PDFs")
        self.overrideredirect(False)  # Permitir controle da janela
        self.resizable(False, False)  # Desabilitar redimensionamento
        self.grab_set()
        self.lift()

        # Ícone da Janela
        self.iconbitmap(False, "assets/icons/icon_16x16.ico")

        # Paleta de cores
        self.color_palette = palette_color_light
