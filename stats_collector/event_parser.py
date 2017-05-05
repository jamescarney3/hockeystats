# pass this function as the first argument to any event html blob's find_all
# method to isolate on-ice tables which can then be passed into
# parse_player_table and transformed into data dicts that represent on-ice
# personel for each team
def is_player_table(tag):
    return tag.font != [] and tag.name == 'tr' and tag.tr

# takes as an argument one bs4 tag instance representing one team's players
# on-ice for a given game event and parses it into a list of dicts containing
# each player's position, abbreviated position, name, and number
def parse_player_table(on_ice_tr):
    on_ice = []
    on_ice_tables = on_ice_tr.find_all('table')

    for table in on_ice_tables:
        position_name = table.font['title'].split(' - ')[0]
        player_name = table.font['title'].split(' - ')[1]
        number = table.find_all('tr')[0].get_text(strip=True)
        position_key = table.find_all('tr')[1].get_text(strip=True)

        on_ice.append({'position_name': position_name,
                       'player_name': player_name,
                       'number': number,
                       'position_key': position_key});
    return on_ice
