"""Client information form frame component.

This module contains the form for entering client/company information
including company name, NIF, statistical information, and responsible person.
"""

from customtkinter import CTkFrame, CTkLabel, CTkEntry


class ClientFormFrame(CTkFrame):
    """Form frame for client information input.
    
    This frame contains input fields for company details:
    - Company name
    - NIF (Tax ID)
    - Statistical information
    - Responsible person
    """

    def __init__(self, master) -> None:
        """Initialize the client form frame.
        
        Args:
            master: The parent widget (typically a bill form).
        """
        super().__init__(master)

        self.master = master

        # Create left column for form fields
        self.left_frame = CTkFrame(self)
        self.left_frame.pack(
            side="left",
            fill="both",
            expand=True,
            pady=self.master.styles.pady
        )

        # Create right column for form fields
        self.right_frame = CTkFrame(self)
        self.right_frame.pack(
            side="right",
            fill="both",
            expand=True,
            pady=self.master.styles.pady
        )


        # Pack the form into its parent
        self.pack(
            side="left",
            fill="both",
            expand=True,
            pady=self.master.styles.pady
        )

        # Store input references for data access
        # Store input references for data access
        self.company_name_input = None
        self.nif_input = None
        self.statistic_input = None
        self.responsible_input = None

    def company_name_frame(self) -> None:
        """Create the company name input field."""
        label = CTkLabel(self.left_frame, text="Raison sociale")
        label.pack(anchor="w")

        self.company_name_input = CTkEntry(
            self.left_frame,
            width=self.master.styles.entry_width,
            height=self.master.styles.entry_height
        )
        self.company_name_input.pack(anchor="w")

    def nif_frame(self) -> None:
        """Create the NIF (Tax ID) input field."""
        label = CTkLabel(self.left_frame, text="NIF")
        label.pack(anchor="w")

        self.nif_input = CTkEntry(
            self.left_frame,
            width=self.master.styles.entry_width,
            height=self.master.styles.entry_height
        )
        self.nif_input.pack(anchor="w")

    def statistic_frame(self) -> None:
        """Create the statistical information input field."""
        label = CTkLabel(self.left_frame, text="Statistique")
        label.pack(anchor="w")

        self.statistic_input = CTkEntry(
            self.left_frame,
            width=self.master.styles.entry_width,
            height=self.master.styles.entry_height
        )
        self.statistic_input.pack(anchor="w")

    def responsible_frame(self) -> None:
        """Create the responsible person input field."""
        label = CTkLabel(self.right_frame, text="Responsable")
        label.pack(anchor="w")

        self.responsible_input = CTkEntry(
            self.right_frame,
            width=self.master.styles.entry_width,
            height=self.master.styles.entry_height
        )
        self.responsible_input.pack(anchor="w")
        
    