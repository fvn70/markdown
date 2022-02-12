def plain():
    return input("Text: ")


def bold():
    return "**" + input("Text: ") + "**"


def italic():
    return "*" + input("Text: ") + "*"


def header():
    while True:
        level = int(input("Level: "))
        if level in range(1, 7):
            break
        else:
            print("The level should be within the range of 1 to 6")
    txt = input("Text: ")
    return "#" * level + " " + txt + "\n"


def link():
    label = input("Label: ")
    url = input("URL: ")
    return "[" + label + "](" + url + ")"


def inline_code():
    txt = input("Text: ")
    return "`" + txt + "`"


def new_line():
    return "\n"


def m_list(order=None):
    ord = False if order is None else order
    while True:
        nums = int(input("Number of rows: "))
        if nums > 0:
            break
        else:
            print("The number of rows should be greater than zero")
    rows = read_rows(nums)
    digs = [n for n in range(nums)]
    if ord:
        txt = list(map(lambda n, s: f"{n + 1}. " + s, digs, rows))
    else:
        txt = list(map(lambda s: "* " + s, rows))
    return "\n".join(txt)


def read_rows(n):
    lst = []
    for i in range(n):
        lst.append(input(f"Row #{i + 1}: "))
    return lst


cmd_set = set("plain bold italic header link inline-code ordered-list unordered-list new-line !help !done".split())
text = ""
while True:
    cmd = input("Choose a formatter: ")
    if cmd not in cmd_set:
        print("Unknown formatting type or command")
    elif cmd == "!help":
        print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
        print("Special commands: !help !done")
    elif cmd.endswith("-list"):
        text += m_list(cmd.startswith("ordered")) + "\n"
        print(text)
    elif cmd == "!done":
        file = open("output.md", "w")
        file.write(text)
        file.close()
        break
    else:
        cmd = cmd.replace("-", "_")
        text += eval(cmd + "()")
        print(text)
