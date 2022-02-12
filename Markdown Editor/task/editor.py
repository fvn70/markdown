
cmd_set = set("plain bold italic header link inline-code ordered-list unordered-list new-line !help !done".split())
text = ""
while True:
    cmd = input("Choose a formatter: ")
    if cmd not in cmd_set:
        print("Unknown formatting type or command")
    elif cmd == "!help":
        print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
        print("Special commands: !help !done")
    elif cmd == "!done":
        break
