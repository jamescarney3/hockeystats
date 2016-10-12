# initial_game_id_iterator is a dict that represents
# the first game report available in the format this
# project will initially deal with, as well as an
# example of the data structure to which all game
# report urls will be serialized. Its fields map to
# the component parts of a game report url, namely
# the season-year element of the path (year key) and
# and the game id element of the path (always built
# from seasona and game keys, also round and series
# keys for playoff games). The "fails" k/v pair
# represents the number of consecutive failures the
# scraper has encountered and is used to determine
# whether it has reached the end of a preseason or
# regular season (variable lengths due to lockouts
# and/or canceled games).
initial_game_id_iterator = {"year": 2007,
                            "season": 1,
                            "game": 0,
                            "round": 1,
                            "series": 1,
                            "fails": 0}

MAX_FAILS = 10
PRESEASON_CODE = 1
REG_SEASON_CODE = 2
PLAYOFF_CODE = 3
PLAYOFF_MAX_ROUNDS = 4
PLAYOFF_MAX_SERIES = 8
PLAYOFF_MAX_GAMES = 7

# The increment_game_id_iterator function takes a
# game report url seralized into an game_id_iterator
# and returns a game_id_iterator that can be
# deseralized into the url for the next game report
# the scraper will attempt to process.
def increment_game_id_iterator(game_id_iterator=initial_game_id_iterator, **kwargs):

    year = game_id_iterator["year"]
    season = game_id_iterator["season"]
    game = game_id_iterator["game"]
    rd = game_id_iterator["round"] # round is a reserved word. nice.
    series = game_id_iterator["series"]
    fails = game_id_iterator["fails"]
    next_iterator = game_id_iterator.copy()

    if season < PLAYOFF_CODE:
        if fails < MAX_FAILS:
            next_iterator.update({"game": game + 1,
                                  "fails": 0})
        else:
            next_iterator.update({"season": season + 1,
                                  "game": 1,
                                  "fails": 0})
    else:
        if game < PLAYOFF_MAX_GAMES:
            next_iterator.update({"game": game + 1,
                                  "fails": 0})
        elif series < 2**(PLAYOFF_MAX_ROUNDS - rd): # bracketology!
            next_iterator.update({"series": series + 1,
                                  "game": 1,
                                  "fails": 0})
        elif rd < PLAYOFF_MAX_ROUNDS:
            next_iterator.update({"round": rd + 1,
                                  "series": 1,
                                  "game": 1,
                                  "fails": 0})
        else:
            next_iterator.update({"year": year + 1,
                                  "season": 1,
                                  "game": 1,
                                  "round": 1,
                                  "series": 1,
                                  "fails": 0})
    return next_iterator
