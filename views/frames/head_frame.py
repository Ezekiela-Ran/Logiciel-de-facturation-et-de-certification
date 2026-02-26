"""Header frame for invoice forms and database records.

This module contains the header section that displays invoice forms
and database records. It supports switching between different invoice types.
"""

import customtkinter

from views.bill_type.standard_invoice import StandardInvoice
from views.bill_type.proforma_invoice import ProformaInvoice
from views.foundation.styles import UIStyles


class HeadFrame(customtkinter.CTkFrame):
    """Header frame for displaying invoice forms and records.
    
    This frame displays the invoice form and corresponding database records.
    It supports switching between regular and proforma invoice types.
    """

    def __init__(self, master) -> None:
        """Initialize the header frame.
        
        Args:
            master: The parent widget (MainFrame).
        """
        self.styles = UIStyles()
        super().__init__(master)

        # Initialize with regular invoice by default
        self.current_invoice = None
        self.display_regular_bill()

    def _clear(self) -> None:
        """Clear all child widgets from the frame."""
        for widget in self.winfo_children():
            widget.destroy()

    def clear_head_frame(self) -> None:
        """Clear the frame content before displaying a new invoice type."""
        self._clear()

    def display_regular_bill(self) -> None:
        """Display the regular invoice form.
        
        Switches to display the regular bill type with all its specific fields
        and database records.
        """
        self.clear_head_frame()
        self.current_invoice = StandardInvoice(self)

    def display_proforma_bill(self) -> None:
        """Display the proforma invoice form.
        
        Switches to display the proforma bill type with all its specific fields
        and database records.
        """
        self.clear_head_frame()
        self.current_invoice = ProformaInvoice(self)
       
    
