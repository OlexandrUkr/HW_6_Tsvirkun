class IteratorFib:

    def __init__(self, nmax):
        self.n1 = 0
        self.n2 = 1
        self.max = nmax

    def __iter__(self):
        return self

    def __next__(self):
        self.current = self.n1
        if self.current > self.max:
            raise StopIteration
        self.n0 = self.n1
        self.n1 = self.n2
        self.n2 = self.n0 + self.n2
        return self.current

    def is_odd(self):
        if self.current % 2 == 0:
            return "Число парне"
        else:
            return "Число непарне"


"""
for i in IteratorFib(20):
    print(i)
"""
fib = IteratorFib(255)
print(next(fib))
print(next(fib))
print(fib.is_odd())
print(next(fib))
print(next(fib))
print(next(fib))
print(fib.is_odd())
print(next(fib))
print(next(fib))
print(fib.is_odd())
print(next(fib))
print(next(fib))
