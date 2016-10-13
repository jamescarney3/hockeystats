import unittest
import context

from stats_collector.url_generator import (generate_game_report_url,
                                           generate_home_players_url,
                                           generate_visitor_players_url)

class TestUrlGenerator(unittest.TestCase):
    def test_generate_regular_season_game_report_url(self):
        target_url = 'http://www.nhl.com/scores/htmlreports/20102011/PL020808.HTM'
        iterator = {"year": 2010,
                    "season": 2,
                    "game": 808,
                    "round": 1,
                    "series": 1,
                    "fails": 0}
        self.assertEqual(generate_game_report_url(iterator), target_url)

    def test_generate_regular_season_home_roster_report_url(self):
        target_url = 'http://www.nhl.com/scores/htmlreports/20102011/TH020808.HTM'
        iterator = {"year": 2010,
                    "season": 2,
                    "game": 808,
                    "round": 1,
                    "series": 1,
                    "fails": 0}
        self.assertEqual(generate_home_players_url(iterator), target_url)

    def test_generate_regular_season_visitor_roster_report_url(self):
        target_url = 'http://www.nhl.com/scores/htmlreports/20102011/TV020808.HTM'
        iterator = {"year": 2010,
                    "season": 2,
                    "game": 808,
                    "round": 1,
                    "series": 1,
                    "fails": 0}
        self.assertEqual(generate_visitor_players_url(iterator), target_url)

    def test_generate_playoff_game_report_url(self):
        target_url = 'http://www.nhl.com/scores/htmlreports/20102011/PL030413.HTM'
        iterator = {"year": 2010,
                    "season": 3,
                    "game": 3,
                    "round": 4,
                    "series": 1,
                    "fails": 0}
        self.assertEqual(generate_game_report_url(iterator), target_url)

    def test_bad_game_id_iterator(self):
        iterator = {"year": 2010,
                    "season": 3,
                    "round": 4,
                    "series": 1,
                    "fails": 0}
        with self.assertRaises(Exception):
            generate_game_report_url(iterator)

if __name__ == '__main__':
    unittest.main()
