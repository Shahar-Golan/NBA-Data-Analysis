import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
from machine_learning_screen import MachineLearningScreen
from season_selection import SeasonSelectionScreen
from options_screen import OptionsScreen

class NBAApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("NBA Data Analysis - Professional Analytics Platform")
        self.geometry("1200x900")
        self.configure(bg='#1a1a2e')  # Dark blue background
        
        # Set modern style
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Configure colors
        self.colors = {
            'primary': '#c9302c',      # NBA red
            'secondary': '#0f3460',    # NBA blue
            'background': '#1a1a2e',   # Dark background
            'surface': '#16213e',      # Card background
            'text_primary': '#ffffff',  # White text
            'text_secondary': '#b0b0b0', # Gray text
            'accent': '#ffd700'        # Gold accent
        }
        
        # Load and set up background
        self.setup_background()
        
        self.current_screen = None
        self.show_season_selection()

    def setup_background(self):
        try:
            bg_path = os.path.join(os.path.dirname(__file__), '..', 'assests', 'nba-logo-design.webp')
            if os.path.exists(bg_path):
                bg_image = Image.open(bg_path)
                bg_image = bg_image.resize((200, 200), Image.Resampling.LANCZOS)
                bg_image = bg_image.convert("RGBA")
                
                data = bg_image.getdata()
                new_data = []
                for item in data:
                    if item[3] > 0:
                        new_data.append((item[0], item[1], item[2], 30))
                    else:
                        new_data.append(item)
                bg_image.putdata(new_data)
                
                self.bg_photo = ImageTk.PhotoImage(bg_image)
            else:
                self.bg_photo = None
        except Exception as e:
            print(f"Could not load background image: {e}")
            self.bg_photo = None

    def show_season_selection(self):
        if self.current_screen:
            self.current_screen.pack_forget()
        self.current_screen = SeasonSelectionScreen(self, self.show_options_screen, self.colors, self.bg_photo)
        self.current_screen.pack(fill=tk.BOTH, expand=True)

    def show_options_screen(self, season, option_type):
        if self.current_screen:
            self.current_screen.pack_forget()
        if option_type == "analytics":
            self.current_screen = OptionsScreen(self, season, self.show_season_selection, self.colors)
        elif option_type == "ml":
            self.current_screen = MachineLearningScreen(self, season, self.show_season_selection, self.colors)
        self.current_screen.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    app = NBAApp()
    app.mainloop()
