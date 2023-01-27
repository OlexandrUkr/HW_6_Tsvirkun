def progression_gen(d):
    print("Start")
    a = 0
    while True:
        yield a
        a = a + d


gen = progression_gen(4)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
