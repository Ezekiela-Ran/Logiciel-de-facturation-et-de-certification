import customtkinter

class ScreenConfig(customtkinter.CTk):

    def __init__(self, master, title):

        self.master = master
        
        self.title = title
        
        self.screen_width = self.master.winfo_screenwidth()

        
        self.screen_height = self.master.winfo_screenheight()

        self.master.geometry(f"{int(self.screen_width * 0.8)}x{int(self.screen_height * 0.8)}")

        self.master.title(self.title)