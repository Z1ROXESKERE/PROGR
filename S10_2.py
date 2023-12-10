with open("empty_rabota.txt", "w") as file:
    pass

with open("data_rabota.txt", "w") as file:
    file.write("ERROR")

def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            data = file.read()
            if not data:
                raise Exception("Файл пуст")
            else:
                print(data)
    except Exception as e:
        print(e)

read_file("empty_rabota.txt")

read_file("data_rabota.txt")