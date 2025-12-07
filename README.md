# dsci510_fall2025_final_project
This is a dsci fall 2025 final project


# <Project title> MLB Umpire Data Analysis
Project scope update:
Originally, my main goal for my project was to analyze umpire ejections and see if the umpire’s poor accuracy led to more ejections. After trying to make python codes to help collect and process data, I have hit multiple roadblocks. As a result, I am slightly updating the question for my project. My new question is, if a player is ejected from a game, is that team more likely to lose the game? 

I was having difficulty converting my Jupyter notebook to a python script and calling all my functions. I was able to get the code to work in a singular large Jupyter notebook, but could not separate the functions and call them without the code crashing. So I am uploading my Jupyter notebook with all my work in main.ipynb


# Data sources
[](https://www.retrosheet.org/eject.htm)
- list of all MLB umpire ejections
f"https://statsapi.mlb.com/api/v1/game/{game_id}/boxscore"
-MLB API that lets me pull box score
https://www.kaggle.com/datasets/mattop/mlb-baseball-umpire-scorecards-2015-2022?resource=download
-kaggle umpire scorecard data set, I will use to compare umpire accuracy

# Results 
I found in my dataset of 586 games with an ejection, the team that received an ejection would lost 65.7% of the time. I also found that most of the ejections took place when the weather was between 70-80 degrees.

# Installation
pip install kaggle pandas matplotlib

# Running analysis 
My plots are in the Jupyter notebook main


