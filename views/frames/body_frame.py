"""Body frame component for the application.

This module contains the body section of the application which can be
used for additional content or features.
"""

import customtkinter


class BodyFrame(customtkinter.CTkFrame):
    """Body frame for additional content.
    
    This frame serves as a container for additional content between
    the header and footer sections.
    """

    def __init__(self, master) -> None:
        """Initialize the body frame.
        
        Args:
            master: The parent widget (MainFrame).
        """
        super().__init__(master)