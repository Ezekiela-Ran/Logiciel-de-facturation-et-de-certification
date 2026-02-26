"""Main frame container for the application.

This module defines the main scrollable frame that contains all sections
of the application: header, body, and footer.
"""

import customtkinter

from views.frames.head_frame import HeadFrame
from views.frames.body_frame import BodyFrame
from views.frames.foot_frame import FootFrame
from views.foundation.styles import UIStyles


class MainFrame(customtkinter.CTkScrollableFrame):
    """Main application frame containing header, body, and footer sections.
    
    This frame organizes the layout into three main sections:
    - Header: Invoice form and database records
    - Body: Additional content area
    - Footer: Control buttons and status information
    """

    def __init__(self, master) -> None:
        """Initialize the main application frame.
        
        Args:
            master: The root CTk application instance.
        """
        styles = UIStyles()

        super().__init__(master)

        self.pack(
            fill="both",
            expand=True,
            padx=styles.padx,
            pady=styles.pady
        )

        # Initialize header section with invoice forms
        self.head_frame = HeadFrame(self)
        self.head_frame.pack(
            fill="both",
            expand=True,
            pady=styles.pady,
            side="top"
        )

        # Initialize body section
        self.body_frame = BodyFrame(self)
        self.body_frame.pack(
            fill="both",
            expand=True,
            pady=styles.pady,
            side="top"
        )

        # Initialize footer section
        self.foot_frame = FootFrame(self)
        self.foot_frame.pack(
            fill="both",
            expand=True,
            pady=styles.pady,
            side="bottom"
        )
    