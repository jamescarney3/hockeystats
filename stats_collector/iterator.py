INIT_YEAR = 2007
INIT_SEASON_CODE = 1
INIT_GAME = 0
INIT_ROUND = 1
INIT_SERIES = 1
INIT_FAILS = 0

MAX_FAILS = 10
PRESEASON_CODE = 1
REG_SEASON_CODE = 2
PLAYOFF_CODE = 3
PLAYOFF_MAX_ROUNDS = 4
PLAYOFF_MAX_SERIES = 8 # this isn't used, keep for notes
PLAYOFF_MAX_GAMES = 7

class GameIterator:
    # should this be able to take a dict or **kwargs so you can instantiate a
    # fresh one from wherever you left of for whatever reason?
    def __init__(self):
        self.year = INIT_YEAR
        self.season_code = INIT_SEASON_CODE
        self.game = INIT_GAME
        self.round = INIT_ROUND
        self.series = INIT_SERIES
        self.fails = INIT_FAILS

    # getting vals out of this thing should happen with serialize and get, but
    # it would obviously be better to bury the actual ivars by usore prefixing
    # them and providing getters
    def serialize(self):
        return {
            'year': self.year,
            'season_code': self.season_code,
            'game': self.game,
            'round': self.round,
            'series': self.series,
            'fails': self.fails}

    def get(self, key):
        return self.serialize().get(key)

    def reset_keys(self, *keys):
        for key in keys:
            if key == 'fails':
                setattr(self, key, 0)
            else:
                setattr(self, key, 1)

    def increment_keys(self, *keys):
        for key in keys:
            setattr(self, key, getattr(self, key) + 1)

    def log_failure(self):
        self.increment_keys('fails')


    def increment(self):
        # not looking at playoffs, normal game numbering
        if self.season_code < PLAYOFF_CODE:
            # I might not have exceeded the max number of games in this (pre|post|*)season
            if self.fails < MAX_FAILS:
                # just increment game number
                self.increment_keys('game')
                self.reset_keys('fails')

            # I'm consistently not getting data for game numbers this high
            else:
                # increment season code for reg season or playoffs and reset game code
                self.increment_keys('season_code')
                self.reset_keys('fails', 'game')

        # it's the playoffs! game numbering is complicated
        else:
            # this isn't a game 7
            if self.game < PLAYOFF_MAX_GAMES:
                # just increment game number
                self.increment_keys('game')
                self.reset_keys('fails')

            # there's still at least another series left in this round: #bracketology!
            elif self.series < 2 ** (PLAYOFF_MAX_ROUNDS - self.round):
                self.increment_keys('series')
                self.reset_keys('fails', 'game')

            # there's still at least another round left in the playoffs
            elif self.round < PLAYOFF_MAX_ROUNDS:
                self.increment_keys('round')
                self.reset_keys('fails', 'game', 'series')

            # this was game 7 of the cup finals
            else:
                self.increment_keys('year')
                self.reset_keys('fails', 'game', 'series', 'round', 'season_code')


##### OLD CODE IS HERE #####
#
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
#
# initial_game_id_iterator = {"year": 2007,
#                             "season": 1,
#                             "game": 0,
#                             "round": 1,
#                             "series": 1,
#                             "fails": 0}
#
# The increment_game_id_iterator function takes a
# game report url seralized into an game_id_iterator
# and returns a game_id_iterator that can be
# deseralized into the url for the next game report
# the scraper will attempt to process.
#
# def increment_game_id_iterator(game_id_iterator=initial_game_id_iterator):
#
#     year = game_id_iterator["year"]
#     season = game_id_iterator["season"]
#     game = game_id_iterator["game"]
#     rd = game_id_iterator["round"] # round is a reserved word. nice.
#     series = game_id_iterator["series"]
#     fails = game_id_iterator["fails"]
#     next_iterator = game_id_iterator.copy()
#
#     if season < PLAYOFF_CODE:
#         if fails < MAX_FAILS:
#             next_iterator.update({"game": game + 1,
#                                   "fails": 0})
#         else:
#             next_iterator.update({"season": season + 1,
#                                   "game": 1,
#                                   "fails": 0})
#     else:
#         if game < PLAYOFF_MAX_GAMES:
#             next_iterator.update({"game": game + 1,
#                                   "fails": 0})
#         elif series < 2**(PLAYOFF_MAX_ROUNDS - rd): # bracketology!
#             next_iterator.update({"series": series + 1,
#                                   "game": 1,
#                                   "fails": 0})
#         elif rd < PLAYOFF_MAX_ROUNDS:
#             next_iterator.update({"round": rd + 1,
#                                   "series": 1,
#                                   "game": 1,
#                                   "fails": 0})
#         else:
#             next_iterator.update({"year": year + 1,
#                                   "season": 1,
#                                   "game": 1,
#                                   "round": 1,
#                                   "series": 1,
#                                   "fails": 0})
#     return next_iterator