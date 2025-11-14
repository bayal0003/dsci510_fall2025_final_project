# dsci510_fall2025_final_project
This is a dsci fall 2025 final project


# <Project title> MLB Umpire Data Analysis
Project scope update:
Originally, my main goal for my project was to analyze umpire ejections and see if the umpire’s poor accuracy led to more ejections. After trying to make python codes to help collect and process data, I have hit multiple roadblocks. As a result, I am slightly updating the question for my project. My new question is, if a player is ejected from a game, is that team more likely to lose the game? 
Right now, I have no trouble working with the csv file with a list of all MLB umpire ejections. I am able to create boxplots easily showing what umpires eject the most, who get ejected the most, and the reason they got ejected the most.
My main challenge right now is getting the result of the game in which a team was ejected. I was able to create a python code that uses MLB API to give me the box score of the game. My main issue is that the format of the GAMEID from retro sheet is different from what the MLB uses for API. Once I figure that out, I will be able to pull the game data and store who the winner is in my database.
Finally, to use my third source, there is a Kaggle database with MLB Umpire scorecards, I can find the top 10 umpires with ejections in the range of the Kaggle Database(2015-2022) and compare their overall accuracies and see if the umpires who love to eject players have a worse accuracy.


# Data sources
[](https://www.retrosheet.org/eject.htm)
- list of all MLB umpire ejections
f"https://statsapi.mlb.com/api/v1/game/{game_id}/boxscore"
-MLB API that lets me pull box score
https://www.kaggle.com/datasets/mattop/mlb-baseball-umpire-scorecards-2015-2022?resource=download
-kaggle umpire scorecard data set, I will use to compare umpire accuracy

# Results 
My findings right now are still pending. I am able to find the leading umpires for ejections and the leading reasons for ejections, now i need to find the data that tells me the outcome of the game

# Installation
pip install kaggle pandas matplotlib

# Running analysis 
_update these instructions_


From `src/` directory run:

`python main.py `

Results will appear in `results/` folder. All obtained will be stored in `data/`