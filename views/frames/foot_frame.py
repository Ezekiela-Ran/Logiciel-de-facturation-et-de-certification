"""Footer frame component for the application.

This module contains the footer section of the application which typically
contains control buttons and status information.
"""

import customtkinter


class FootFrame(customtkinter.CTkFrame):
    """Footer frame for control buttons and status information.
    
    This frame serves as the footer section containing action buttons
    and status indicators.
    """

    def __init__(self, master) -> None:
        """Initialize the footer frame.
        
        Args:
            master: The parent widget (MainFrame).
        """
        super().__init__(master)