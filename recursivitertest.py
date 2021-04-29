def test(a):
    a = a+1
    print(a)
    if a > 10:
        return
    test(a)

test(1)
