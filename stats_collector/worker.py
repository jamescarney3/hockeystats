# A Worker instance will be in charge of combining other tools in the project
# for the purpose of fetching, parsing, and storing game data. It will keep a
# reference to a GameIterator instance in order to intelligently iterate over
# available game reports, use url parsing utils to generate game report urls
# using aforementioned GameIterator instance, and use report parsing utils
# (which in turn may leverage models of players, coaches, events, games, and
# teams, to be implemented separately) to parse fetched reports for storage in
# a yet unspecified persistent storage layer

class Worker:
