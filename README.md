NBA Data Analysis Project
This project is an end-to-end data analysis and machine learning pipeline for exploring, analyzing, and predicting outcomes based on NBA player and team performance data. Built with a GUI interface, this project allows users to select a season, view player analytics across different tiers, and run machine learning models to predict game outcomes.

Features
Data Collection:

NBA data is fetched from an API and processed into a structured format.
Seasonal data files are organized by team and player performance metrics.
Data Analysis:

Analyze player performance against various opponent tiers.
Compute metrics like Points Per Game (PPG), Assists Per Game (APG), Rebounds Per Game (RPG), and Win Percentage (W%).
View performance breakdown for players by tier.
Machine Learning:

Build machine learning models (Logistic Regression, SVM, Naive Bayes, Random Forest) to predict game outcomes.
Training and validation accuracy metrics are displayed for model evaluation.
Predict and display playoff game results and compare model predictions to actual results.
GUI:

Select NBA seasons and view detailed player stats for each season.
Choose between player analytics or machine learning prediction workflows.
Display analysis and model results visually within the GUI.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/Shahar-Golan/NBA-Data-Analysis.git
cd NBA-Data-Analysis-Project
Install required libraries:

bash
Copy code
pip install -r requirements.txt
Set up environment variables if API keys or specific configurations are needed.

Usage
Run the GUI:

bash
Copy code
python main_file.py
Navigate the GUI:

Season Selection: Choose a season to analyze.
Player Analytics: View player statistics across different tiers.
Machine Learning Analysis: Run selected models and view predictions.
Project Structure
Dataset_Creation: Scripts to process and organize raw data files.
Machine_Learning: Contains model training and evaluation scripts.
GUI: Files to manage the graphical user interface and user interaction.
All_Seasons: Folder to store seasonal data files.
Future Improvements
Add more advanced machine learning models and hyperparameter tuning.
Implement deeper analytics, such as comparing regular season vs. playoff performance.
Enhance visualization within the GUI for richer analysis.
License
This project is licensed under the MIT License. See LICENSE for more information.

Contact
For any questions, feel free to reach out via GitHub Issues or contact me at [your_email@example.com].