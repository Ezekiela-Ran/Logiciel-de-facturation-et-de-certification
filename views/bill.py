import customtkinter

class Bill(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.label = customtkinter.CTkLabel(self, text="This is the Bill class")
        self.label.pack(pady=20)