# NBA Data Analysis Project

This project is an end-to-end data analysis and machine learning pipeline for exploring, analyzing, and predicting outcomes based on NBA player and team performance data. Built with a GUI interface, this project allows users to select a season, view player analytics across different tiers, and run machine learning models to predict game outcomes.

## Features

1. **Data Collection**:
   - NBA data is fetched from an API and processed into a structured format.
   - Seasonal data files are organized by team and player performance metrics.

2. **Data Analysis**:
   - Analyze player performance against various opponent tiers.
   - Compute metrics like Points Per Game (PPG), Assists Per Game (APG), Rebounds Per Game (RPG), and Win Percentage (W%).
   - View performance breakdown for players by tier.

3. **Machine Learning**:
   - Build machine learning models (Logistic Regression, SVM, Naive Bayes, Random Forest) to predict game outcomes.
   - Training and validation accuracy metrics are displayed for model evaluation.
   - Predict and display playoff game results and compare model predictions to actual results.

4. **GUI**:
   - Select NBA seasons and view detailed player stats for each season.
   - Choose between player analytics or machine learning prediction workflows.
   - Display analysis and model results visually within the GUI.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Shahar-Golan/NBA-Data-Analysis-Project.git
   cd NBA-Data-Analysis-Project
