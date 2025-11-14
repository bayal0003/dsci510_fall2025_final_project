import requests
import pandas as pd

BOXSCORE_URL = "https://statsapi.mlb.com/api/v1/game/{game_pk}/boxscore"

def get_boxscore_json(game_pk: int) -> dict:
    """
    Fetch raw boxscore JSON from MLB Stats API for a given game_pk.
    """
    url = BOXSCORE_URL.format(game_pk=game_pk)
    resp = requests.get(url)
    resp.raise_for_status()  # will raise HTTPError if invalid game_pk or server error
    return resp.json()

def boxscore_team_tables(boxscore_json: dict):
    """
    Convert boxscore JSON into two DataFrames: home team & away team player stats.
    Returns (away_df, home_df).
    """
    teams = boxscore_json.get("teams", {})
    away = teams.get("away", {})
    home = teams.get("home", {})

    def players_to_rows(team_dict: dict, side: str):
        rows = []
        players = team_dict.get("players", {})
        team_name = team_dict.get("team", {}).get("name", side)

        for player_id, pdata in players.items():
            person = pdata.get("person", {})
            stats = pdata.get("stats", {})
            batting = stats.get("batting", {})
            pitching = stats.get("pitching", {})
            fielding = stats.get("fielding", {})

            row = {
                "team": team_name,
                "side": side,
                "fullName": person.get("fullName"),
                "position": pdata.get("position", {}).get("abbreviation"),
                "batting_AB": batting.get("atBats"),
                "batting_R": batting.get("runs"),
                "batting_H": batting.get("hits"),
                "batting_RBI": batting.get("rbi"),
                "batting_BB": batting.get("baseOnBalls"),
                "batting_SO": batting.get("strikeOuts"),
                "batting_HR": batting.get("homeRuns"),
                "pitching_IP": pitching.get("inningsPitched"),
                "pitching_H": pitching.get("hits"),
                "pitching_R": pitching.get("runs"),
                "pitching_ER": pitching.get("earnedRuns"),
                "pitching_BB": pitching.get("baseOnBalls"),
                "pitching_SO": pitching.get("strikeOuts"),
                "pitching_HR": pitching.get("homeRuns"),
                "pitching_Pitches": pitching.get("numberOfPitches"),
                "pitching_Strikes": pitching.get("strikes"),
                "fielding_E": fielding.get("errors"),
                "fielding_PO": fielding.get("putOuts"),
                "fielding_A": fielding.get("assists"),
            }
            rows.append(row)
        return rows

    away_rows = players_to_rows(away, "away")
    home_rows = players_to_rows(home, "home")

    away_df = pd.DataFrame(away_rows)
    home_df = pd.DataFrame(home_rows)

    return away_df, home_df

def main():
    # Example game_pk (you can replace this with any valid MLB game_pk)
    # For example: 748287, 716297, etc. (regular-season games from recent years)
    game_pk = int(input("Enter MLB game_pk: ").strip())

    # 1. Get JSON
    box_json = get_boxscore_json(game_pk)

    # 2. Get team DataFrames
    away_df, home_df = boxscore_team_tables(box_json)

    print("\n=== Away Team Boxscore ===")
    print(away_df)

    print("\n=== Home Team Boxscore ===")
    print(home_df)

if __name__ == "__main__":
    main()
