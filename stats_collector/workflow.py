import requests

from url_generator import *
# generate_game_report_url
# generate_home_players_url
# generate_visitor_players_url

# The get_reports function takes an iterator object as its
# only argument and uses it to generate game data urls and
# request corresponding reports
# TODO error handling for dead urls
# TODO test to verify it returns an array of strings from response contents
# TODO test to verify it throws on a dead url
def get_reports(game_id_iterator):
    game_report_url = generate_game_report_url(game_id_iterator)
    home_players_url = generate_home_players_url(game_id_iterator)
    visitor_players_url = generate_visitor_players_url(game_id_iterator)
    game_report = requests.get(game_report_url).content
    home_players = requests.get(home_players_url).content
    visitor_players = requests.get(visitor_players_url).content
    return [game_report, home_players, visitor_players]
