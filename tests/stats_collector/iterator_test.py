import unittest
import context

from stats_collector.iterator import increment_game_id_iterator, MAX_FAILS

class TestGameIdIteratorIncrementor(unittest.TestCase):
    def test_iterator_with_no_args(self):
        first_game_id_iterator = {"year": 2007,
                                  "season": 1,
                                  "game": 1,
                                  "round": 1,
                                  "series": 1,
                                  "fails": 0}
        self.assertEqual(increment_game_id_iterator(), first_game_id_iterator)

    def test_preseason_game(self):
        first_game_id_iterator = {"year": 2007,
                                  "season": 1,
                                  "game": 10,
                                  "round": 1,
                                  "series": 1,
                                  "fails": 0}
        next_game_id_iterator = {"year": 2007,
                                 "season": 1,
                                 "game": 11,
                                 "round": 1,
                                 "series": 1,
                                 "fails": 0}
        self.assertEqual(increment_game_id_iterator(first_game_id_iterator), next_game_id_iterator)

    def test_reg_season_game(self):
        first_game_id_iterator = {"year": 2007,
                                  "season": 2,
                                  "game": 10,
                                  "round": 1,
                                  "series": 1,
                                  "fails": 0}
        next_game_id_iterator = {"year": 2007,
                                 "season": 2,
                                 "game": 11,
                                 "round": 1,
                                 "series": 1,
                                 "fails": 0}
        self.assertEqual(increment_game_id_iterator(first_game_id_iterator), next_game_id_iterator)

    def test_playoff_midseries_game(self):
        first_game_id_iterator = {"year": 2007,
                                  "season": 3,
                                  "game": 4,
                                  "round": 1,
                                  "series": 1,
                                  "fails": 0}
        next_game_id_iterator = {"year": 2007,
                                 "season": 3,
                                 "game": 5,
                                 "round": 1,
                                 "series": 1,
                                 "fails": 0}
        self.assertEqual(increment_game_id_iterator(first_game_id_iterator), next_game_id_iterator)

    def test_playoff_game_seven(self):
        first_game_id_iterator = {"year": 2007,
                                  "season": 3,
                                  "game": 7,
                                  "round": 1,
                                  "series": 1,
                                  "fails": 0}
        next_game_id_iterator = {"year": 2007,
                                 "season": 3,
                                 "game": 1,
                                 "round": 1,
                                 "series": 2,
                                 "fails": 0}
        self.assertEqual(increment_game_id_iterator(first_game_id_iterator), next_game_id_iterator)

    def test_playoff_last_series_end(self):
        first_game_id_iterator = {"year": 2007,
                                  "season": 3,
                                  "game": 7,
                                  "round": 1,
                                  "series": 8,
                                  "fails": 0}
        next_game_id_iterator = {"year": 2007,
                                 "season": 3,
                                 "game": 1,
                                 "round": 2,
                                 "series": 1,
                                 "fails": 0}
        self.assertEqual(increment_game_id_iterator(first_game_id_iterator), next_game_id_iterator)

    def test_playoff_last_round_end(self):
        first_game_id_iterator = {"year": 2007,
                                  "season": 3,
                                  "game": 7,
                                  "round": 4,
                                  "series": 1,
                                  "fails": 0}
        next_game_id_iterator = {"year": 2008,
                                 "season": 1,
                                 "game": 1,
                                 "round": 1,
                                 "series": 1,
                                 "fails": 0}
        self.assertEqual(increment_game_id_iterator(first_game_id_iterator), next_game_id_iterator)

    def test_preseason_fails_limit(self):
        first_game_id_iterator = {"year": 2007,
                                  "season": 1,
                                  "game": 10,
                                  "round": 1,
                                  "series": 1,
                                  "fails": MAX_FAILS}
        next_game_id_iterator = {"year": 2007,
                                 "season": 2,
                                 "game": 1,
                                 "round": 1,
                                 "series": 1,
                                 "fails": 0}
        self.assertEqual(increment_game_id_iterator(first_game_id_iterator), next_game_id_iterator)

    def test_reg_season_fails_limit(self):
        first_game_id_iterator = {"year": 2007,
                                  "season": 2,
                                  "game": 10,
                                  "round": 1,
                                  "series": 1,
                                  "fails": MAX_FAILS}
        next_game_id_iterator = {"year": 2007,
                                 "season": 3,
                                 "game": 1,
                                 "round": 1,
                                 "series": 1,
                                 "fails": 0}
        self.assertEqual(increment_game_id_iterator(first_game_id_iterator), next_game_id_iterator)

    def test_invalid_game_id_iterator(self):
        bad_game_id_iterator = {"year": 2007,
                                "season": "banana",
                                "game": 1,
                                "series": 1,
                                "fails": 0}
        with self.assertRaises(Exception):
            increment_game_id_iterator(bad_game_id_iterator)

if __name__ == '__main__':
    unittest.main()
