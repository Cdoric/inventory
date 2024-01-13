import os
import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
sys.path.append(str(current_dir))
from . import ttk
# import tkinter as tk
# from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x200")

        # Create the Treeview
        self.tree = ttk.Treeview(self, columns=('one', 'two', 'three'), show='headings')
        self.tree.pack(fill='both', expand=True)

        # Create the Table Headings
        self.tree.heading('one', text='Column 1')
        self.tree.heading('two', text='Column 2')
        self.tree.heading('three', text='Column 3')

        # Configure the Treeview columns to have input
        self.tree.column('one', width=100)
        self.tree.column('two', width=100)
        self.tree.column('three', width=100)

        # Create a button for adding a new row
        self.add_row_button = ttk.Button(self, text='Add Row', command=self.add_row)
        self.add_row_button.pack(fill='x', expand=True)

        # Create a button for adding a new column
        self.add_column_button = ttk.Button(self, text='Add Column', command=self.add_column)
        self.add_column_button.pack(fill='x', expand=True)

        # Create a button for deleting a row
        self.delete_row_button = ttk.Button(self, text='Delete Row', command=self.delete_row)
        self.delete_row_button.pack(fill='x', expand=True)

        # Create a button for deleting a column
        self.delete_column_button = ttk.Button(self, text='Delete Column', command=self.delete_column)
        self.delete_column_button.pack(fill='x', expand=True)

    def add_row(self):
        self.tree.insert('', 'end', values=('', '', ''))

    def add_column(self):
        column_name = 'column' + str(len(self.tree['columns']) + 1)
        self.tree['columns'] = self.tree['columns'] + (column_name,)
        self.tree.heading(column_name, text=column_name.capitalize())
        self.tree.column(column_name, width=100)

    def delete_row(self):
        self.tree.delete(self.tree.selection())

    def delete_column(self):
        self.tree['columns'] = self.tree['columns'][:-1]
        self.tree.delete(self.tree.get_children())
        for child in self.tree.get_children():
            values = list(self.tree.item(child)['values'])
            values = values[:-1]
            self.tree.item(child, values=tuple(values))

if __name__ == "__main__":
    app = App()
    app.mainloop()