class CustomException(Exception):
    pass


def main(a):
    if a < 6:
        raise CustomException("Значение меньше 6")


if __name__ == '__main__':
    main(5)