"""Application menu bar component.

This module contains the menu bar with file operations and theme selection.
"""

import customtkinter
from CTkMenuBar import CTkMenuBar, CustomDropdownMenu


class ApplicationMenuBar(CTkMenuBar):
    """Application menu bar with file and theme options.
    
    This class creates the menu bar with the following menus:
    - File: New document, Print options
    - Theme: Light/Dark mode selection
    """

    def __init__(self, master, **kwargs) -> None:
        """Initialize the application menu bar.
        
        Args:
            master: The root application instance.
            **kwargs: Additional keyword arguments for CTkMenuBar.
        """
        super().__init__(master, **kwargs)

        self._initialize_file_menu(master)
        self._initialize_theme_menu(master)

    def _initialize_file_menu(self, master) -> None:
        """Initialize the File menu with document operations.
        
        Args:
            master: The root application instance.
        """
        file_menu = self.add_cascade(text="Fichier")
        file_dropdown = CustomDropdownMenu(widget=file_menu, master=master)

        # New document submenu
        new_submenu = file_dropdown.add_submenu("Nouveau")
        new_submenu.add_option(
            option="Facture normale",
            command=lambda: master.main_frame.head_frame.display_regular_bill()
        )
        new_submenu.add_option(
            option="Facture proforma",
            command=lambda: master.main_frame.head_frame.display_proforma_bill()
        )

        file_dropdown.add_separator()

        # Print submenu
        print_submenu = file_dropdown.add_submenu("Imprimer")
        print_submenu.add_option(option="Facture normale")
        print_submenu.add_option(option="Facture proforma")
        print_submenu.add_option(option="Certification")

    def _initialize_theme_menu(self, master) -> None:
        """Initialize the Theme menu with appearance mode options.
        
        Args:
            master: The root application instance.
        """
        theme_menu = self.add_cascade(text="Thème")
        theme_dropdown = CustomDropdownMenu(widget=theme_menu, master=master)

        theme_dropdown.add_option(
            option="Clair",
            command=lambda: customtkinter.set_appearance_mode("light")
        )
        theme_dropdown.add_option(
            option="Sombre",
            command=lambda: customtkinter.set_appearance_mode("dark")
        )


# Legacy alias for backward compatibility
MenuBar = ApplicationMenuBar