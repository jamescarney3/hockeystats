import unittest
import context

from stats_collector.url_generator import (generate_game_report_url,
                                           generate_home_players_url,
                                           generate_visitor_players_url)

class TestUrlGenerator(unittest.TestCase):
    def test_dummy(self):
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()
