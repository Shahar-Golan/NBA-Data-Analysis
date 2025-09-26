import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sys
import os

# Add parent directory to Python path to access Machine_Learning module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Machine_Learning.model_training import run_machine_learning_model


class MachineLearningScreen(tk.Frame):
    def __init__(self, parent, season, on_back, colors):
        super().__init__(parent, bg=colors['background'])
        self.parent = parent
        self.season = season
        self.on_back = on_back
        self.colors = colors
        self.hero_images = {}
        self.current_results = {}
        
        self.setup_ui()
        self.load_hero_images()

    def setup_ui(self):
        # Main container with padding
        main_container = tk.Frame(self, bg=self.colors['background'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)
        
        # Header section
        self.create_header(main_container)
        
        # Model selection panel
        self.create_model_panel(main_container)
        
        # Results visualization area
        self.create_results_area(main_container)
        
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
            text=f"MACHINE LEARNING ANALYSIS",
            font=("Arial", 28, "bold"),
            fg=self.colors['text_primary'],
            bg=self.colors['background']
        )
        season_title.pack(anchor='w')
        
        season_subtitle = tk.Label(
            title_text_frame,
            text=f"Season {self.season}  AI-Powered Predictive Modeling",
            font=("Arial", 14),
            fg=self.colors['text_secondary'],
            bg=self.colors['background']
        )
        season_subtitle.pack(anchor='w')

    def create_model_panel(self, parent):
        # Model selection card
        model_card = tk.Frame(parent, bg=self.colors['surface'], relief='raised', bd=1)
        model_card.pack(fill=tk.X, pady=(0, 25))
        
        model_content = tk.Frame(model_card, bg=self.colors['surface'])
        model_content.pack(fill=tk.X, padx=30, pady=20)
        
        # Section title
        model_title = tk.Label(
            model_content,
            text="SELECT MACHINE LEARNING MODEL",
            font=("Arial", 16, "bold"),
            fg=self.colors['text_primary'],
            bg=self.colors['surface']
        )
        model_title.pack(pady=(0, 20))
        
        # Model buttons grid
        models_frame = tk.Frame(model_content, bg=self.colors['surface'])
        models_frame.pack(fill=tk.X)
        
        # Define models with their colors and descriptions
        models = [
            {
                "name": "Logistic Regression",
                "code": "logistic_regression",
                "color": self.colors['primary'],
                "desc": "Linear classification model",
                "icon": ""
            },
            {
                "name": "Support Vector Machine",
                "code": "svm_model",
                "color": self.colors['secondary'],
                "desc": "Powerful margin-based classifier",
                "icon": ""
            },
            {
                "name": "Random Forest",
                "code": "random_forest_model",
                "color": "#2e8b57",  # Sea green
                "desc": "Ensemble tree-based method",
                "icon": ""
            },
            {
                "name": "Naive Bayes",
                "code": "naive_bayes_model",
                "color": "#ff6347",  # Tomato
                "desc": "Probabilistic classifier",
                "icon": ""
            }
        ]
        
        # Create model cards in 2x2 grid
        for i, model in enumerate(models):
            row = i // 2
            col = i % 2
            
            self.create_model_card(models_frame, model, row, col)

    def create_model_card(self, parent, model, row, col):
        # Create model card
        card_frame = tk.Frame(parent, bg=self.colors['background'], padx=10, pady=10)
        card_frame.grid(row=row, column=col, sticky='ew', padx=(0, 15) if col == 0 else (15, 0))
        
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_columnconfigure(1, weight=1)
        
        model_card = tk.Frame(card_frame, bg=self.colors['surface'], relief='raised', bd=1)
        model_card.pack(fill=tk.BOTH, expand=True)
        
        card_content = tk.Frame(model_card, bg=self.colors['surface'])
        card_content.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Icon
        icon_label = tk.Label(
            card_content,
            text=model['icon'],
            font=("Arial", 24),
            fg=model['color'],
            bg=self.colors['surface']
        )
        icon_label.pack(pady=(0, 10))
        
        # Model name
        name_label = tk.Label(
            card_content,
            text=model['name'],
            font=("Arial", 12, "bold"),
            fg=self.colors['text_primary'],
            bg=self.colors['surface']
        )
        name_label.pack(pady=(0, 5))
        
        # Description
        desc_label = tk.Label(
            card_content,
            text=model['desc'],
            font=("Arial", 9),
            fg=self.colors['text_secondary'],
            bg=self.colors['surface']
        )
        desc_label.pack(pady=(0, 15))
        
        # Run button
        run_button = tk.Button(
            card_content,
            text="RUN MODEL",
            command=lambda: self.run_model(model['code'], model['name']),
            bg=model['color'],
            fg=self.colors['text_primary'],
            font=("Arial", 10, "bold"),
            relief='flat',
            bd=0,
            pady=8,
            cursor='hand2'
        )
        run_button.pack(fill=tk.X)
        
        # Hover effects
        def on_enter(event, btn=run_button, color=model['color']):
            btn.configure(bg=self.colors['accent'], fg=self.colors['background'])
        
        def on_leave(event, btn=run_button, color=model['color']):
            btn.configure(bg=color, fg=self.colors['text_primary'])
        
        run_button.bind("<Enter>", on_enter)
        run_button.bind("<Leave>", on_leave)

    def create_results_area(self, parent):
        # Results card
        results_card = tk.Frame(parent, bg=self.colors['surface'], relief='raised', bd=1)
        results_card.pack(fill=tk.BOTH, expand=True, pady=(0, 25))
        
        # Card header
        card_header = tk.Frame(results_card, bg=self.colors['surface'])
        card_header.pack(fill=tk.X, padx=30, pady=(20, 0))
        
        results_title = tk.Label(
            card_header,
            text="MODEL RESULTS",
            font=("Arial", 14, "bold"),
            fg=self.colors['text_primary'],
            bg=self.colors['surface']
        )
        results_title.pack(anchor='w')
        
        # Results area
        self.results_frame = tk.Frame(results_card, bg=self.colors['surface'])
        self.results_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=(20, 30))
        
        # Initial placeholder
        self.create_placeholder_results()

    def create_placeholder_results(self):
        placeholder_frame = tk.Frame(self.results_frame, bg=self.colors['background'])
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
            text="Select a machine learning model to analyze the data",
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
            # Header image - use Vinsanity for ML (dynamic/innovative)
            header_path = os.path.join(os.path.dirname(__file__), '..', 'assests', 'Vinsanity.jpg')
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

    def run_model(self, model_code, model_name):
        # Clear previous results
        for widget in self.results_frame.winfo_children():
            widget.destroy()
        
        # Show loading message
        loading_frame = tk.Frame(self.results_frame, bg=self.colors['background'])
        loading_frame.pack(expand=True)
        
        loading_label = tk.Label(
            loading_frame,
            text=" Running Model...",
            font=("Arial", 16),
            fg=self.colors['accent'],
            bg=self.colors['background']
        )
        loading_label.pack()
        
        status_label = tk.Label(
            loading_frame,
            text=f"Executing {model_name}",
            font=("Arial", 12),
            fg=self.colors['text_secondary'],
            bg=self.colors['background']
        )
        status_label.pack(pady=(10, 0))
        
        # Update the display
        self.update()
        
        try:
            # Run the model
            val_acc, test_acc = run_machine_learning_model(self.season, model_code)
            
            # Store results
            self.current_results = {
                'model': model_name,
                'validation_accuracy': val_acc,
                'test_accuracy': test_acc
            }
            
            # Display results
            self.display_results()
            
        except Exception as e:
            # Handle errors
            self.display_error(str(e))

    def display_results(self):
        # Clear loading message
        for widget in self.results_frame.winfo_children():
            widget.destroy()
        
        results = self.current_results
        
        # Results container
        results_container = tk.Frame(self.results_frame, bg=self.colors['background'])
        results_container.pack(expand=True, fill=tk.BOTH, pady=20)
        
        # Model name
        model_label = tk.Label(
            results_container,
            text=f" {results['model']} - Complete",
            font=("Arial", 18, "bold"),
            fg=self.colors['accent'],
            bg=self.colors['background']
        )
        model_label.pack(pady=(0, 20))
        
        # Create accuracy cards
        accuracy_frame = tk.Frame(results_container, bg=self.colors['background'])
        accuracy_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Validation Accuracy Card
        val_card = tk.Frame(accuracy_frame, bg=self.colors['surface'], relief='raised', bd=1)
        val_card.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        val_content = tk.Frame(val_card, bg=self.colors['surface'])
        val_content.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        val_title = tk.Label(
            val_content,
            text="VALIDATION ACCURACY",
            font=("Arial", 12, "bold"),
            fg=self.colors['text_primary'],
            bg=self.colors['surface']
        )
        val_title.pack()
        
        val_value = tk.Label(
            val_content,
            text=f"{results['validation_accuracy']:.1%}",
            font=("Arial", 24, "bold"),
            fg=self.colors['primary'],
            bg=self.colors['surface']
        )
        val_value.pack(pady=(10, 0))
        
        # Test Accuracy Card
        test_card = tk.Frame(accuracy_frame, bg=self.colors['surface'], relief='raised', bd=1)
        test_card.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0))
        
        test_content = tk.Frame(test_card, bg=self.colors['surface'])
        test_content.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        test_title = tk.Label(
            test_content,
            text="TEST ACCURACY",
            font=("Arial", 12, "bold"),
            fg=self.colors['text_primary'],
            bg=self.colors['surface']
        )
        test_title.pack()
        
        test_value = tk.Label(
            test_content,
            text=f"{results['test_accuracy']:.1%}",
            font=("Arial", 24, "bold"),
            fg=self.colors['secondary'],
            bg=self.colors['surface']
        )
        test_value.pack(pady=(10, 0))
        
        # Performance indicator
        avg_accuracy = (results['validation_accuracy'] + results['test_accuracy']) / 2
        if avg_accuracy > 0.8:
            performance = ("EXCELLENT", self.colors['accent'])
        elif avg_accuracy > 0.7:
            performance = ("GOOD", "#2e8b57")
        elif avg_accuracy > 0.6:
            performance = ("FAIR", "#ff6347")
        else:
            performance = ("NEEDS IMPROVEMENT", "#dc143c")
        
        performance_label = tk.Label(
            results_container,
            text=f"Performance: {performance[0]}",
            font=("Arial", 14, "bold"),
            fg=performance[1],
            bg=self.colors['background']
        )
        performance_label.pack(pady=(20, 0))

    def display_error(self, error_message):
        # Clear loading message
        for widget in self.results_frame.winfo_children():
            widget.destroy()
        
        # Error container
        error_container = tk.Frame(self.results_frame, bg=self.colors['background'])
        error_container.pack(expand=True)
        
        error_icon = tk.Label(
            error_container,
            text="",
            font=("Arial", 48),
            fg="#dc143c",
            bg=self.colors['background']
        )
        error_icon.pack()
        
        error_label = tk.Label(
            error_container,
            text="Model Execution Failed",
            font=("Arial", 16, "bold"),
            fg="#dc143c",
            bg=self.colors['background']
        )
        error_label.pack(pady=(10, 0))
        
        error_detail = tk.Label(
            error_container,
            text=error_message,
            font=("Arial", 10),
            fg=self.colors['text_secondary'],
            bg=self.colors['background'],
            wraplength=400
        )
        error_detail.pack(pady=(10, 0))
