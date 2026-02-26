"""Base model for invoice forms.

This module provides a base class for different invoice types with common
elements like client form and database records display.
"""

from views.foundation.styles import UIStyles, Styles
from views.frames.client_form_frame import ClientFormFrame
from views.frames.database_frame import DatabaseFrame


class InvoiceFormModel:
    """Base model for invoice form types.
    
    This class provides common functionality for different invoice types,
    including client information form and database records display.
    """

    def __init__(self, master) -> None:
        """Initialize the invoice form model.
        
        Args:
            master: The parent widget (typically a header frame).
        """
        self.styles = UIStyles()
        self.master = master

        # Initialize client information form
        self.client_form = ClientFormFrame(self.master)
        self._initialize_client_form()

        # Initialize database records display
        self.database_records = DatabaseFrame(self.master)

    def _initialize_client_form(self) -> None:
        """Initialize all client form fields."""
        self.client_form.company_name_frame()
        self.client_form.nif_frame()
        self.client_form.statistic_frame()
        self.client_form.responsible_frame()


# Legacy alias for backward compatibility
FormModel = InvoiceFormModel
        
        
   