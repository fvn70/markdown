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


cmd_set = set("plain bold italic header link inline-code new-line !help !done".split())
text = ""
while True:
    cmd = input("Choose a formatter: ")
    if cmd not in cmd_set:
        print("Unknown formatting type or command")
    elif cmd == "!help":
        print("Available formatters: plain bold italic header link inline-code new-line")
        print("Special commands: !help !done")
    elif cmd == "!done":
        break
    else:
        cmd = cmd.replace("-", "_")
        text += eval(cmd + "()")
        print(text)
