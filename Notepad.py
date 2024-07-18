import tkinter as tk
from tkinter import filedialog, messagebox

import tkinter as tk

from tkinter import filedialog, scrolledtext, Menu


class NoteApp:

    def __init__(self, root):

        self.root = root

        self.root.title("Note App")

        self.root.geometry("800x600")

        self.text_area = scrolledtext.ScrolledText(self.root, font=("Arial", 12))

        self.text_area.pack(fill=tk.BOTH, expand=True)

        self.menu_bar = Menu(self.root)

        self.file_menu = Menu(self.menu_bar, tearoff=0)

        self.file_menu.add_command(label="New", command=self.new_note)

        self.file_menu.add_command(label="Open", command=self.open_note)

        self.file_menu.add_command(label="Save", command=self.save_note)

        self.file_menu.add_separator()

        self.file_menu.add_command(label="Exit", command=self.root.quit)

        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        self.edit_menu = Menu(self.menu_bar, tearoff=0)

        self.edit_menu.add_command(label="Cut", command=self.cut_text)

        self.edit_menu.add_command(label="Copy", command=self.copy_text)

        self.edit_menu.add_command(label="Paste", command=self.paste_text)

        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)

        self.view_menu = Menu(self.menu_bar, tearoff=0)

        self.view_menu.add_command(label="Dark Mode", command=self.toggle_dark_mode)

        self.menu_bar.add_cascade(label="View", menu=self.view_menu)

        self.tools_menu = Menu(self.menu_bar, tearoff=0)

        self.tools_menu.add_command(label="Italic", command=self.syntax_highlighting)
        self.tools_menu.add_command(label="Bold", command=self.syntax_highlighting)
        self.tools_menu.add_command(label="Underline", command=self.syntax_highlighting)

        self.menu_bar.add_cascade(label="Tools", menu=self.tools_menu)

        self.root.config(menu=self.menu_bar)

        self.is_dark_mode = False

    def new_note(self):

        self.text_area.delete("1.0", tk.END)

    def open_note(self):

        file_path = filedialog.askopenfilename(filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))

        if file_path:
            with open(file_path, "r") as file:
                self.text_area.delete("1.0", tk.END)

                self.text_area.insert(tk.END, file.read())

    def save_note(self):

        content = self.text_area.get("1.0", tk.END)

        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))

        if file_path:
            with open(file_path, "w") as file:
                file.write(content)

            messagebox.showinfo("Note Saved", "The note has been saved successfully.")

    def cut_text(self):

        self.text_area.event_generate("<<Cut>>")

    def copy_text(self):

        self.text_area.event_generate("<<Copy>>")

    def paste_text(self):

        self.text_area.event_generate("<<Paste>>")

    def toggle_dark_mode(self):

        if self.is_dark_mode:

            self.text_area.config(bg="white", fg="black")

            self.is_dark_mode = False

        else:

            self.text_area.config(bg="black", fg="white")

            self.is_dark_mode = True

    def syntax_highlighting(self):

        content = self.text_area.get("1.0", tk.END)

        # Implement syntax highlighting logic here

# Create the Tkinter root window

root = tk.Tk()

note_app = NoteApp(root)

root.mainloop()
