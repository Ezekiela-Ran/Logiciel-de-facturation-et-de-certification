import customtkinter
from screenconfig import ScreenConfig
from views.components.menubar import MenuBar
from views.frames.main_frame import MainFrame

# PROGRAMME PRINCIPALE:

class Main(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Configuration de la fenêtre
        ScreenConfig(self, "ACSSQDA 1.1")

        # Barre de menu
        MenuBar(self)

        # Fenêtre principale
        self.main_frame = MainFrame(self)
    
    
app = Main()
app.mainloop()