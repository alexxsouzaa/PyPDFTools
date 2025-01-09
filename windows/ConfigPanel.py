import customtkinter as ctk

class FrameAsButtonApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.title("Frame como Botão")

        # Criando um Frame estilizado como botão
        self.clickable_frame = ctk.CTkFrame(
            master=self,
            width=200,
            height=100,
            corner_radius=10,
            fg_color="#3498db"  # Azul inicial
        )
        self.clickable_frame.place(x=100, y=100)

        # Adicionando texto dentro do Frame
        self.label = ctk.CTkLabel(
            master=self.clickable_frame,
            text="Clique aqui",
            text_color="white",
            font=("Segoe UI", 16)
        )
        self.label.place(relx=0.5, rely=0.5, anchor="center")

        # Associando eventos ao Frame e ao Label
        self.clickable_frame.bind("<Button-1>", self.on_frame_click)
        self.label.bind("<Button-1>", self.on_frame_click)  # Garante clique no texto também

        # Adicionando efeito de hover
        self.clickable_frame.bind("<Enter>", self.on_hover)
        self.clickable_frame.bind("<Leave>", self.on_leave)

    def on_frame_click(self, event):
        print("Frame clicado!")

    def on_hover(self, event):
        self.clickable_frame.configure(fg_color="#2980b9")  # Cor mais escura no hover

    def on_leave(self, event):
        self.clickable_frame.configure(fg_color="#3498db")  # Cor original ao sair


if __name__ == "__main__":
    app = FrameAsButtonApp()
    app.mainloop()
