from get_box_score import get_boxscore_json, boxscore_team_tables


# Example game_pk (you can replace this with any valid MLB game_pk)
# For example: 748287, 716297, etc. (regular-season games from recent years)

# if you want the user to input the MLB game_pk
# game_pk = int(input("Enter MLB game_pk: ").strip())

#for this test, I will provide you with the game_pk

print("\nTesting ability to pull box score using MLB API")

print("\nUsing example MLB game_pk = 662888 to show boxscore of Chicago Whitesox and Detroit Tigers")

game_pk = 662888

    # 1. Get JSON
box_json = get_boxscore_json(game_pk)

    # 2. Get team DataFrames
away_df, home_df = boxscore_team_tables(box_json)

print("\n=== Away Team Boxscore ===")
print(away_df)

print("\n=== Home Team Boxscore ===")
print(home_df)
