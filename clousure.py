def main():
    a = 1

    def nested():
        print(a)
    return nested


def make_multiplier(x):
    def multiplier(n):
        return x * n
    
    return multiplier

if __name__ == '__main__':
    my_fun = main()
    my_fun()
    del(main)
    my_fun()

    times10 = make_multiplier(10)
    times4 = make_multiplier(4)

    print(times10(3))
    print(times4(5))
    print(times10(times4(2)))