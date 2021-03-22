import typing


class Foo:

    def __new__(*args, **kwargs) -> object:
        return super(Foo, Foo).__new__(*args, **kwargs)

    def __init__(self, *args, **kwargs) -> None:
        for i in range(11):
            print(i)

def main() -> None:
    f: Foo = Foo()

if __name__ == '__main__':
    main()