from contextlib import contextmanager


class File(object):

    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type and exc_tb:
            print(f"{exc_type}: {exc_val}")
        self.file_obj.close()


@contextmanager
def open_file(name):
    file = open(name, "w")
    yield file
    file.close()


def main():
    with File("mytext.txt", "w") as file:
        file.write("Это текст")

    with open_file("mytext.txt") as f:
        f.write("От так вот")


if __name__ == '__main__':
    main()