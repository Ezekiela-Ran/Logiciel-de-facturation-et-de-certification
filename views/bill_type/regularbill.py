from customtkinter import CTkFrame, CTkLabel, CTkEntry
import views.foundation.form_model as form_model
from views.foundation.styles import Styles

class RegularBill(form_model.FormModel):
    def __init__(self, master):
        super().__init__(master)
        
        self.styles = Styles()
        
        # Appel des méthodes pour afficher les champs spécifiques à la facture régulière
        
        """ FORMULAIRE CLIENT """
        # Champs pour date de résultat    
        def date_result_frame(self):
            
            self.result_date = CTkLabel(self.client_form.right_frame, text="Date de résultat")
            self.result_date.pack(anchor="w")
            
            self.result_date_input = CTkEntry(self.client_form.right_frame, width=self.master.styles.entry_width, height=self.master.styles.entry_height)
            self.result_date_input.pack(anchor="w")
        
        # Champs pour adresse de l'entreprise
        def address_frame(self):
            
            self.address = CTkLabel(self.client_form.left_frame, text="Adresse")
            self.address.pack(anchor="w")
            
            self.address_input = CTkEntry(self.client_form.left_frame, width=self.master.styles.entry_width, height=self.master.styles.entry_height)
            self.address_input.pack(anchor="w")
            
        # Champs pour les réferences des produits
        def product_reference_frame(self):
            
            self.product_reference = CTkLabel(self.client_form.right_frame, text="Réf produits")
            self.product_reference.pack(anchor="w")
            
            self.product_reference_input = CTkEntry(self.client_form.right_frame, width=self.master.styles.entry_width, height=self.master.styles.entry_height)
            self.product_reference_input.pack(anchor="w")
            
        # Champ pour la date d'émission
        def date_issue_frame(self):
            
            self.issue_date = CTkLabel(self.client_form.right_frame, text="Date d'émission")
            self.issue_date.pack(anchor="w")
                
            self.issue_date_input = CTkEntry(self.client_form.right_frame, width=self.master.styles.entry_width, height=self.master.styles.entry_height)
            self.issue_date_input.pack(anchor="w")
        
        # Numéro de facture
        def bill_number_frame(self):    
        
            bill_number = CTkLabel(self.client_form.left_frame, text="N° de facture")
            bill_number.pack(anchor="w")

        """ BASE DE DONNEES """
        # Label numéro de facture
        def bill_number_label(self):
            bill_number = CTkLabel(self.database_records.second_column, text="N° de facture")
            bill_number.pack(anchor="w")
            
        # Label date d'émission    
        def date_label(self):
            issue_date = CTkLabel(self.database_records.third_column, text="Date d'émission")
            issue_date.pack(anchor="w")
            
        def display_database_records(self, records):
        # Effacer les enregistrements précédents
            
            for record in records:
                company_name = CTkLabel(self.database_records.first_column, text=record[0])
                company_name.pack(anchor="w")
                
                bill_number = CTkLabel(self.database_records.second_column, text=record[1])
                bill_number.pack(anchor="w")
                
                date = CTkLabel(self.database_records.third_column, text=record[2])
                date.pack(anchor="w")
        
        # Exemple de liste de données pour records 
        records = [ ("Tech Solutions SARL", "FAC-001", "2026-01-15"), ("Green Energy Corp", "FAC-002", "2026-01-20"), ("Madagascar Logistics", "FAC-003", "2026-02-01"), ("Oceanic Trading", "FAC-004", "2026-02-10"), ("Digital Future Ltd", "FAC-005", "2026-02-18"),]
        
        # Appel des méthodes pour afficher les champs spécifiques à la facture proforma       
        date_issue_frame(self)
        date_result_frame(self)
        address_frame(self)
        product_reference_frame(self)
        bill_number_frame(self)
        
        
        # Appel de la méthode pour afficher les labels de la base de données 
        bill_number_label(self)
        date_label(self)
        
        # Appel de la méthode pour afficher les enregistrements de la base de données
        display_database_records(self, records)