import customtkinter
class ProformaBill(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.label = customtkinter.CTkLabel(self, text="This is the Proforma Bill class")
        self.label.pack(pady=20)