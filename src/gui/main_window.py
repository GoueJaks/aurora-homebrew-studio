import customtkinter as ctk

from gui.sidebar import Sidebar
from pages.home import HomePage
from pages.items import ItemsPage
from pages.magic_items import MagicItemsPage
from pages.spells import SpellsPage
from pages.feats import FeatsPage
from pages.backgrounds import BackgroundsPage
from pages.monsters import MonstersPage
from pages.settings import SettingsPage


class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Aurora Homebrew Studio")
        self.geometry("1400x850")
        self.minsize(1200, 700)

        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar = Sidebar(self)
        self.sidebar.grid(row=0, column=0, sticky="ns")

        self.page_container = ctk.CTkFrame(self, corner_radius=0)
        self.page_container.grid(row=0, column=1, sticky="nsew")

        self.pages = {
            "Home": HomePage(self.page_container),
            "Items": ItemsPage(self.page_container),
            "Magic Items": MagicItemsPage(self.page_container),
            "Spells": SpellsPage(self.page_container),
            "Feats": FeatsPage(self.page_container),
            "Backgrounds": BackgroundsPage(self.page_container),
            "Monsters": MonstersPage(self.page_container),
            "Settings": SettingsPage(self.page_container),
        }

        self.show_page("Home")

    def show_page(self, page_name):

        # Hide all pages
        for page in self.pages.values():
            page.pack_forget()

        # Show selected page
        self.pages[page_name].pack(fill="both", expand=True)