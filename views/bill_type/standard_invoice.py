"""Standard invoice form implementation.

This module contains the form for standard (regular) invoices with specific
fields for result date, address, product references, and invoice details.
"""

from customtkinter import CTkFrame, CTkLabel, CTkEntry

import views.foundation.form_model as form_model
import fake_data


class StandardInvoice(form_model.InvoiceFormModel):
    """Standard invoice form implementation.
    
    This class extends the base invoice form with fields specific to
    standard invoices including result date, address, and product references.
    """

    def __init__(self, master) -> None:
        """Initialize the standard invoice form.
        
        Adds specific fields for standard invoices and displays sample records.
        
        Args:
            master: The parent widget (typically HeadFrame).
        """
        super().__init__(master)

        # Add standard invoice specific form fields
        self._add_form_fields()

        # Display invoice records from sample data
        records = fake_data.records
        self.display_database_records(records)

    def _add_form_fields(self) -> None:
        """Add all standard invoice specific form fields."""
        self.create_result_date_field()
        self.create_address_field()
        self.create_product_reference_field()
        self.create_issue_date_field()
        self.create_bill_number_field()

    def create_result_date_field(self) -> None:
        """Create the result date input field in the right column."""
        label = CTkLabel(self.client_form.right_frame, text="Date de résultat")
        label.pack(anchor="w")

        self.result_date_input = CTkEntry(
            self.client_form.right_frame,
            width=self.master.styles.entry_width,
            height=self.master.styles.entry_height
        )
        self.result_date_input.pack(anchor="w")

    def create_address_field(self) -> None:
        """Create the company address input field in the left column."""
        label = CTkLabel(self.client_form.left_frame, text="Adresse")
        label.pack(anchor="w")

        self.address_input = CTkEntry(
            self.client_form.left_frame,
            width=self.master.styles.entry_width,
            height=self.master.styles.entry_height
        )
        self.address_input.pack(anchor="w")

    def create_product_reference_field(self) -> None:
        """Create the product reference input field in the right column."""
        label = CTkLabel(self.client_form.right_frame, text="Réf produits")
        label.pack(anchor="w")

        self.product_reference_input = CTkEntry(
            self.client_form.right_frame,
            width=self.master.styles.entry_width,
            height=self.master.styles.entry_height
        )
        self.product_reference_input.pack(anchor="w")

    def create_issue_date_field(self) -> None:
        """Create the issue date input field in the right column."""
        label = CTkLabel(self.client_form.right_frame, text="Date d'émission")
        label.pack(anchor="w")

        self.issue_date_input = CTkEntry(
            self.client_form.right_frame,
            width=self.master.styles.entry_width,
            height=self.master.styles.entry_height
        )
        self.issue_date_input.pack(anchor="w")

    def create_bill_number_field(self) -> None:
        """Create the bill number label in the left column."""
        label = CTkLabel(self.client_form.left_frame, text="N° de facture")
        label.pack(anchor="w")

    def display_database_records(self, records: list) -> None:
        """Display invoice records in the database section.
        
        Args:
            records: List of invoice records to display.
                    Each record should be [company_name, bill_number, issue_date].
        """
        # Clear previous records while keeping the header
        self._clear_records()

        if not records:
            self._show_empty_message()
        else:
            self._display_record_rows(records)

    def _clear_records(self) -> None:
        """Clear all record rows from the database frame."""
        for widget in self.database_records.winfo_children():
            if widget != self.database_records.records_label:
                widget.destroy()

    def _show_empty_message(self) -> None:
        """Display a message when no records are available."""
        message = CTkLabel(
            self.database_records,
            text="Aucun enregistrement trouvé."
        )
        message.pack(pady=self.master.styles.pady)

    def _display_record_rows(self, records: list) -> None:
        """Display all invoice records as rows.
        
        Args:
            records: List of invoice records to display.
        """
        for record in records:
            self._create_record_row(record)

    def _create_record_row(self, record: list) -> None:
        """Create a single row for a record.
        
        Args:
            record: Invoice record data [company_name, bill_number, issue_date].
        """
        # Create row container
        record_frame = CTkFrame(self.database_records)
        record_frame.pack(fill="x", pady=self.master.styles.pady)

        # Create columns for the row
        columns = self._create_row_columns(record_frame, 3)

        # Populate columns with record data
        company_label = CTkLabel(
            columns[0],
            text=record[0],
            wraplength=self.master.styles.wraplength
        )
        company_label.pack(anchor="w")

        bill_number_label = CTkLabel(
            columns[1],
            text=record[1],
            wraplength=self.master.styles.wraplength
        )
        bill_number_label.pack(anchor="w")

        date_label = CTkLabel(
            columns[2],
            text=record[2],
            wraplength=self.master.styles.wraplength
        )
        date_label.pack(anchor="w")

    def _create_row_columns(self, parent_frame, column_count: int) -> list:
        """Create column frames for a record row.
        
        Args:
            parent_frame: The parent frame for columns.
            column_count: Number of columns to create.
            
        Returns:
            List of column frame widgets.
        """
        columns = []
        for _ in range(column_count):
            column = CTkFrame(parent_frame, width=100)
            column.pack(
                side="left",
                fill="both",
                expand=True,
                pady=self.master.styles.pady
            )
            columns.append(column)
        return columns
