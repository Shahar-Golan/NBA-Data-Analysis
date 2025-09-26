import os
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from find_path import get_top_players_regular_season_path
from data_processing import load_player_names, get_player_data
from analyze_calculation import (analyze_ast, analyze_ppg, analyze_reb, analyze_wins)
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class OptionsScreen(tk.Frame):
    def __init__(self, parent, season, on_back, colors):
        super().__init__(parent, bg=colors['background'])
        self.parent = parent
        self.season = season
        self.on_back = on_back
        self.colors = colors
        self.hero_images = {}
        
        self.setup_ui()
        self.load_hero_images()

    def setup_ui(self):
        # Main container with padding
        main_container = tk.Frame(self, bg=self.colors['background'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)
        
        # Header section
        self.create_header(main_container)
        
        # Control panel (player selection + stats buttons)
        self.create_control_panel(main_container)
        
        # Visualization area
        self.create_visualization_area(main_container)
        
        # Navigation
        self.create_navigation(main_container)

    def create_header(self, parent):
        header_frame = tk.Frame(parent, bg=self.colors['background'])
        header_frame.pack(fill=tk.X, pady=(0, 25))
        
        # Back button (top-left)
        back_frame = tk.Frame(header_frame, bg=self.colors['background'])
        back_frame.pack(fill=tk.X)
        
        back_button = tk.Button(
            back_frame,
            text=" BACK",
            command=self.on_back,
            bg=self.colors['surface'],
            fg=self.colors['text_secondary'],
            font=("Arial", 10, "bold"),
            relief='flat',
            bd=0,
            padx=20,
            pady=8,
            cursor='hand2'
        )
        back_button.pack(side=tk.LEFT)
        
        # Title section
        title_frame = tk.Frame(header_frame, bg=self.colors['background'], height=120)
        title_frame.pack(fill=tk.X, pady=(20, 0))
        title_frame.pack_propagate(False)
        
        # Hero image
        self.header_image_label = tk.Label(
            title_frame,
            bg=self.colors['background']
        )
        self.header_image_label.pack(side=tk.LEFT, padx=(0, 30))
        
        # Title text
        title_text_frame = tk.Frame(title_frame, bg=self.colors['background'])
        title_text_frame.pack(side=tk.LEFT, fill=tk.Y, expand=True)
        
        season_title = tk.Label(
            title_text_frame,
            text=f"PLAYER ANALYTICS",
            font=("Arial", 28, "bold"),
            fg=self.colors['text_primary'],
            bg=self.colors['background']
        )
        season_title.pack(anchor='w')
        
        season_subtitle = tk.Label(
            title_text_frame,
            text=f"Season {self.season}  Performance Analysis",
            font=("Arial", 14),
            fg=self.colors['text_secondary'],
            bg=self.colors['background']
        )
        season_subtitle.pack(anchor='w')

    def create_control_panel(self, parent):
        # Control panel card
        control_card = tk.Frame(parent, bg=self.colors['surface'], relief='raised', bd=1)
        control_card.pack(fill=tk.X, pady=(0, 25))
        
        control_content = tk.Frame(control_card, bg=self.colors['surface'])
        control_content.pack(fill=tk.X, padx=30, pady=20)
        
        # Player selection section
        player_section = tk.Frame(control_content, bg=self.colors['surface'])
        player_section.pack(fill=tk.X, pady=(0, 20))
        
        player_label = tk.Label(
            player_section,
            text="SELECT PLAYER",
            font=("Arial", 12, "bold"),
            fg=self.colors['text_primary'],
            bg=self.colors['surface']
        )
        player_label.pack(anchor='w', pady=(0, 8))
        
        # Load and display player names dropdown
        player_names = load_player_names(self.season)
        
        self.player_dropdown = ttk.Combobox(
            player_section, 
            values=player_names,
            font=("Arial", 11),
            state="readonly"
        )
        self.player_dropdown.pack(fill=tk.X, ipady=8)
        
        # Stats buttons section
        stats_section = tk.Frame(control_content, bg=self.colors['surface'])
        stats_section.pack(fill=tk.X)
        
        stats_label = tk.Label(
            stats_section,
            text="ANALYSIS OPTIONS",
            font=("Arial", 12, "bold"),
            fg=self.colors['text_primary'],
            bg=self.colors['surface']
        )
        stats_label.pack(anchor='w', pady=(0, 15))
        
        # Create modern stat buttons
        buttons_frame = tk.Frame(stats_section, bg=self.colors['surface'])
        buttons_frame.pack(fill=tk.X)
        
        self.create_stat_button(buttons_frame, "POINTS PER GAME", 
                              lambda: self.show_stat_analysis(analyze_ppg, "Points Per Game"),
                              self.colors['primary'], 0)
        
        self.create_stat_button(buttons_frame, "ASSISTS PER GAME", 
                              lambda: self.show_stat_analysis(analyze_ast, "Assists Per Game"),
                              self.colors['secondary'], 1)
        
        self.create_stat_button(buttons_frame, "REBOUNDS PER GAME", 
                              lambda: self.show_stat_analysis(analyze_reb, "Rebounds Per Game"),
                              '#2e8b57', 2)  # Sea green
        
        self.create_stat_button(buttons_frame, "WINS ANALYSIS", 
                              lambda: self.show_stat_analysis(analyze_wins, "Wins"),
                              '#ff6347', 3)  # Tomato

    def create_stat_button(self, parent, text, command, bg_color, index):
        button = tk.Button(
            parent,
            text=text,
            command=command,
            bg=bg_color,
            fg=self.colors['text_primary'],
            font=("Arial", 11, "bold"),
            relief='flat',
            bd=0,
            padx=20,
            pady=12,
            cursor='hand2'
        )
        button.pack(side=tk.LEFT, padx=(0, 15) if index < 3 else (0, 0), fill=tk.X, expand=True)
        
        # Hover effects
        def on_enter(event):
            button.configure(bg=self.colors['accent'], fg=self.colors['background'])
        
        def on_leave(event):
            button.configure(bg=bg_color, fg=self.colors['text_primary'])
        
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)

    def create_visualization_area(self, parent):
        # Visualization card
        viz_card = tk.Frame(parent, bg=self.colors['surface'], relief='raised', bd=1)
        viz_card.pack(fill=tk.BOTH, expand=True, pady=(0, 25))
        
        # Card header
        card_header = tk.Frame(viz_card, bg=self.colors['surface'])
        card_header.pack(fill=tk.X, padx=30, pady=(20, 0))
        
        viz_title = tk.Label(
            card_header,
            text="DATA VISUALIZATION",
            font=("Arial", 14, "bold"),
            fg=self.colors['text_primary'],
            bg=self.colors['surface']
        )
        viz_title.pack(anchor='w')
        
        # Graph area
        self.graph_frame = tk.Frame(viz_card, bg=self.colors['surface'])
        self.graph_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=(20, 30))
        
        # Initial placeholder
        self.create_placeholder_visualization()

    def create_placeholder_visualization(self):
        placeholder_frame = tk.Frame(self.graph_frame, bg=self.colors['background'])
        placeholder_frame.pack(expand=True)
        
        placeholder_label = tk.Label(
            placeholder_frame,
            text="",
            font=("Arial", 48),
            fg=self.colors['text_secondary'],
            bg=self.colors['background']
        )
        placeholder_label.pack()
        
        instruction_label = tk.Label(
            placeholder_frame,
            text="Select a player and choose an analysis option to view data",
            font=("Arial", 12),
            fg=self.colors['text_secondary'],
            bg=self.colors['background']
        )
        instruction_label.pack(pady=(10, 0))

    def create_navigation(self, parent):
        nav_frame = tk.Frame(parent, bg=self.colors['background'])
        nav_frame.pack(fill=tk.X)

    def load_hero_images(self):
        try:
            # Header image - use Kobe & Shaq for analytics
            header_path = os.path.join(os.path.dirname(__file__), '..', 'assests', 'Kobe & Shaq.jpg')
            if os.path.exists(header_path):
                img = Image.open(header_path)
                img = img.resize((100, 100), Image.Resampling.LANCZOS)
                img = self.make_circular_image(img)
                self.hero_images['header'] = ImageTk.PhotoImage(img)
                self.header_image_label.configure(image=self.hero_images['header'])
        
        except Exception as e:
            print(f"Could not load hero images: {e}")

    def make_circular_image(self, image):
        size = min(image.size)
        mask = Image.new('L', (size, size), 0)
        from PIL import ImageDraw
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, size, size), fill=255)
        
        result = Image.new('RGBA', (size, size))
        result.paste(image.resize((size, size)), (0, 0))
        result.putalpha(mask)
        
        return result

    def show_stat_analysis(self, stat_function, title):
        player_name = self.player_dropdown.get()
        if not player_name:
            messagebox.showerror("Selection Error", "Please select a player.")
            return

        result = stat_function(self.season, player_name)
        if result is not None:
            self.display_plot(result, f"{player_name} - {title}")
        else:
            messagebox.showerror("Data Error", f"No data available for {player_name}.")

    def display_plot(self, data, title):
        # Clear the previous plot
        for widget in self.graph_frame.winfo_children():
            widget.destroy()

        # Create a modern plot
        plt.style.use('dark_background')
        fig, ax = plt.subplots(figsize=(8, 5))
        fig.patch.set_facecolor(self.colors['surface'])
        ax.set_facecolor(self.colors['background'])
        
        # Plot the data with NBA colors
        if isinstance(data, pd.Series):
            bars = ax.bar(data.index, data.values, 
                         color=[self.colors['primary'], self.colors['secondary'], self.colors['accent']])
        elif isinstance(data, np.ndarray):
            bars = ax.bar(range(len(data)), data, 
                         color=[self.colors['primary'], self.colors['secondary'], self.colors['accent']])
        else:
            messagebox.showerror("Data Error", "Unsupported data format for plotting.")
            return

        # Styling
        ax.set_title(title, fontsize=16, fontweight='bold', color=self.colors['text_primary'], pad=20)
        ax.set_xlabel("Tier", fontsize=12, color=self.colors['text_secondary'])
        ax.set_ylabel("Stat Value", fontsize=12, color=self.colors['text_secondary'])
        
        ax.set_xticks([1, 2, 3])
        ax.tick_params(colors=self.colors['text_secondary'])
        ax.grid(True, alpha=0.3, color=self.colors['text_secondary'])
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + height*0.02,
                   f'{height:.1f}', ha='center', va='bottom', 
                   color=self.colors['text_primary'], fontweight='bold')

        plt.tight_layout()

        # Display in tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        plt.close(fig)  # Prevent memory leaks
