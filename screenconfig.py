"""Screen configuration module for the invoice application.

This module handles the configuration and setup of the main window
properties such as dimensions and title.
"""

import customtkinter

# Screen configuration constants
WINDOW_WIDTH_RATIO = 0.8
WINDOW_HEIGHT_RATIO = 0.8


class ScreenConfig:
    """Configure the screen and window properties.
    
    This class sets up the application window with appropriate dimensions
    based on the screen size and applies the window title.
    """

    def __init__(self, root: customtkinter.CTk, title: str) -> None:
        """Initialize screen configuration.
        
        Args:
            root: The root CTk window instance.
            title: The title to display in the window title bar.
        """
        self.root = root
        self.window_title = title

        # Get screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate window dimensions based on screen size
        window_width = int(screen_width * WINDOW_WIDTH_RATIO)
        window_height = int(screen_height * WINDOW_HEIGHT_RATIO)

        # Apply window configuration
        self.root.geometry(f"{window_width}x{window_height}")
        self.root.title(self.window_title)