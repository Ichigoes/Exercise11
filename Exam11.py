import re
note = input()
new_char = ""

while note != "Last note":

    if note == "Last note":
        break

    pattern = r"(?P<name>^[\!|\@|\#|\$]+|^[A-Z\!|\@|\#|\$\?]+[A-Za-z0-9\!+\@+\#\$\?]+)=(?P<len>\d+)<<(?P<code>\w+)"
    results = re.finditer(pattern, note)

    note = input()

    for result in results:
        if not result and int(result.group("len")) != len(result.group("code")):
            print("Nothing found!")

        else:
            for char in result.group('name'):
                if char.isalpha():
                    new_char += char

            print(f"Coordinates found! {new_char} -> {result.group('code')}")

    new_char = ""
