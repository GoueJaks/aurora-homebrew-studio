import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, width=220)

        self.grid_propagate(False)

        title = ctk.CTkLabel(
            self,
            text="Aurora\nHomebrew\nStudio",
            font=("Segoe UI", 22, "bold")
        )

        title.pack(pady=(25, 30))

        pages = [
            "Home",
            "Items",
            "Magic Items",
            "Spells",
            "Feats",
            "Backgrounds",
            "Monsters",
            "Settings"
        ]

        for page in pages:
            button = ctk.CTkButton(
                self,
                text=page,
                command=lambda p=page: master.show_page(p)
            )

            button.pack(fill="x", padx=15, pady=5)