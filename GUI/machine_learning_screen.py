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

    def create_header(self, parent):
        header_frame = tk.Frame(parent, bg=self.colors['background'])
        header_frame.pack(fill=tk.X, pady=(0, 25))
        
        # Back button
        back_button = tk.Button(
            header_frame,
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
        
        # Title
        title_label = tk.Label(
            header_frame,
            text=f"MACHINE LEARNING ANALYSIS - {self.season}",
            font=("Arial", 24, "bold"),
            fg=self.colors['text_primary'],
            bg=self.colors['background']
        )
        title_label.pack(pady=(20, 0))

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
        
        # Define models
        models = [
            {"name": "Logistic Regression", "code": "logistic_regression", "color": self.colors['primary']},
            {"name": "Support Vector Machine", "code": "svm_model", "color": self.colors['secondary']},
            {"name": "Random Forest", "code": "random_forest_model", "color": "#2e8b57"},
            {"name": "Naive Bayes", "code": "naive_bayes_model", "color": "#ff6347"}
        ]
        
        # Create buttons
        for model in models:
            button = tk.Button(
                model_content,
                text=model['name'],
                command=lambda code=model['code'], name=model['name']: self.run_model(code, name),
                bg=model['color'],
                fg=self.colors['text_primary'],
                font=("Arial", 12, "bold"),
                relief='flat',
                bd=0,
                pady=10,
                cursor='hand2'
            )
            button.pack(fill=tk.X, pady=5)

    def create_results_area(self, parent):
        # Results card
        results_card = tk.Frame(parent, bg=self.colors['surface'], relief='raised', bd=1)
        results_card.pack(fill=tk.BOTH, expand=True)
        
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
        
        instruction_label = tk.Label(
            placeholder_frame,
            text="Select a machine learning model to analyze the data",
            font=("Arial", 12),
            fg=self.colors['text_secondary'],
            bg=self.colors['background']
        )
        instruction_label.pack(pady=(10, 0))

    def load_hero_images(self):
        pass  # Placeholder for image loading

    def run_model(self, model_code, model_name):
        print(f"Running model: {model_name} with code: {model_code}")
        
        # Clear previous results
        for widget in self.results_frame.winfo_children():
            widget.destroy()
        
        # Show loading message
        loading_label = tk.Label(
            self.results_frame,
            text=f"Running {model_name}...",
            font=("Arial", 14),
            fg=self.colors['accent'],
            bg=self.colors['surface']
        )
        loading_label.pack(expand=True)
        
        # Force GUI update
        self.parent.update()
        
        try:
            # Run the model
            val_acc, test_acc = run_machine_learning_model(self.season, model_code)
            print(f"Results - Validation: {val_acc:.3f}, Test: {test_acc:.3f}")
            
            # Clear loading and show results
            loading_label.destroy()
            
            # Create results display
            results_container = tk.Frame(self.results_frame, bg=self.colors['surface'])
            results_container.pack(expand=True, fill=tk.BOTH, pady=20)
            
            # Model name
            model_label = tk.Label(
                results_container,
                text=f"{model_name} - Results",
                font=("Arial", 16, "bold"),
                fg=self.colors['accent'],
                bg=self.colors['surface']
            )
            model_label.pack(pady=(0, 20))
            
            # Create accuracy display
            accuracy_frame = tk.Frame(results_container, bg=self.colors['surface'])
            accuracy_frame.pack(fill=tk.X, pady=(0, 20))
            
            # Validation Accuracy
            val_card = tk.Frame(accuracy_frame, bg=self.colors['background'], relief='raised', bd=1)
            val_card.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
            
            tk.Label(
                val_card,
                text="VALIDATION ACCURACY",
                font=("Arial", 11, "bold"),
                fg=self.colors['text_primary'],
                bg=self.colors['background']
            ).pack(pady=(10, 5))
            
            tk.Label(
                val_card,
                text=f"{val_acc:.1%}",
                font=("Arial", 20, "bold"),
                fg=self.colors['primary'],
                bg=self.colors['background']
            ).pack(pady=(0, 10))
            
            # Test Accuracy
            test_card = tk.Frame(accuracy_frame, bg=self.colors['background'], relief='raised', bd=1)
            test_card.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0))
            
            tk.Label(
                test_card,
                text="TEST ACCURACY",
                font=("Arial", 11, "bold"),
                fg=self.colors['text_primary'],
                bg=self.colors['background']
            ).pack(pady=(10, 5))
            
            tk.Label(
                test_card,
                text=f"{test_acc:.1%}",
                font=("Arial", 20, "bold"),
                fg=self.colors['secondary'],
                bg=self.colors['background']
            ).pack(pady=(0, 10))
            
            # Performance indicator
            avg_accuracy = (val_acc + test_acc) / 2
            if avg_accuracy > 0.8:
                performance_text = "EXCELLENT"
                performance_color = self.colors['accent']
            elif avg_accuracy > 0.7:
                performance_text = "GOOD"
                performance_color = "#2e8b57"
            elif avg_accuracy > 0.6:
                performance_text = "FAIR"
                performance_color = "#ff6347"
            else:
                performance_text = "NEEDS IMPROVEMENT"
                performance_color = "#dc143c"
            
            performance_label = tk.Label(
                results_container,
                text=f"Performance: {performance_text}",
                font=("Arial", 12, "bold"),
                fg=performance_color,
                bg=self.colors['surface']
            )
            performance_label.pack(pady=(20, 0))
            
        except Exception as e:
            print(f"Error running model: {e}")
            # Show error
            loading_label.destroy()
            
            error_label = tk.Label(
                self.results_frame,
                text=f"Error: {str(e)}",
                font=("Arial", 12),
                fg="#dc143c",
                bg=self.colors['surface']
            )
            error_label.pack(expand=True)
