from customtkinter import CTkFrame, CTkLabel
import customtkinter


class DatabaseFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.master = master
        
        self.pack(side="right", fill="both", expand=True)
        
        self.first_column = CTkFrame(self)
        self.first_column.pack(side="left", fill="both", expand=True, pady=self.master.styles.pady)
        
        self.second_column = CTkFrame(self)
        self.second_column.pack(side="left", fill="both", expand=True, pady=self.master.styles.pady)
        
        self.third_column = CTkFrame(self)
        self.third_column.pack(side="left", fill="both", expand=True, pady=self.master.styles.pady)
        
        
    # Label raison sociale       
    def company_name_label(self):
        company_name = CTkLabel(self.first_column, text="Raison sociale")
        company_name.pack(anchor="w")
        