import customtkinter
from CTkMenuBar import CTkMenuBar, CustomDropdownMenu

class MenuBar(CTkMenuBar):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Création des menus
        self.file = self.add_cascade(text="Fichier")
        self.theme = self.add_cascade(text="Thème")

        # Dropdown menu pour le fichier
        self.file_menu = CustomDropdownMenu(widget=self.file, master=master)
        
        self.file_menu.add_option(option="Nouveau facture", command=lambda: master.main_frame.display_bill())

        self.file_menu.add_option(option="Nouveau facture proforma", command=lambda: master.main_frame.display_proforma_bill())
        
        # Dropdown menu pour le thème
        self.theme_menu = CustomDropdownMenu(widget=self.theme, master=master)
        self.theme_menu.add_option(option="Clair", command=lambda: customtkinter.set_appearance_mode("light"))
        self.theme_menu.add_option(option="Sombre", command=lambda: customtkinter.set_appearance_mode("dark"))