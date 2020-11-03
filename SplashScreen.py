#===========================
# Imports
#===========================

import tkinter as tk
from tkinter import ttk, colorchooser as cc, Menu, Spinbox as sb, scrolledtext as st, messagebox as mb, filedialog as fd

#===========================
# Main Component
#===========================

class SplashScreen(tk.Toplevel):
    """
    Provides loading screen functionality for the main/widget application.
    :param parent: main application screen.
    """
    #------------------------------------------
    # Initializer
    #------------------------------------------
    def __init__(self, widget):
        super().__init__()
        self.widget = widget

        self.init_vars()
        self.init_UI()
        self.init_methods()
        self.init_config()

    #------------------------------------------
    # Instance Variables
    #------------------------------------------
    def init_vars(self):
        self.text_percentage = self.min_percentage = self.max_percentage = 0

    #------------------------------------------
    # Load Methods
    #------------------------------------------
    def init_methods(self):
        self.load_text()
        self.load_progressbar()

    #-------------------------------------------
    # Window Settings
    #-------------------------------------------
    def init_config(self):
        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        self.overrideredirect(1)
        self.geometry(self.center_window())
        self.config(cursor='wait')

    #-------------------------------------------
    # Widgets
    #-------------------------------------------
    def init_UI(self):
        self.frame = ttk.Frame(self)
        self.frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.load = ttk.Label(self.frame, text=f'Loading... {self.text_percentage}%')
        self.load.pack(pady=(15, 10))

        self.progressbar = ttk.Progressbar(self.frame, orient=tk.HORIZONTAL, length=500, mode='determinate')
        self.progressbar.pack(padx=10, pady=(5, 10))

    # INSTANCE ---------------------------------------
    def load_progressbar(self):
        self.progressbar['value'] = 0
        self.progressbar['maximum'] = 100
        self.max_percentage = 100
        self.read_percentage()

    def read_percentage(self):
        """Simulate loading progress bar; update progress bar."""
        self.min_percentage += 5
        self.progressbar['value'] = self.min_percentage

        if self.min_percentage < self.max_percentage:
            self.after(100, self.read_percentage)

    def load_text(self):
        self.text_percentage += 5
        self.load.config(text=f'Loading... {self.text_percentage}%')
        self.read_text()

    def read_text(self):
        """Simulate reading text; update label text."""
        if self.text_percentage == 100:
            self.destroy()
            self.widget.deiconify() # show window
            return
        else:
            self.widget.after(100, self.load_text)

    #--------------------------------------------
    def current_window_size(self):
        """Get the updated current size of this widget."""
        self.update()
        height_of_window = self.winfo_height()
        width_of_window = self.winfo_width()

        return (height_of_window, width_of_window)

    def current_screen_size(self):
        """Get the current dimension of the screen."""
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        return (screen_width, screen_height)

    def center_window(self):
        """Center this tkinter window."""
        height_of_window, width_of_window = self.current_window_size()
        screen_width, screen_height = self.current_screen_size()

        x_coordinate = (screen_width / 2) - (width_of_window / 2)
        y_coordinate = (screen_height / 2) - (height_of_window / 2)

        return f'{int(width_of_window)}x{int(height_of_window)}+{int(x_coordinate)}+{int(y_coordinate)}'


#===========================
# Test Main App
#===========================

class App(tk.Tk):
    """Main Application."""

    def __init__(self):
        super().__init__()

        # TO USE THE COMPONENT ++++++++++++++++++++
        self.withdraw() # hide window
        splash_screen = SplashScreen(self)
        # +++++++++++++++++++++++++++++++++++++++++

        self.init_config()
        self.init_UI()

    def init_config(self):
        self.title('template')

    def init_UI(self):
        self.frame = ttk.Frame(self)
        self.frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

#===========================
# Start GUI
#===========================

def main():
    app = App().mainloop()

if __name__ == '__main__':
    main()