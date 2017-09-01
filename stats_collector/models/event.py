class Event:
    def __init__(self, **kwargs):
        self.seq = kwargs['seq']
        self.per = kwargs['per']
        self.str = kwargs['str']
        self.time_elapsed = kwargs['time_elapsed']
        self.time_remaining = kwargs['time_remaining']
        self.type = kwargs['type']
        self.desc = kwargs['desc']
        self.visitor_on_ice = kwargs['visitor_on_ice']
        self.home_on_ice = kwargs['home_on_ice']

    def __repr__(self):
        return '<Event %s at %s period %s>' % (self.type, self.time_elapsed, self.per)
