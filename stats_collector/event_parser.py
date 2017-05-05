# TODO figure out how to parse event descriptions

import re

# takes a BeautifulSoup tag instance (assumed to be a child of an event tag
# instance that represents a team's on-ice personnel for that event) and parses
# it into a list of dicts containing each player's position, abbreviated
# position, name, and number
def parse_on_ice_td(on_ice_td):
    outer_table = on_ice_td.table
    # sometimes there's no one on the ice for penalties that happen after the
    # game ends (+ other potential edge cases...)
    if outer_table:
        players = outer_table.find_all('table')
        on_ice = []
        for player in players:
            player_json = {'position_name': player.font['title'].split(' - ')[0],
                           'player_name': player.font['title'].split(' - ')[1],
                           'number': player.find_all('tr')[0].get_text(strip=True),
                           'position_key': player.find_all('tr')[1].get_text(strip=True)}
            on_ice.append(player_json)
        return on_ice
    return None

# takes a beatiful soup tag instance assumed to represent a game event and
# parses it into a representative json object
def parse_event(event_tr):
    event_tds = event_tr.find_all('td', recursive=False)
    event_json = {'seq': int(event_tds[0].get_text()),
                  'per': int(event_tds[1].get_text()),
                  'str': event_tds[2].get_text(),
                  'time_elapsed': event_tds[3].contents[0],
                  'time_remaining': event_tds[3].contents[1].get_text(),
                  'type': event_tds[4].get_text(),
                  'desc': event_tds[5].get_text(),
                  'visitor_on_ice': parse_on_ice_td(event_tds[6]),
                  'home_on_ice': parse_on_ice_td(event_tds[7])}
    return event_json
