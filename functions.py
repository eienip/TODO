def file_read():
    with open("todos.txt", mode="r", encoding="utf-8") as f:
        data = f.read().splitlines()
    return data


def file_write(data):
    with open("todos.txt", mode="w", encoding="utf-8") as f:
        f.write("\n".join(data))
