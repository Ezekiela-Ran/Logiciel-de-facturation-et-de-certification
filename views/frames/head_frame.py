import customtkinter
from views.bill_type.regularbill import RegularBill
from views.bill_type.proformabill import ProformaBill
from views.foundation.styles import Styles

class HeadFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        self.styles = Styles()
        super().__init__(master)
        
        # Initialiasation de la facture affichée par défaut    
        self.regular_bill = RegularBill(self)
        
        # Formulaire de la facture:
        self.regular_bill.client_form.pack(side="left", pady=self.styles.pady)   
        
        # Affichage des enregistrements de la base de données
        self.regular_bill.database_records.pack(side="right", expand=True, fill="both", pady=self.styles.pady)
    
    # Méthode pour effacer le contenu du cadre de tête avant d'afficher une nouvelle facture    
    def clear_head_frame(self):
        for widget in self.winfo_children():
            widget.destroy()
          
    
    # Méthode pour afficher la facture régulière      
    def display_regular_bill(self):
        
        self.clear_head_frame()
        
        self.regular_bill = RegularBill(self)
        self.regular_bill.client_form.pack(side="left", expand=True, fill="both", pady=self.styles.pady)   
        self.regular_bill.database_records.pack(side="right", expand=True, fill="both", pady=self.styles.pady)
        
    
    # Méthode pour afficher la facture proforma        
    def display_proforma_bill(self):
        
        self.clear_head_frame()
        
        self.proforma_bill = ProformaBill(self)  
        self.proforma_bill.client_form.pack(side="left", expand=True, fill="both", pady=self.styles.pady)  
        self.proforma_bill.database_records.pack(side="right", expand=True, fill="both", pady=self.styles.pady)
       
    
