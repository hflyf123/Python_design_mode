def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
if __name__ == '__main__':
    for i in fab(5):
        print(i)
