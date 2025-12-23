code = "[1++][2-][3+][<]"

digits = []
parts = code.strip("[]").split("][")

print(parts)
for part in parts:
    if (part == "<"):
        if digits:
            digits.append(digits[-1])
        else:
            print("no hay nada")
    else:
        num = int(part[0])
        for op in part[1:]:
            if op == "+":
                num = (num + 1) % 10
            elif (op == "-"):
                num = (num-1) % 10
        digits.append(num)
if (len(digits) >= 4):
    print(digits)
