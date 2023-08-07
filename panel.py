# panel.py

import tkinter as tk
import webbrowser


class Panel:
    def __init__(self, root):
        self.entry = tk.Entry(root)
        self.entry.pack()

        self.button = tk.Button(root, text="Look up", command=self.lookup_word)
        self.button.pack()

        self.entry.bind("<Return>", lambda event: self.lookup_word())

        # This will set the focus to the text entry field
        self.entry.focus_set()

    def lookup_word(self):
        # This function will be called when the button is clicked.
        # It opens the Google dictionary page for the word the user has entered.
        word = self.entry.get()
        url = "https://www.google.com/search?q=define+" + word
        webbrowser.open_new(url)

