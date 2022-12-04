try:
    raise ExceptionGroup("Описание групп исключений", [
        IndexError("Чет  не тот индекс"),
        ZeroDivisionError("Поделил на ноль?!"),
        TypeError("Что за тип?"),
        IndexError("Это точно тот индекс?"),
        ValueError("Что за значение?"),
    ])
except *ValueError as eg:
    print(f"ValueError: " + ", ".join(str(exc) for exc in eg.exceptions))
except *ZeroDivisionError as eg:
    print(f"ZeroDivisionError: " + ", ".join(str(exc) for exc in eg.exceptions))
except *IndexError as eg:
    print(f"ZeroDivisionError: " + ", ".join(str(exc) for exc in eg.exceptions))
except *TypeError as eg:
    print(f"ZeroDivisionError: " + ", ".join(str(exc) for exc in eg.exceptions))



if __name__ == '__main__':
    raise ExceptionGroup("Описание групп исключений", [
        ZeroDivisionError("Поделил на ноль?!"),
        IndexError("Это точно тот индекс?"),
    ])