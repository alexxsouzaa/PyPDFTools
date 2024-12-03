import customtkinter
from PIL import Image
from modules.colors.palette_color import *

class LoginScreen(customtkinter.CTk):
    def __init__(self):
        super().__init__(fg_color="#F5F5F5")
        self.geometry("780x480+250+100")
        self.title("PyPDFTools")
        self.overrideredirect(False)
        self.resizable(False, False)

        self.colors = palette_color_light

        #====== Frames ======#
        # Frame para imagem
        self.ImagemFrame = customtkinter.CTkFrame(
            master=self,
            height=480,
            width=464,
            corner_radius= 6,
            border_width=0,
            fg_color=self.colors["purple"],
            bg_color=self.colors["purple"]
        )
        self.ImagemFrame.place(x=0, y=0)

        # Frame de login
        self.AuthFrame = customtkinter.CTkFrame(
            master=self,
            height=480,
            width=316,
            fg_color=self.colors["color_bg"],
            bg_color=self.colors["color_bg"]
        )
        self.AuthFrame.place(x=464, y=0)

        # Frame do Divisor
        self.DivisorFrame = customtkinter.CTkFrame(
            master=self.AuthFrame,
            height=2,
            width=260,
            corner_radius=10,
            fg_color=self.colors["light_gray"],

        )
        self.DivisorFrame.place(x=28, y=156)

        #====== Imagem ======#
        self.BackgroundImagem = customtkinter.CTkImage(
            light_image=Image.open("assets/images/background_login.png"),
            dark_image=Image.open("assets/images/background_login.png"),
            size=(464, 480)
        )

        #====== Entrys ======#
        # Titulo da entry de email
        self.TitleEntryEmail = customtkinter.CTkLabel(
            master=self.AuthFrame,
            text="E-mail ou usuário",
            font=('Segoe UI', 10, 'normal'),
            text_color=self.colors["dark_gray"]
        )
        self.TitleEntryEmail.place(x=28, y=184)

        # Entry E-mail
        self.EmailEntry = customtkinter.CTkEntry(
            master=self.AuthFrame,
            border_width=0,
            corner_radius=8,
            fg_color=self.colors["light_gray"],
            text_color=self.colors["dark_gray"],
            font=('Segoe UI', 10, 'normal'),
            height=32,
            width=260
            )
        self.EmailEntry.place(x=28, y=208)

        # Titulo da entry de email
        self.TitleEntrySenha = customtkinter.CTkLabel(
            master=self.AuthFrame,
            text="Senha",
            font=('Segoe UI', 10, 'normal'),
            text_color=self.colors["dark_gray"]
        )
        self.TitleEntrySenha.place(x=28, y=246)
        
        # Entry Senha
        self.SenhaEntry = customtkinter.CTkEntry(
            master=self.AuthFrame,
            border_width=0,
            corner_radius=8,
            fg_color=self.colors["light_gray"],
            text_color=self.colors["dark_gray"],
            font=('Segoe UI', 10, 'normal'),
            show='*',
            height=32,
            width=260
            )
        self.SenhaEntry.place(x=28, y=269)

        #====== Buttons ======#
        # Button login
        self.LoginButton = customtkinter.CTkButton(
            master=self.AuthFrame,
            text="Entrar",
            font=('Segoe UI', 12, 'bold'),
            border_width=0,
            corner_radius=20,
            fg_color=self.colors["purple"],
            hover_color=self.colors["dark_purple"],
            height=32,
            width=260
            )
        self.LoginButton.place(x=28, y=327)

        #====== Labels ======#
        # Label de titulo
        self.TituloLabel = customtkinter.CTkLabel(
            master=self.AuthFrame,
            text="Bem-vindo de volta!",
            font=('Segoe UI', 26, 'bold'),
            text_color=self.colors["color_title"]
        )
        self.TituloLabel.place(x=28, y=80)

        # Label de subtitulo
        self.SubtituloLabel = customtkinter.CTkLabel(
            master=self.AuthFrame,
            text="Faça login para acessar sua conta.",
            font=('Segoe UI', 10, 'normal'),
            text_color=self.colors["dark_gray"]
        )
        self.SubtituloLabel.place(x=28, y=111)

        # Label rodapé
        self.RodapeLabel = customtkinter.CTkLabel(
            master=self.AuthFrame,
            text="Dúvidas ou problemas? Entre em contato\n com nosso suporte técnico.",
            text_color=self.colors["dark_gray"],
            font=('Segoe UI', 10, 'normal'),
            justify="center"
        )
        self.RodapeLabel.place(x=66, y=434)

        # Label da background
        self.BackgroundLabel = customtkinter.CTkLabel(
            master=self,
            image=self.BackgroundImagem,
            text=""
        )
        self.BackgroundLabel.place(x=0, y=0)

        #===== Switchs =====#
        # Shitch do tema
        self.theme_switch_var = customtkinter.StringVar(value="light")
        self.theme_switch = customtkinter.CTkSwitch(
            master=self.AuthFrame,
            text="",
            command=self.theme_switch_event,
            variable=self.theme_switch_var,
            onvalue="dark",
            offvalue="light",
            hover=self.colors["light_purple"],
            corner_radius=20
            )
        self.theme_switch.place(x=240, y=20)

    def theme_switch_event(self):
        # Altera o tema da janela
        self._set_appearance_mode(self.theme_switch_var.get())

        try:
            # Altera entre as paletas de cores "Light" e "Dark"
            if self.theme_switch_var.get() == "light":
                # Paleta "Light"
                self.colors = palette_color_light
            else:
                # Paleta "Dark"
                self.colors = palette_color_dark
        except:
            pass

        # Atualiza o tema
        self.update_thema()

    def update_thema(self):
        # Atualiza as cores do tema
        self.AuthFrame.configure(fg_color=self.colors["color_bg"],  bg_color=self.colors["color_bg"])
        self.DivisorFrame.configure(fg_color=self.colors["light_gray"],  bg_color=self.colors["light_gray"])
        self.EmailEntry.configure(fg_color=self.colors["light_gray"])
        self.SenhaEntry.configure(fg_color=self.colors["light_gray"])
        self.TituloLabel.configure(text_color=self.colors["color_title"])

        


        

        




# Inicialização da aplicação
LoginScreen = LoginScreen()
LoginScreen.mainloop()
