import customtkinter as ctk
from PIL import Image
from modules.colors.palette_color import *
from windows.MainScreen import MainScreen

class LoginScreen(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color="#F5F5F5")
        
        # Configuração da janela principal
        self.geometry("780x480+250+100")
        self.title("Login - PyPDFTools")
        self.overrideredirect(False)  # Permitir controle da janela
        self.resizable(False, False)  # Desabilitar redimensionamento
        self._set_appearance_mode("light") # Tema da janela

        # Ícone da Janela
        self.iconbitmap("assets/icons/icon_16x16.ico")

        # Paleta de cores
        self.color_palette = palette_color_light

        # === Criação dos Frames === #
        # Frame da imagem (lado esquerdo)
        self.frame_image = ctk.CTkFrame(
            master=self,
            height=480,
            width=464,
            corner_radius=6,
            fg_color=self.color_palette["purple"],
            bg_color=self.color_palette["purple"]
        )
        self.frame_image.place(x=0, y=0)

        # Frame de autenticação (lado direito)
        self.frame_auth = ctk.CTkFrame(
            master=self,
            height=480,
            width=316,
            fg_color=self.color_palette["color_bg"],
            bg_color=self.color_palette["color_bg"]
        )
        self.frame_auth.place(x=464, y=0)

        # Frame divisor (linha decorativa no frame de autenticação)
        self.frame_divider = ctk.CTkFrame(
            master=self.frame_auth,
            height=2,
            width=260,
            corner_radius=10,
            fg_color=self.color_palette["light_gray"],
        )
        self.frame_divider.place(x=28, y=156)

        # === Imagem de Fundo === #
        self.background_image = ctk.CTkImage(
            light_image=Image.open("assets/images/background_login.png"),
            dark_image=Image.open("assets/images/background_login.png"),
            size=(464, 480)
        )

        # Label para exibir a imagem de fundo
        self.label_background = ctk.CTkLabel(
            master=self,
            image=self.background_image,
            text=""
        )
        self.label_background.place(x=0, y=0)

        # === Campos de Entrada (Entrys) === #
        # Título do campo de email/usuário
        self.label_email_title = ctk.CTkLabel(
            master=self.frame_auth,
            text="E-mail ou usuário",
            font=('Segoe UI', 10),
            text_color=self.color_palette["dark_gray"]
        )
        self.label_email_title.place(x=28, y=184)

        # Campo de entrada para email/usuário
        self.entry_email = ctk.CTkEntry(
            master=self.frame_auth,
            border_width=0,
            corner_radius=8,
            fg_color=self.color_palette["light_gray"],
            text_color=self.color_palette["dark_gray"],
            font=('Segoe UI', 10),
            height=32,
            width=260
        )
        self.entry_email.place(x=28, y=208)

        # Título do campo de senha
        self.label_password_title = ctk.CTkLabel(
            master=self.frame_auth,
            text="Senha",
            font=('Segoe UI', 10),
            text_color=self.color_palette["dark_gray"]
        )
        self.label_password_title.place(x=28, y=246)

        # Campo de entrada para senha
        self.entry_password = ctk.CTkEntry(
            master=self.frame_auth,
            border_width=0,
            corner_radius=8,
            fg_color=self.color_palette["light_gray"],
            text_color=self.color_palette["dark_gray"],
            font=('Segoe UI', 10),
            show='*',
            height=32,
            width=260
        )
        self.entry_password.place(x=28, y=269)

        # === Textos (Labels) === #
        # Título principal
        self.label_welcome = ctk.CTkLabel(
            master=self.frame_auth,
            text="Bem-vindo de volta!",
            font=('Segoe UI', 26, 'bold'),
            text_color=self.color_palette["color_title"]
        )
        self.label_welcome.place(x=28, y=80)

        # Subtítulo
        self.label_subtitle = ctk.CTkLabel(
            master=self.frame_auth,
            text="Faça login para acessar sua conta.",
            font=('Segoe UI', 10),
            text_color=self.color_palette["dark_gray"]
        )
        self.label_subtitle.place(x=28, y=111)

        # Rodapé com informações de suporte
        self.label_footer = ctk.CTkLabel(
            master=self.frame_auth,
            text="Dúvidas ou problemas? Entre em contato\ncom nosso suporte técnico.",
            text_color=self.color_palette["dark_gray"],
            font=('Segoe UI', 10),
            justify="center"
        )
        self.label_footer.place(x=66, y=434)

        # === Botões (Buttons) === #
        # Botão de login
        self.button_login = ctk.CTkButton(
            master=self.frame_auth,
            text="Entrar",
            font=('Segoe UI', 12, 'bold'),
            corner_radius=50,
            fg_color=self.color_palette["purple"],
            hover_color=self.color_palette["dark_purple"],
            height=32,
            width=260,
            command=self.open_main_screen  # Passa a referência da função
        )
        self.button_login.place(x=28, y=327)

        # === Switch para Tema === #
        self.switch_theme_var = ctk.StringVar(value="light")
        self.switch_theme = ctk.CTkSwitch(
            master=self.frame_auth,
            text="",
            command=self.toggle_theme,
            variable=self.switch_theme_var,
            onvalue="dark",
            offvalue="light",
            hover=self.color_palette["light_purple"],
            corner_radius=20
        )
        self.switch_theme.place(x=250, y=10)

    def toggle_theme(self):
        """Alterna o tema da aplicação (claro ou escuro)."""
        self._set_appearance_mode(self.switch_theme_var.get())

        # Atualiza a paleta de cores
        self.color_palette = palette_color_light if self.switch_theme_var.get() == "light" else palette_color_dark
        self.update_theme_colors()

    def update_theme_colors(self):
        """Atualiza as cores da interface com base na paleta de cores atual."""
        self.frame_auth.configure(fg_color=self.color_palette["color_bg"], bg_color=self.color_palette["color_bg"])
        self.frame_divider.configure(fg_color=self.color_palette["light_gray"])
        self.entry_email.configure(fg_color=self.color_palette["light_gray"])
        self.entry_password.configure(fg_color=self.color_palette["light_gray"])
        self.label_welcome.configure(text_color=self.color_palette["color_title"])

    def open_main_screen(self):
        """Abre a tela principal após o login."""
        MainScreen(self)


LoginScreen = LoginScreen()
LoginScreen.mainloop()
