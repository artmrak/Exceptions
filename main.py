result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError
    except ValueError:
        if b > 100:
            raise IndexError
    except TypeError:
        raise TypeError("Недопустимые типы аргументов для функции")
    except ZeroDivisionError:
        return a / b

data = {(10, 2): 2, (2, 5): 5, (123, 4): 4, (18, 0): 0, ((), 15): 15, (8, 4): 4}

for key in data:
    try:
        res = divider(key[0], data[key])
        result.append(res)
    except (ValueError, IndexError, TypeError) as e:
        print(f"Error: {e}")

print(result)