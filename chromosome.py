from __future__ import annotations
from numpy.random import randint


class Chromosome:
    def __init__(self, chromosome_length, bounds):
        self.bounds = bounds
        self.chromosome_length = chromosome_length
        self.bits = randint(0, 2, chromosome_length*len(bounds)).tolist()

    def decode(self) -> float:
        decoded = list()
        largest = 2**self.chromosome_length
        for i in range(len(self.bounds)):
            # extract the substring
            start, end = i * \
                self.chromosome_length, (i * self.chromosome_length) + \
                self.chromosome_length
            substring = self.bits[start:end]
            # convert bitstring to a string of chars
            chars = ''.join([str(s) for s in substring])
            # convert string to integer
            integer = int(chars, 2)
            # scale integer to desired range
            value = self.bounds[i][0] + (integer/largest) * \
                (self.bounds[i][1] - self.bounds[i][0])
            # store
            decoded.append(value)
        return decoded

    def score(self, desired_function: function) -> float:
        return desired_function(self.decode())

    def __index__(self):
        return len(self.bits)

    def copy(self) -> Chromosome:
        copy = Chromosome(self.chromosome_length, self.bounds)
        copy.bits = self.bits
        return copy

    def __getitem__(self, key):
        return self.bits[key]

    def __setitem__(self, key, value):
        self.bits[key] = value

    def __iter__(self):
        return iter(self.bits)

    def __str__(self) -> str:
        return str(self.bits)


ChromosomeList = list[Chromosome]
