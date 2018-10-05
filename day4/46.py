def decorator_name(func):
    def any_fun():
        print("ask me")

        func()

        print("asking")

    return any_fun

@decorator_name
def question():
    print("ncdnhi")

@decorator_name
def ans():
    print('hudh')

question()
ans()