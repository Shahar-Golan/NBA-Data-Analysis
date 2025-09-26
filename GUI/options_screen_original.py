import os
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from find_path import get_top_players_regular_season_path
from data_processing import load_player_names, get_player_data # Import from data_processing
from analyze_calculation import (analyze_ast, analyze_ppg, analyze_reb, analyze_wins)
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg




class OptionsScreen(tk.Frame):
    def __init__(self, parent, season, on_back):
        super().__init__(parent)
        self.parent = parent
        self.season = season
        self.on_back = on_back

        # Title
        tk.Label(self, text=f"Player Analysis for {season}", font=("Helvetica", 16)).pack(pady=10)

        # Load and display player names dropdown
        player_names = load_player_names(season)
        tk.Label(self, text="Select Player:").pack(pady=10)
        self.player_dropdown = ttk.Combobox(self, values=player_names)
        self.player_dropdown.pack(pady=10)

        # Frame for displaying the graph
        self.graph_frame = tk.Frame(self)
        self.graph_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Analysis buttons
        tk.Button(self, text="PPG", command=lambda: self.show_stat_analysis(analyze_ppg, "Points Per Game")).pack(
            side=tk.LEFT, padx=5)
        tk.Button(self, text="AST", command=lambda: self.show_stat_analysis(analyze_ast, "Assists Per Game")).pack(
            side=tk.LEFT, padx=5)
        tk.Button(self, text="REB", command=lambda: self.show_stat_analysis(analyze_reb, "Rebounds Per Game")).pack(
            side=tk.LEFT, padx=5)
        tk.Button(self, text="W's", command=lambda: self.show_stat_analysis(analyze_wins, "Wins")).pack(side=tk.LEFT,
                                                                                                        padx=5)

        # Back button
        back_button = tk.Button(self, text="Back", command=self.on_back)
        back_button.pack(pady=20)

    def show_stat_analysis(self, stat_function, title):
        player_name = self.player_dropdown.get()
        if not player_name:
            tk.messagebox.showerror("Selection Error", "Please select a player.")
            return

        # it gets a function as a parameter and insert
        result = stat_function(self.season, player_name)
        if result is not None:
            # Display the result in a plot
            self.display_plot(result, f"{player_name} - {title}")
        else:
            tk.messagebox.showerror("Data Error", f"No data available for {player_name}.")

    def display_plot(self, data, title):
        # Clear the previous plot, if any
        for widget in self.graph_frame.winfo_children():
            widget.destroy()

        # Create a figure and axis for the plot
        fig, ax = plt.subplots(figsize=(5, 4))
        # Check if data is a numpy array or pandas Series, and handle it accordingly
        if isinstance(data, pd.Series):
            ax.bar(data.index, data.values, color="skyblue")
        elif isinstance(data, np.ndarray):
            ax.bar(range(len(data)), data, color="skyblue")
        else:
            # Fallback if the data type is unexpected
            tk.messagebox.showerror("Data Error", "Unsupported data format for plotting.")
            return

        ax.set_title(title)
        ax.set_xlabel("Tier")
        ax.set_ylabel("Stat Value")

        ax.set_xticks([1,2,3])

        # Display the plot in the tkinter frame
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def show_ppg(self):
        self.show_stat_analysis(analyze_ppg)

    def show_ast(self):
        self.show_stat_analysis(analyze_ast)

    def show_reb(self):
        self.show_stat_analysis(analyze_reb)

    def show_wins(self):
        self.show_stat_analysis(analyze_wins)