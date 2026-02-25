from customtkinter import CTkFrame, CTkLabel, CTkEntry

class ClientFormFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.master = master
        
        # cadre de gauche pour le formulaire client
        self.left_frame = CTkFrame(self)  
        self.left_frame.pack(side="left", fill="both", expand=True, pady=self.master.styles.pady)
        
        # cadre de droite pour le formulaire client
        self.right_frame = CTkFrame(self)
        self.right_frame.pack(side="right", fill="both", expand=True, pady=self.master.styles.pady)
        
        
        self.pack(side="left", fill="both", expand=True, pady=self.master.styles.pady)
    
    # Raison sociale    
    def company_name_frame(self):
        
        company_name = CTkLabel(self.left_frame, text="Raison sociale")
        company_name.pack(anchor="w")
        
        input_company_name = CTkEntry(self.left_frame, width=self.master.styles.entry_width, height=self.master.styles.entry_height)
        input_company_name.pack(anchor="w")
        
    # NIF    
    def nif_frame(self):
        
        Nif = CTkLabel(self.left_frame, text="NIF")
        Nif.pack(anchor="w")
        
        input_nif = CTkEntry(self.left_frame, width=self.master.styles.entry_width, height=self.master.styles.entry_height)
        input_nif.pack(anchor="w")
        
    # Statistic    
    def statistic_frame(self):
        
        Statistic = CTkLabel(self.left_frame, text="Statistique")
        Statistic.pack(anchor="w")
        
        input_statistic = CTkEntry(self.left_frame, width=self.master.styles.entry_width, height=self.master.styles.entry_height)
        input_statistic.pack(anchor="w")    
        
    # Responsable
    def responsible_frame(self):
        
        Responsible = CTkLabel(self.right_frame, text="Responsable")
        Responsible.pack(anchor="w")
        
        input_responsible = CTkEntry(self.right_frame, width=self.master.styles.entry_width, height=self.master.styles.entry_height)
        input_responsible.pack(anchor="w")
        
    