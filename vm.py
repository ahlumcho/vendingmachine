change = 0

def run(raw):
    global change
    change = 0

    tokens = raw.split(" ")
    cmd, params = tokens[0], tokens[1:]


    if cmd == "잔액":
        return "잔액은 " + str(change) + "원입니다"
    else:
        coin = params[0]
        change += int(params[0])
        return coin + "원을 넣었습니다"
