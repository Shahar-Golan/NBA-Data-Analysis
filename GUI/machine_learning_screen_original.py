import tkinter as tk
from tkinter import messagebox, ttk
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
        
        self.setup_ui()
        self.load_hero_images()

        # Title
        tk.Label(self, text=f"Machine Learning Analysis for {season}", font=("Helvetica", 16)).pack(pady=10)

        # Model selection buttons
        models = {
            "Logistic Regression": "logistic_regression",
            "SVM": "svm_model",
            "Random Forest": "random_forest_model",
            "Naive Bayes": "naive_bayes_model"
        }

        for model_name, model_code in models.items():
            button = tk.Button(self, text=model_name, command=lambda code=model_code: self.run_model(code))
            button.pack(pady=5)

        # Back button
        back_button = tk.Button(self, text="Back", command=self.on_back)
        back_button.pack(pady=10)

        # Label to display results
        self.result_label = tk.Label(self, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=20)

    def run_model(self, model_name):
        # Placeholder function to simulate model execution
        messagebox.showinfo("Model Execution", "Running the model...")
        # Here, you would call your model function and handle the result.
        val_acc, test_acc =   run_machine_learning_model(self.season, model_name)
        # Display accuracies in the result label
        self.result_label.config(text=f"{model_name.replace('_', ' ').title()} Results:\n"
                                      f"Validation Accuracy: {val_acc:.2%}\n"
                                      f"Test Accuracy: {test_acc:.2%}")