import customtkinter
from views.screenconfig import ScreenConfig
from views.menubar import MenuBar
from views.mainframe import MainFrame

# PROGRAMME PRINCIPALE:

class Main(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Configuration de la fenêtre
        ScreenConfig(self, 1366, "ACSSQDA 1.1")

        # Barre de menu
        MenuBar(self)

        # Fenêtre principale
        self.main_frame = MainFrame(self)

        # Affichage par défaut
        self.main_frame.default_display()
    
    
app = Main()
app.mainloop()