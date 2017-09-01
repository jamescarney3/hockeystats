import unittest
import context
from mock import MagicMock

# from stats_collector.workflow import (get_game_report)


class TestWorkflow(unittest.TestCase):
    def test_get_game_report_from_good_url(self):
        # check that iterator.increment_game_id_iterator is called
        # check that successful call/response is logged
        self.assertEqual(True, True)

    def test_get_game_report_from_bad_url(self):
        # check that iterator["fails"] is incremented
        # check that iterator.increment_game_id_iterator is called
        # check that bad call/response is logged
        self.assertEqual(True, True)
        self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()
