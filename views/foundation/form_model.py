from views.foundation.styles import Styles
from views.frames.client_form_frame import ClientFormFrame
from views.frames.database_frame import DatabaseFrame

class FormModel:
    def __init__(self, master):
        
        self.styles = Styles()
        
        self.master = master
        
        # Formulaire client
        self.client_form = ClientFormFrame(self.master)
        
        
        self.client_form.company_name_frame()
        self.client_form.nif_frame()
        self.client_form.statistic_frame()
        self.client_form.responsible_frame()
        
        # Base de donnée
        self.database_records = DatabaseFrame(self.master)
        
        self.database_records.company_name_label()
        
        
   