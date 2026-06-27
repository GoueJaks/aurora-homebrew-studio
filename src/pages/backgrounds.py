import customtkinter as ctk

class BackgroundsPage(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        label = ctk.CTkLabel(
            self,
            text="Backgrounds",
            font=("Segoe UI", 28, "bold")
        )

        label.pack(pady=40)