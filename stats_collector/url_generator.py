# all data, both play by play and roster reports lives
# here.
BASE_URL = 'http://www.nhl.com/scores/htmlreports/'

PLAY_BY_PLAY_PREFIX = '/PL'
HOME_PLAYERS_PREFIX = '/TH'
VISITOR_PLAYERS_PREFIX = '/TV'
EXTENSION = '.HTM'

PRESEASON_CODE = 1
REG_SEASON_CODE = 2
PLAYOFF_CODE = 3

def generate_game_report_url(game_id_iterator):
    return (BASE_URL
            + get_year_path(game_id_iterator['year'])
            + PLAY_BY_PLAY_PREFIX
            + get_game_id(game_id_iterator['season'],
                          game_id_iterator['game'],
                          game_id_iterator['series'],
                          game_id_iterator['round'])
            + EXTENSION)

def generate_home_players_url(game_id_iterator):
    return (BASE_URL
            + get_year_path(game_id_iterator['year'])
            + HOME_PLAYERS_PREFIX
            + get_game_id(game_id_iterator['season'],
                          game_id_iterator['game'],
                          game_id_iterator['series'],
                          game_id_iterator['round'])
            + EXTENSION)

def generate_visitor_players_url(game_id_iterator):
    return (BASE_URL
            + get_year_path(game_id_iterator['year'])
            + VISITOR_PLAYERS_PREFIX
            + get_game_id(game_id_iterator['season'],
                          game_id_iterator['game'],
                          game_id_iterator['series'],
                          game_id_iterator['round'])
            + EXTENSION)

def get_game_id(season, game, series, rd):
    if season < PLAYOFF_CODE:
        return str(season).zfill(2) + str(game).zfill(4)
    else:
        return str(season).zfill(2) + (str(rd) + str(series) + str(game)).zfill(4)

def get_year_path(year):
    return str(year) + str(year + 1)

__all__ = ['generate_game_report_url',
           'generate_home_players_url',
           'generate_visitor_players_url']
