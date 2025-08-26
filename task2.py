import json
import argparse

JSONFILE = "json.json"
FILE = "abood.txt"


def read_file_txt():
    try:
        with open(FILE, "r") as f:
            data = f.readlines()
            return data
    except FileNotFoundError as e:
        print("error", e)
        return []


def read_file():
    try:
        with open(JSONFILE, "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError as e:
        print("error", e)
        return []
    except json.JSONDecodeError as e:
        print("error", e)
        return []


def history(args):
    arr = read_file_txt()
    if len(arr) >= 10:
        arr.pop(0)
        writeHistory(arr)
    with open(FILE, "a") as f:
        if arr == []:
            f.write(f"{args}")
        else:
            f.write(f"\n{args}")


def writeHistory(data):
    with open(FILE, "w") as f:
        f.writelines(data)


def is_there_a_name(data):
    if not data:
        print("no data")
        return False
    for i in data:
        if "name" in i:
            return True
    print("no name found")
    return False


def get_name(data):
    if is_there_a_name(data):
        for i in data:
            if "name" in i:
                for k in i.items():
                    print("there is a name already", k[1])
                    return k[1]
    return True


def write(data):
    try:
        with open(JSONFILE, "w") as file:
            json.dump(data, file, indent=2)
    except FileNotFoundError as e:
        print("error", e)
        return []
    except json.JSONDecodeError as e:
        print("error", e)
        return []


if not read_file():
    write([])


def set_name(data, name):
    if not is_there_a_name(data):
        data.append({"name": name})
        write(data)
        history(f"User set name to {name}")
        print("name set to", name)
        return name


def change_name(data, name):
    if is_there_a_name(data):
        data.remove({"name": get_name(data)})
        data.append({"name": name})
        write(data)
        history(f"User changed name to {name}")
        print("name set to", name)
        return name
    print("name already set to", get_name(data))


def score_board(data, name, score):
    try:
        data.append({name: score})
        write(data)
        history(f"User added score: {name} {score}")
    except FileNotFoundError as e:
        print("error", e)
        return []


def shoplist(data, name):
    try:
        data.append({"shoplist": name})
        write(data)
        history(f"User added to shoplist: {name}")
    except FileNotFoundError as e:
        print("error", e)
        return []


def show_one(data, key, num):
    if not data:
        print("no data")
        return []
    arr = []
    print("showing", num, key)
    for i in data:
        if key in i:
            arr.append(i)

    if num > len(arr):
        print("out of range")
        print("please go see func showAll".title())
        return []
    print(arr[num-1], "showone")


def showAll(data, key):
    print("showing all", key)
    if not data:
        print("no data")
        return []
    for i in data:
        if key in i:
            print(i)


def printSomething(data):
    if not data:
        print("no data")
        return []
    for i, n in enumerate(data, 1):
        print(i, n)


def delete(data, num):
    if not data:
        print("no data")
        return []
    element = data[num-1]
    data.remove(element)
    write(data)
    print("deleted", element)


def handle(command, args, data):
    if command == "history":
        read_file_txt()
    if command == "my-name-is":
        set_name(data, args.name)
    if command == "change-name":
        change_name(data, args.name)
    if command == "scoreboard":
        score_board(data, args.name, args.score)
    if command == "shoplist":
        shoplist(data, args.name)
    if command == "show-one":
        show_one(data, args.key, args.num)
    if command == "show-all":
        showAll(data, args.key)
    if command == "delete":
        delete(data, args.num)
    if command == "print":
        printSomething(data)
    if command == "what-is-my-name":
        get_name(data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    set_name_parser = sub.add_parser("my-name-is")
    set_name_parser.add_argument("name", type=str, help="Name to set")
    get_name_parser = sub.add_parser("what-is-my-name")
    change_name_parser = sub.add_parser("change-name")
    change_name_parser.add_argument("name", type=str, help="New name to set")
    score_board_parser = sub.add_parser("scoreboard")
    score_board_parser.add_argument("name", type=str, help="Scoreboard name")
    score_board_parser.add_argument("score", type=int, help="Score value")
    shoplist_parser = sub.add_parser("shoplist")
    shoplist_parser.add_argument("name", type=str, help="Shoplist item")
    show_one_parser = sub.add_parser("show-one")
    show_one_parser.add_argument("key", type=str, help="Key to show")
    show_one_parser.add_argument("num", type=int, help="Item number to show")
    show_all_parser = sub.add_parser("show-all")
    show_all_parser.add_argument("key", type=str, help="Key to show all")
    delete_parser = sub.add_parser("delete")
    delete_parser.add_argument("num", type=int, help="Item number to delete")
    print_parser = sub.add_parser("print")
    histroy_parser = sub.add_parser("history")
    args = parser.parse_args()

    handle(args.command, args, read_file())
    print("done")
