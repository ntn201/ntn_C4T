flock = [5,9,10,3,6,4,2,8,7]
print("Hello, my name is Nguyen and these are my sheeps's size: ", flock, sep = "\n")

_max = 0
for sheep in flock:
    if sheep > _max:
        _max = sheep
print("Now my biggest sheep has size", _max, "let's shear it")
flock[flock.index(_max)] = 8
_max = 0
print("After shearing, here is my flock",flock)
for sheep in flock:
    sheep += 50
print("One month has passed, here is my flock",flock)
for i in range(4):
    for sheep in flock:
        sheep += 50
    print("One month has passed, here is my flock",flock)
    for sheep in flock:
        if sheep > _max:
            _max = sheep
    print("Now my biggest sheep has size", _max, "let's shear it")
    flock[flock.index(_max)] = 8
    _max = 0
    print("After shearing, here is my flock",flock)


