

class Arrow:


    def __init__(self, source, dest, value):

        self.source = source
        self.dest = dest
        self.value = value


    def __str__(self):
        return "Source: %s, dest: %s, value: %s" % (self.source, self.dest, self.value)

    def __eq__(self, other):
        return self.source == other.source and self.dest == other.dest and self.value == other.value
