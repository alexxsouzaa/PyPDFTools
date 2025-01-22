import customtkinter as ctk
import os
from PIL import Image
from modules.colors.palette_color import *
from windows.MergePDFScreen import MergePDF

class MainScreen(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master, fg_color="#FFF")
        
        # Configuração da janela principal
        self.geometry("780x480")
        self.title("PyPDFTools")
        self.overrideredirect(False)  # Permitir controle da janela
        self.resizable(False, False)  # Desabilitar redimensionamento
        self.grab_set()
        self.lift()

        # Ícone da Janela
        self.iconbitmap(False, "assets/icons/icon_16x16.ico")

        # Paleta de cores
        self.color_palette = palette_color_light

        # === Frames === #
        # Frame do Logo (lado direito)
        self.frame_logo = ctk.CTkFrame(
            master=self,
            fg_color=self.color_palette["light_gray"],
            corner_radius=50,
            width=150,
            height=34
        )
        self.frame_logo.place(x=24, y=24)

        self.menu()
        
        # Frame do Usuario (lado esquerdo)
        self.frame_user = ctk.CTkFrame(
            master=self,
            fg_color=self.color_palette["light_gray"],
            corner_radius=50,
            width=106,
            height=34
        )
        self.frame_user.place(x=650, y=24)

        # === Botões (Buttons) === #
        # Botão de notificações
        self.button_notification = ctk.CTkButton(
            master=self.frame_user,
            text="",
            corner_radius=50,
            width= 28,
            height=28,
            fg_color=self.color_palette["white"]
        )
        self.button_notification.place(x=3, y=3)

        # Botão de troca de tema
        self.button_theme = ctk.CTkButton(
            master=self.frame_user,
            text="",
            corner_radius=50,
            width= 28,
            height=28,
            fg_color=self.color_palette["white"]
        )
        self.button_theme.place(x=39, y=3)

        # Botão de usuario
        self.button_user = ctk.CTkButton(
            master=self.frame_user,
            text="",
            corner_radius=50,
            width= 28,
            height=28,
            fg_color=self.color_palette["lilac"],
            hover_color=self.color_palette["purple"]
        )
        self.button_user.place(x=75, y=3)

        # === Imagens === #
        # Imagem do logo
        self.image_logo = ctk.CTkImage(
            light_image=Image.open("assets/images/logo.png"),
            dark_image=Image.open("assets/images/logo.png"),
            size=(79, 14)
        )

        # === Label === 
        # Label para exibir do logo
        self.label_logo = ctk.CTkLabel(
            master=self.frame_logo,
            image=self.image_logo,
            text=""
        )
        self.label_logo.place(x=35, y=4)

        # Cards de informação
        self.card_information(
            bg_color=self.color_palette["dark_blue"],
            text_color=self.color_palette["gray"],
            title="Totalmente Grátis",
            subtitle="Um projeto de aprendizado criado para todos",
            icon_path="assets/icons/coins.png",
            x=24, y=90,
            width=276,
            height=88,
            )
        
        self.card_information(
            bg_color=self.color_palette["purple"],
            text_color=self.color_palette["white"],
            title="Meu GitHub",
            subtitle="Descubra outros projetos",
            icon_path="assets/icons/git_hub.png",
            x=316, y=90,
            width=212,
            height=88,
            )
        
        self.card_information(
            bg_color=self.color_palette["lilac"],
            text_color=self.color_palette["white"],
            title="Sobre o Projeto",
            subtitle="Saiba mais sobre a evolução do projeto",
            icon_path="assets/icons/folder.png",
            x=544, y=90,
            width=212,
            height=88,
            )

        # Cards de opções
        self.card_options(
            title="Juntar PDFs",
            subtitle="Combine e organize seus PDFs na ordem\nque preferir, de forma simples e rápida!",
            icon_path="assets/icons/arrow_shrink.png",
            x=25, y=210, classe=MergePDF
        )

        self.card_options(
            title="Dividir PDFs",
            subtitle="Selecione páginas específicas, separe ou\nconverta cada uma em PDFs individuais.",
            icon_path="assets/icons/arrow_expand.png",
            x=274, y=210,
        )

        self.card_options(
                    title="Proteger PDFs",
                    subtitle="Proteja PDFs com senha e evite acessos não\nautorizados.",
                    icon_path="assets/icons/padlock.png",
                    x=523, y=210
                )
        
        self.card_options(
                    title="PDF para JPG",
                    subtitle="Extraia as imagens contidas em um arquivo\nPDF ou converta cada página em um JPG",
                    icon_path="assets/icons/image.png",
                    x=25, y=337
                )
        
        self.card_options(
                    title="JPG para PDF",
                    subtitle="Converta suas imagens JPG para PDF. Ajuste\na orientação e as margens.",
                    icon_path="assets/icons/paper.png",
                    x=274, y=337
                )
        
        self.card_options(
                    title="WORD para PDF",
                    subtitle="Converta seus documentos WORD para PDF\ncom a máxima qualidade.",
                    icon_path="assets/icons/docs.png",
                    x=523, y=337
                )


    def card_information(self, x, y, width, height, bg_color="", text_color="", title="", subtitle="", icon_path=""):
        # Frame for the information card
        self.info_frame = ctk.CTkFrame(
            master=self,
            fg_color=bg_color,
            corner_radius=10,
            width=width,
            height=height
        )
        self.info_frame.place(x=x, y=y)

        # Title label of the card
        self.title_label = ctk.CTkLabel(
            master=self.info_frame,
            text=title,
            font=('Segoe UI', 12, 'bold'),
            text_color=self.color_palette["white"]
        )
        self.title_label.place(x=16, y=38)

        # Subtitle label of the card
        self.subtitle_label = ctk.CTkLabel(
            master=self.info_frame,
            text=subtitle,
            font=('Segoe UI', 10, 'normal'),
            text_color=text_color,
            height=8
        )
        self.subtitle_label.place(x=16, y=62)

        # === Icon === #
        # Validate if the icon path exists
        if os.path.exists(icon_path):
            # Load the icon image
            self.icon_image = ctk.CTkImage(
                light_image=Image.open(icon_path),
                dark_image=Image.open(icon_path),
                size=(12, 12)
            )
            
            # Label to display the icon
            self.icon_label = ctk.CTkLabel(
                master=self.info_frame,
                image=self.icon_image,
                text=""
            )
            self.icon_label.place(x=17, y=10)
        else:
            print(f"Error: Icon path '{icon_path}' not found.")

    def card_options(self, classe=None, x=int, y=int, title="", subtitle="", icon_path=""):
        frame_opitions = ctk.CTkFrame(
            master=self,
            width=233,
            height=111,
            corner_radius=10,
            fg_color=self.color_palette["light_gray"]
        )
        frame_opitions.place(x=x, y=y)

        title_label = ctk.CTkLabel(
            master=frame_opitions,
            text=title,
            font=('Segoe UI', 12, 'bold'),
            text_color=self.color_palette["dark_blue"]
        )
        title_label.place(x=16, y=48)

        subtitle_label = ctk.CTkLabel(
            master=frame_opitions,
            text=subtitle,
            font=('Segoe UI', 10, 'normal'),
            text_color=self.color_palette["gray"],
            anchor="w",
            justify="left"
        )
        subtitle_label.place(x=16, y=71)

        # === Icon === #
        # Validate if the icon path exists
        if os.path.exists(icon_path):
            # Load the icon image
                icon_image = ctk.CTkImage(
                light_image=Image.open(icon_path),
                dark_image=Image.open(icon_path),
                size=(24, 24)
            )
            
            # Label to display the icon
                icon_label = ctk.CTkLabel(
                master=frame_opitions,
                image=icon_image,
                text=""
            )
                icon_label.place(x=16, y=16)
        else:
            print(f"Error: Icon path '{icon_path}' not found.")


        def on_frame_click(event):
             screen = classe(self)

        # Altera o curso do mouse
        def on_enter(event):
            frame_opitions.configure(cursor="hand2")  # Altera o cursor ao entrar no frame
            title_label.configure(cursor="hand2")  # Altera o cursor ao entrar no frame
            subtitle_label.configure(cursor="hand2")  # Altera o cursor ao entrar no frame
            icon_label.configure(cursor="hand2")  # Altera o cursor ao entrar no frame

        def on_leave(event):
            frame_opitions.configure(cursor="")  # Volta ao cursor padrão ao sair do frame
            title_label.configure(cursor="")  # Volta ao cursor padrão ao sair do frame
            subtitle_label.configure(cursor="")  # Volta ao cursor padrão ao sair do frame
            icon_label.configure(cursor="")  # Volta ao cursor padrão ao sair do frame


        # Tornando todos os itens do card clicavel
        frame_opitions.bind("<Button-1>", on_frame_click)
        title_label.bind("<Button-1>", on_frame_click)
        subtitle_label.bind("<Button-1>", on_frame_click)
        icon_label.bind("<Button-1>", on_frame_click)

        frame_opitions.bind("<Enter>", on_enter)
        frame_opitions.bind("<Leave>", on_leave)   



    def menu(self):
        # Frame do Menu (centro)
        self.frame_menu = ctk.CTkFrame(
            master=self,
            fg_color=self.color_palette["light_gray"],
            corner_radius=50,
            width=460,
            height=34
        )
        self.frame_menu.place(x=182, y=24)



            