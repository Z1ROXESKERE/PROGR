def avergens(*args):
    if not args:
        return 0
    a =sum(args)
    b = len(args)
    c = a/ b
    return c

if __name__ == "__main__":
    result = avergens(4, 6, 7, 9, 3, 2, 10)
    print(f"Среднее арифметическое: {result}")