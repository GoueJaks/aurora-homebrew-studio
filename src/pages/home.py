import customtkinter as ctk


class HomePage(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        title = ctk.CTkLabel(
            self,
            text="Welcome to Aurora Homebrew Studio",
            font=("Segoe UI", 28, "bold")
        )

        title.pack(pady=40)

        subtitle = ctk.CTkLabel(
            self,
            text="Create and manage homebrew content for the Aurora Character Builder.",
            font=("Segoe UI", 16)
        )

        subtitle.pack()