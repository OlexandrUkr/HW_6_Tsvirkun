def coroutine(func):
    def wrap(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen

    return wrap


@coroutine
def average():
    n = 0
    suma = 0
    sr = 0
    while True:
        a = yield sr
        suma += a
        n += 1
        sr = suma / n


ser = average()
print(ser.send(10))
print(ser.send(5))
print(ser.send(5))
print(ser.send(1))
