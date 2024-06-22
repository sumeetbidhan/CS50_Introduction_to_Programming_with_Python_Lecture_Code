def f(*args, **Kwargs):
    print("Named:", Kwargs)
    print("ARGED: ", args)

f(galleons=100, sickles=50, knuts=25)
f(102, 22, 2)