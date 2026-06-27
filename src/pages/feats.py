import customtkinter as ctk

class FeatsPage(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        label = ctk.CTkLabel(
            self,
            text="Feats",
            font=("Segoe UI", 28, "bold")
        )

        label.pack(pady=40)