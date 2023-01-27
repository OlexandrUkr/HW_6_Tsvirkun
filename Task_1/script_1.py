class IteratorFib:

    def __init__(self, nmax):
        self.max = nmax

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        return self

    def __next__(self):
        current = self.n1
        if current > self.max:
            raise StopIteration
        self.n0 = self.n1
        self.n1 = self.n2
        self.n2 = self.n0 + self.n2
        if current % 2 == 0:
            return f"{current} - парне число"
        return current


for i in IteratorFib(255):
    print(i)
