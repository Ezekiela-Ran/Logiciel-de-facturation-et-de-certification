from customtkinter import CTkLabel, CTkEntry
import views.foundation.form_model as form_model

class ProformaBill(form_model.FormModel):
    def __init__(self, master):
        super().__init__(master)
        
        """ FORMULAIRE CLIENT """
        # Numéro de facture proforma
        def bill_number_frame(self):    
        
            bill_number = CTkLabel(self.client_form.left_frame, text="N° de facture proforma")
            bill_number.pack(anchor="w")
            
        # Champ pour la date
        def date_issue_frame(self):
            
            self.issue_date = CTkLabel(self.client_form.right_frame, text="Date")
            self.issue_date.pack(anchor="w")
                
            self.issue_date_input = CTkEntry(self.client_form.right_frame, width=self.master.styles.entry_width, height=self.master.styles.entry_height)
            self.issue_date_input.pack(anchor="w")
            
        """ BASE DE DONNEES """
        # Numéro de facture proforma
        
        def bill_number_label(self):
            bill_number = CTkLabel(self.database_records.second_column, text="N° de facture proforma")
            bill_number.pack(anchor="w")
        
        # Label date d'émission    
        def date_label(self):
            issue_date = CTkLabel(self.database_records.third_column, text="Date")
            issue_date.pack(anchor="w")
        
        
        # Appel des méthodes pour afficher les champs spécifiques à la facture proforma    
        bill_number_frame(self)
        date_issue_frame(self)
        
        # Appel de la méthode pour afficher les labels de la base de données 
        bill_number_label(self)
        date_label(self)