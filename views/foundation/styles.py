"""Styling configuration for the invoice application.

This module contains all UI styling constants and configuration
for consistency across the application.
"""


class UIStyles:
    """Centralized styling configuration for the application UI.
    
    This class defines all styling parameters for frames, entries,
    labels, and other UI elements to ensure visual consistency.
    """

    # Padding configuration
    PADDING_X = 2
    PADDING_Y = 2

    # Frame styling
    FRAME_FOREGROUND_COLOR = "yellow"
    FRAME_BORDER_WIDTH = 0
    FRAME_BORDER_COLOR = "black"

    # Entry widget styling
    ENTRY_WIDTH = 150
    ENTRY_HEIGHT = 30

    # Text wrapping for database labels
    LABEL_WRAP_LENGTH = 100

    def __init__(self) -> None:
        """Initialize the UI styles configuration."""
        # Create instance attributes from class constants for compatibility
        self.padx = self.PADDING_X
        self.pady = self.PADDING_Y
        self.frame_fg_color = self.FRAME_FOREGROUND_COLOR
        self.frame_border_width = self.FRAME_BORDER_WIDTH
        self.frame_border_color = self.FRAME_BORDER_COLOR
        self.entry_width = self.ENTRY_WIDTH
        self.entry_height = self.ENTRY_HEIGHT
        self.wraplength = self.LABEL_WRAP_LENGTH


# Legacy alias for backward compatibility
Styles = UIStyles
        