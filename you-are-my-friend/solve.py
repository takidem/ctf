import ast


def rot13_char(c):
    if "a" <= c <= "z":
        return chr((ord(c) - ord("a") + 13) % 26 + ord("a"))
    if "A" <= c <= "Z":
        return chr((ord(c) - ord("A") + 13) % 26 + ord("A"))
    return c


def rot13(text):
    return "".join(rot13_char(c) for c in text)


def main():
    with open("output.txt", "r", encoding="utf-8") as f:
        cts = ast.literal_eval(f.read().strip())

    known_prefix = "Alpaca{"
    ct_prefix = rot13(known_prefix)

    ct = [ct_prefix[0]]
    for i in range(1, len(cts)):
        ct.append(chr(cts[i] ^ ord(ct[i - 1])))

    ct = "".join(ct)
    key = cts[0] ^ ord(ct[0])
    flag = rot13(ct)

    print(f"{key = }")
    print(f"{ct = }")
    print(f"{flag = }")


if __name__ == "__main__":
    main()