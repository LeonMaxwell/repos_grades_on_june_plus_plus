def fun1():
    try:
        1/0
    except ZeroDivisionError:
        print("Деление на ноль")


def fun2():
    try:
        l = []
        l[100]
    except IndexError:
        print("Нет такого индекса в списке")


def fun3():
    print(a)


def main():
    fun1()
    fun2()
    fun3()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(str(e))