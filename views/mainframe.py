import customtkinter
from views.bill import Bill
from views.proformabill import ProformaBill

class MainFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill="both", expand=True)
    
    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

    def default_display(self):
        self.clear_frame()
        Bill(self).pack(fill="both", expand=True)

    def display_bill(self):
        self.clear_frame()
        Bill(self).pack(fill="both", expand=True)

    def display_proforma_bill(self):
        self.clear_frame()
        ProformaBill(self).pack(fill="both", expand=True)

    