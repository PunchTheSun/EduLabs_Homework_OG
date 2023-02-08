
def inf_fibo(limit: int):
    a = 0
    b = 1
    yield a
    c = a + b

    while c < limit:
        curr_val = c
        c = a + b
        a = b
        b = c
        yield curr_val


if __name__ == "__main__":
    for val in inf_fibo(100):
        print(val)
