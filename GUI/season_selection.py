import os
import tkinter as tk
from tkinter import ttk

class SeasonSelectionScreen(tk.Frame):
    def __init__(self, parent, on_select_option):
        super().__init__(parent)
        self.parent = parent
        self.on_select_option = on_select_option
        self.selected_season = tk.StringVar()

        tk.Label(self, text="Select Season:").pack(pady=10)


        self.season_dropdown = ttk.Combobox(self, textvariable=self.selected_season)
        self.season_dropdown['values'] = self.get_seasons()
        self.season_dropdown.pack(pady=10)

        # Buttons for Player Analytics and Machine Learning Analysis
        self.analytics_button = tk.Button(self, text="Player Analytics", command=self.go_to_player_analytics)
        self.analytics_button.pack(pady=5)

        self.ml_button = tk.Button(self, text="Machine Learning Analysis", command=self.go_to_machine_learning)
        self.ml_button.pack(pady=5)


    def get_seasons(self):
        # returns available seasons from the directory
        base_path = r"C:\Users\Shahar Golan\PycharmProjects\NBA\All_Seasons"
        return sorted([folder for folder in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, folder))])

    def go_to_player_analytics(self):
        season = self.season_dropdown.get()
        if season:
            self.on_select_option(season, "analytics")
        else:
            tk.messagebox.showwarning("Selection Error", "Please select a season.")

    def go_to_machine_learning(self):
        season = self.season_dropdown.get()
        if season:
            self.on_select_option(season, "ml")
        else:
            tk.messagebox.showwarning("Selection Error", "Please select a season.")




