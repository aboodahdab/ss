import argparse


#  i will write everything i have seen from internet iwill not use ai but maybe some internet#


def readFile(filename):
    # i saw  file word in 17 line of code from my other python file so i know what it does but i forgot it okay ? counts as ai
    with open(filename, "r") as file:
        if file.readlines() == []:
            print("nothing to print")
        return file.readlines()


def show(data):
    for i, v in enumerate(data):
        print(i, v)


def addItemToShoplist(value):
    # i saw file word in 17 line of code from my other python file so i know what it does but i forgot it okay ?counts as ai
    with open("abood.txt", "a") as file:
        if readFile("abood.txt") == []:
            file.write(f"{value}")
            return
        file.write(f"\n{value}")


def add_a_new_score(obj):
    # i saw file word in 17 line of code from my other python file so i know what it does but i forgot it okay ?counts as ai
    with open("abood.txt", "a") as file:
        for key, value in obj.items():
            print(key, value)
            if readFile("abood.txt") == []:
                file.write(f"{key}:{value}")
                return
            file.write(f"\n{key}:{value}")


def remove_line(line, filename):
    data = readFile(filename)

    if data == []:
        print("nothing to remove")
        return

    data[line-1] = ""
    with open(filename, "w")as file:
        for word in data:
            file.write(word)


def add_a_new_contact(name, value):
    # i saw file word in 17 line of code from my other python file so i know what it does but i forgot it okay ?counts as ai
    with open("contatcs.txt", "a") as file:
        if readFile("contatcs.txt") == []:
            file.write(f"{name}:{value}")
            return
        file.write(f"\n{name}:{value}")


def handle(args):
    command = args.command
    filename = "abood.txt"
    if command == "read":
        if args.choices == "contacts":
            filename = "contatcs.txt"
            show(readFile(filename))
            return

        show(readFile(filename))
    if command == "contacts":
        add_a_new_contact(args.name, args.phoneNum)

    if command == "remove":
        if args.choices == "contacts":
            filename = "contatcs.txt"
            remove_line(args.line, filename)
            return
        filename = "abood.txt"
        remove_line(args.line, filename)
    if command == "shoplist":
        addItemToShoplist(args.ingredient)

    if command == "scoreboard":
        add_a_new_score({f"{args.name}": args.value})


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command")
    sub.required = True
    remove = sub.add_parser("remove")
    remove.add_argument("choices", choices=[
                        "scoreboard", "contacts", "shoplist"])
    remove.add_argument("line", type=int)
    read = sub.add_parser("read")
    read.add_argument("choices", choices=[
                      "scoreboard", "contacts", "shoplist"])
    contacts = sub.add_parser("contacts")
    contacts.add_argument("name", type=str)
    contacts.add_argument("phoneNum", type=int)
    scoreboard = sub.add_parser(
        "scoreboard")
    scoreboard.add_argument("name", type=str)
    scoreboard.add_argument("value", type=int)
    shoplist = sub.add_parser(
        "shoplist")
    shoplist.add_argument("ingredient", type=str)
    args = parser.parse_args()
    handle(args)
# just for pull requests 2
