# import tkinter as tk
# from tkinter import ttk
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.geometry("300x200")
#
#         # Create the Treeview
#         self.tree = ttk.Treeview(self, columns=('one', 'two', 'three'), show='headings')
#         self.tree.pack(fill='both', expand=True)
#
#         # Create the Table Headings
#         self.tree.heading('one', text='Column 1')
#         self.tree.heading('two', text='Column 2')
#         self.tree.heading('three', text='Column 3')
#
#         # Configure the Treeview columns to have input
#         self.tree.column('one', width=100)
#         self.tree.column('two', width=100)
#         self.tree.column('three', width=100)
#
#         # Create an Entry Box
#         self.entry = ttk.Entry(self)
#         self.entry.pack(fill='x', expand=True)
#
#         # Bind the Return key to add a new row with input
#         self.entry.bind('<Return>', self.add_row)
#
#     def add_row(self, event):
#         self.tree.insert('', 'end', values=(self.entry.get(), '', ''))
#         self.entry.delete(0, 'end')
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()