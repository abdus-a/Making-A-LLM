class SimpleRandom:
    def __init__(self, seed):
        self.state = seed 
    
    def next_number(self):
        self.state = (self.state * 1664525 + 1013904223) % 4294967296

        return self.state / 4294967296 - 0.5
    