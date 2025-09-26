import os
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class SeasonSelectionScreen(tk.Frame):
    def __init__(self, parent, on_select_option, colors, bg_photo):
        super().__init__(parent, bg=colors['background'])
        self.parent = parent
        self.on_select_option = on_select_option
        self.colors = colors
        self.bg_photo = bg_photo
        self.selected_season = tk.StringVar()
        self.hero_images = {}
        
        self.setup_ui()
        self.load_hero_images()

    def setup_ui(self):
        main_container = tk.Frame(self, bg=self.colors['background'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=40, pady=20)
        
        header_frame = tk.Frame(main_container, bg=self.colors['background'], height=200)
        header_frame.pack(fill=tk.X, pady=(0, 30))
        header_frame.pack_propagate(False)
        
        if self.bg_photo:
            bg_label = tk.Label(header_frame, image=self.bg_photo, bg=self.colors['background'])
            bg_label.place(relx=1.0, rely=0.0, anchor='ne')
        
        title_label = tk.Label(
            header_frame, 
            text="NBA DATA ANALYSIS", 
            font=("Arial", 32, "bold"),
            fg=self.colors['text_primary'],
            bg=self.colors['background']
        )
        title_label.pack(pady=(50, 10))
        
        subtitle_label = tk.Label(
            header_frame,
            text="Professional Basketball Analytics Platform",
            font=("Arial", 14),
            fg=self.colors['text_secondary'],
            bg=self.colors['background']
        )
        subtitle_label.pack()
        
        content_frame = tk.Frame(main_container, bg=self.colors['background'])
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        self.create_season_card(content_frame)
        self.create_option_cards(content_frame)
    
    def create_season_card(self, parent):
        season_card = tk.Frame(parent, bg=self.colors['surface'], relief='raised', bd=1)
        season_card.pack(fill=tk.X, pady=(0, 30), padx=20)
        
        card_content = tk.Frame(season_card, bg=self.colors['surface'])
        card_content.pack(fill=tk.X, padx=30, pady=25)
        
        season_title = tk.Label(
            card_content,
            text="SELECT SEASON",
            font=("Arial", 16, "bold"),
            fg=self.colors['text_primary'],
            bg=self.colors['surface']
        )
        season_title.pack(pady=(0, 15))
        
        dropdown_frame = tk.Frame(card_content, bg=self.colors['surface'])
        dropdown_frame.pack(fill=tk.X)
        
        self.season_dropdown = ttk.Combobox(
            dropdown_frame, 
            textvariable=self.selected_season,
            font=("Arial", 12),
            state="readonly"
        )
        self.season_dropdown['values'] = self.get_seasons()
        self.season_dropdown.pack(pady=10, ipady=8, fill=tk.X)
        
        if self.season_dropdown['values']:
            self.season_dropdown.set(self.season_dropdown['values'][-1])
    
    def create_option_cards(self, parent):
        options_container = tk.Frame(parent, bg=self.colors['background'])
        options_container.pack(fill=tk.BOTH, expand=True, padx=20)
        
        cards_frame = tk.Frame(options_container, bg=self.colors['background'])
        cards_frame.pack(expand=True)
        
        self.create_analytics_card(cards_frame)
        self.create_ml_card(cards_frame)
    
    def create_analytics_card(self, parent):
        analytics_card = tk.Frame(parent, bg=self.colors['surface'], relief='raised', bd=1)
        analytics_card.pack(side=tk.LEFT, padx=(0, 15), pady=20, fill=tk.BOTH, expand=True)
        
        card_content = tk.Frame(analytics_card, bg=self.colors['surface'])
        card_content.pack(fill=tk.BOTH, expand=True, padx=25, pady=25)
        
        self.analytics_image_label = tk.Label(
            card_content,
            text="",
            font=("Arial", 48),
            fg=self.colors['accent'],
            bg=self.colors['surface']
        )
        self.analytics_image_label.pack(pady=(0, 20))
        
        title = tk.Label(
            card_content,
            text="PLAYER ANALYTICS",
            font=("Arial", 18, "bold"),
            fg=self.colors['text_primary'],
            bg=self.colors['surface']
        )
        title.pack(pady=(0, 10))
        
        description = tk.Label(
            card_content,
            text="Deep dive into player performance stats and insights",
            font=("Arial", 11),
            fg=self.colors['text_secondary'],
            bg=self.colors['surface'],
            justify=tk.CENTER
        )
        description.pack(pady=(0, 25))
        
        self.analytics_button = self.create_modern_button(
            card_content,
            "START ANALYTICS",
            self.go_to_player_analytics,
            self.colors['primary']
        )
    
    def create_ml_card(self, parent):
        ml_card = tk.Frame(parent, bg=self.colors['surface'], relief='raised', bd=1)
        ml_card.pack(side=tk.LEFT, padx=(15, 0), pady=20, fill=tk.BOTH, expand=True)
        
        card_content = tk.Frame(ml_card, bg=self.colors['surface'])
        card_content.pack(fill=tk.BOTH, expand=True, padx=25, pady=25)
        
        self.ml_image_label = tk.Label(
            card_content,
            text="",
            font=("Arial", 48),
            fg=self.colors['accent'],
            bg=self.colors['surface']
        )
        self.ml_image_label.pack(pady=(0, 20))
        
        title = tk.Label(
            card_content,
            text="MACHINE LEARNING",
            font=("Arial", 18, "bold"),
            fg=self.colors['text_primary'],
            bg=self.colors['surface']
        )
        title.pack(pady=(0, 10))
        
        description = tk.Label(
            card_content,
            text="AI-driven predictive modeling and forecasting",
            font=("Arial", 11),
            fg=self.colors['text_secondary'],
            bg=self.colors['surface'],
            justify=tk.CENTER
        )
        description.pack(pady=(0, 25))
        
        self.ml_button = self.create_modern_button(
            card_content,
            "START ML ANALYSIS",
            self.go_to_machine_learning,
            self.colors['secondary']
        )
    
    def create_modern_button(self, parent, text, command, bg_color):
        button_frame = tk.Frame(parent, bg=self.colors['surface'])
        button_frame.pack(fill=tk.X)
        
        button = tk.Button(
            button_frame,
            text=text,
            command=command,
            bg=bg_color,
            fg=self.colors['text_primary'],
            font=("Arial", 12, "bold"),
            relief='flat',
            bd=0,
            pady=12,
            cursor='hand2'
        )
        button.pack(fill=tk.X)
        
        def on_enter(event):
            button.configure(bg=self.colors['accent'], fg=self.colors['background'])
        
        def on_leave(event):
            button.configure(bg=bg_color, fg=self.colors['text_primary'])
        
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
        
        return button
    
    def load_hero_images(self):
        try:
            analytics_path = os.path.join(os.path.dirname(__file__), '..', 'assests', 'Air Jordan.jpg')
            if os.path.exists(analytics_path):
                img = Image.open(analytics_path)
                img = img.resize((120, 120), Image.Resampling.LANCZOS)
                img = self.make_circular_image(img)
                self.hero_images['analytics'] = ImageTk.PhotoImage(img)
                self.analytics_image_label.configure(image=self.hero_images['analytics'], text="")
            
            ml_path = os.path.join(os.path.dirname(__file__), '..', 'assests', "Lebron's block.jpg")
            if os.path.exists(ml_path):
                img = Image.open(ml_path)
                img = img.resize((120, 120), Image.Resampling.LANCZOS)
                img = self.make_circular_image(img)
                self.hero_images['ml'] = ImageTk.PhotoImage(img)
                self.ml_image_label.configure(image=self.hero_images['ml'], text="")
        
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

    def get_seasons(self):
        base_path = r"C:\Users\Shahar Golan\PycharmProjects\NBA\All_Seasons"
        try:
            return sorted([folder for folder in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, folder))])
        except:
            return ["2000-01", "2001-02", "2002-03", "2003-04", "2004-05", "2005-06"]

    def go_to_player_analytics(self):
        season = self.season_dropdown.get()
        if season:
            self.on_select_option(season, "analytics")
        else:
            messagebox.showwarning("Selection Error", "Please select a season.")

    def go_to_machine_learning(self):
        season = self.season_dropdown.get()
        if season:
            self.on_select_option(season, "ml")
        else:
            messagebox.showwarning("Selection Error", "Please select a season.")
