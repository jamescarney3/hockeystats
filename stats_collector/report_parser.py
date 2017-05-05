# coding: latin-1

import re
from bs4 import BeautifulSoup

from utils import ABBREVIATIONS

whiteSpaceReducer = re.compile('(\s|\xa0|&nbsp;)+')
name_isolator = re.compile(' (Match/)*Game \d+ ((Dom\./)*Home|(.tr\./)*Away) (Game )*\d+')
attendance_matcher = re.compile('(\d+,|)\d+')
arena_isolator = re.compile('(Attendance|Ass./Att) (\d+,|)\d+ (at|@) ')

# parse_game_report takes a game report dom string and returns a
# json serialization of all events and metadata contained in the
# report
def parse_game_report(game_report_html):
    soup = BeautifulSoup(game_report_html)
    events = soup.find_all('tr', {'class': 'evenColor'})
    visitor_info = soup.find('table', {'id': 'Visitor'})
    home_info = soup.find('table', {'id': 'Home'})
    game_info = soup.find('table', {'id': 'GameInfo'})

    visitor_info_vals = []
    home_info_vals = []
    game_info_vals = []
    game_json = {}

    for td in visitor_info('td'):
        visitor_info_vals.append(whiteSpaceReducer.sub(' ', td.get_text(' ', strip=True)))

    for td in home_info('td'):
        home_info_vals.append(whiteSpaceReducer.sub(' ', td.get_text(' ', strip=True)))

    for td in game_info('td'):
        game_info_vals.append(whiteSpaceReducer.sub(' ', td.get_text(' ', strip=True)))

    game_json['serial'] = re.compile('\D').sub('', game_info_vals[6])
    # if game_info_vals[2]:
    #     game_json['season'] = 'playoffs'
    game_json['date'] = game_info_vals[3]
    game_json['attendance'] = attendance_matcher.search(game_info_vals[4]).group()
    game_json['arena'] = arena_isolator.sub('', game_info_vals[4])
    # game_json['start'] = game_info_vals[5] ---- regexed for start time
    # game_json['end'] = game_info_vals[5] ---- regexed for end time
    game_json['home_team'] = name_isolator.sub('', home_info_vals[5])
    game_json['home_abbreviation'] = ABBREVIATIONS[name_isolator.sub('', home_info_vals[5]).lower()]
    game_json['home_score'] = int(home_info_vals[1])
    game_json['visitor_team'] = name_isolator.sub('', visitor_info_vals[5])
    game_json['visitor_abbreviation'] = ABBREVIATIONS[name_isolator.sub('', visitor_info_vals[5]).lower()]
    game_json['visitor_score'] = int(visitor_info_vals[1])

    game_json['events'] = []

    # for event in events:
    #     game_json['events'].append(parse_event(event))

    # game_json['url'] = url

    return game_json
