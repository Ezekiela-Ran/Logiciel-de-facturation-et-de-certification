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


        self.new = self.file_menu.add_submenu("Nouveau")
        self.new.add_option(option="Facture normale", command=lambda: master.main_frame.head_frame.display_regular_bill())
        self.new.add_option(option="Facture proforma", command=lambda: master.main_frame.head_frame.display_proforma_bill())


        self.file_menu.add_separator()


        self.print = self.file_menu.add_submenu("Imprimer")
        self.print.add_option(option="Facture normale")
        self.print.add_option(option="Facture proforma")
        self.print.add_option(option="Certification")



        
        # Dropdown menu pour le thème
        self.theme_menu = CustomDropdownMenu(widget=self.theme, master=master)
        self.theme_menu.add_option(option="Clair", command=lambda: customtkinter.set_appearance_mode("light"))
        self.theme_menu.add_option(option="Sombre", command=lambda: customtkinter.set_appearance_mode("dark"))