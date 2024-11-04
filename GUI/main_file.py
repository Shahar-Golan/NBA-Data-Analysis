import tkinter as tk
from machine_learning_screen import MachineLearningScreen
from season_selection import SeasonSelectionScreen
from options_screen import OptionsScreen

class NBAApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("NBA Data Analysis")
        self.geometry("800x700")
        self.current_screen = None
        self.show_season_selection()

    def show_season_selection(self):
        if self.current_screen:
            self.current_screen.pack_forget()
        self.current_screen = SeasonSelectionScreen(self, self.show_options_screen)
        self.current_screen.pack()

    def show_options_screen(self, season, option_type):
        if self.current_screen:
            self.current_screen.pack_forget()
        if option_type == "analytics":
            self.current_screen = OptionsScreen(self, season, self.show_season_selection)
        elif option_type == "ml":
            # You’ll need to implement MachineLearningScreen to display the ML analysis
            self.current_screen = MachineLearningScreen(self, season, self.show_season_selection)
        self.current_screen.pack()

# Run the app
if __name__ == "__main__":
    app = NBAApp()
    app.mainloop()
