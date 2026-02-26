"""Main application entry point for ACSSQDA 1.1.

This module initializes and runs the invoice management application.
"""

import customtkinter

from screenconfig import ScreenConfig
from views.components.menubar import ApplicationMenuBar
from views.frames.main_frame import MainFrame


class InvoiceApplication(customtkinter.CTk):
    """Main application window for invoice management system.
    
    This class initializes the main window with all UI components including
    the screen configuration, menu bar, and main frame.
    """

    def __init__(self) -> None:
        """Initialize the invoice application with all UI components."""
        super().__init__()

        # Configure the application window
        ScreenConfig(self, "ACSSQDA 1.1")

        # Initialize the menu bar
        ApplicationMenuBar(self)

        # Initialize the main content frame
        self.main_frame = MainFrame(self)


if __name__ == "__main__":
    app = InvoiceApplication()
    app.mainloop()