class Player:
    def __init__(self, fname, lname, number):
        self.fname = fname;
        self.lname = lname;
        self.number = number;

    def __repr__(self):
        return '<Player %s %s, %s>' % (self.lname, self.fname, self.number)
