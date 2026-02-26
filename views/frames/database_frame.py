"""Database records display frame component.

This module handles the display of invoice records in a table-like format
with columns for company name, bill number, and issue date.
"""

from customtkinter import CTkFrame, CTkLabel
import customtkinter


class DatabaseFrame(customtkinter.CTkScrollableFrame):
    """Scrollable frame for displaying database records.
    
    This frame displays invoice records in a tabular format with three columns:
    - Column 1: Company name
    - Column 2: Invoice number
    - Column 3: Issue date
    """

    # Column configuration
    COLUMN_COUNT = 3

    def __init__(self, master) -> None:
        """Initialize the database frame.
        
        Args:
            master: The parent widget (typically a bill form).
        """
        super().__init__(master, border_color="black", border_width=1)

        self.master = master


        # Pack the database frame into its parent
        self.pack(side="right", fill="both", expand=True)

        # Create header frame for column labels
        # Create header frame for column labels
        self.records_label = CTkFrame(self)
        self.records_label.pack(fill="x", pady=self.master.styles.pady)

        # Create column frames
        self.columns = []
        for _ in range(self.COLUMN_COUNT):
            column = CTkFrame(self.records_label)
            column.pack(
                side="left",
                fill="both",
                expand=True,
                pady=self.master.styles.pady
            )
            self.columns.append(column)

        # Assign columns for easy access
        self.company_name_column = self.columns[0]
        self.bill_number_column = self.columns[1]
        self.issue_date_column = self.columns[2]

        # Legacy attribute names for backward compatibility
        self.first_column = self.company_name_column
        self.second_column = self.bill_number_column
        self.third_column = self.issue_date_column

        # Initialize column headers
        self._initialize_headers()

    def _initialize_headers(self) -> None:
        """Initialize the column header labels."""
        self.company_name_label()
        self.bill_number_label()
        self.issue_date_label()

    def company_name_label(self) -> None:
        """Create the company name column header."""
        label = CTkLabel(self.company_name_column, text="Raison sociale")
        label.pack(anchor="w")

    def bill_number_label(self) -> None:
        """Create the bill number column header."""
        label = CTkLabel(self.bill_number_column, text="N° de facture")
        label.pack(anchor="w")

    def issue_date_label(self) -> None:
        """Create the issue date column header."""
        label = CTkLabel(self.issue_date_column, text="Date d'émission")
        label.pack(anchor="w")
        