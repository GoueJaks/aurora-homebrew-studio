import customtkinter as ctk


class SpellsPage(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        label = ctk.CTkLabel(
            self,
            text="Spells",
            font=("Segoe UI", 28, "bold")
        )

        label.pack(pady=40)