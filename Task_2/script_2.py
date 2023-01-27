def id_gen(prefix=""):
    i = 1
    while True:
        if prefix == "":
            yield str(i)
        else:
            yield f"{prefix}-{i}"
        i += 1


f = id_gen()
print(next(f))
print(next(f))
print(next(f))

f = id_gen("ID")
print(next(f))
print(next(f))
print(next(f))

f = id_gen("INTERNAL-ID")
print(next(f))
print(next(f))
print(next(f))
