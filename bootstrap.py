from stats_collector.workflow import get_reports
from stats_collector.iterator import increment_game_id_iterator
from stats_collector.report_parser import parse_game_report

def sample_report():
    return parse_game_report(get_reports(increment_game_id_iterator())[0])
