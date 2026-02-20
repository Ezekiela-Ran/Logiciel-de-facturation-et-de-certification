import customtkinter

class ScreenConfig(customtkinter.CTk):

    def __init__(self, master, width, title):

        self.master = master
        self.screen_width = width

        self.title = title
        
        self.screen_height = self.master.winfo_screenheight()

        self.master.geometry(f"{self.screen_width}x{int(self.screen_height * 0.8)}")

        self.master.title(self.title)