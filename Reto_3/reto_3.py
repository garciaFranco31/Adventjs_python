def envolver(size, char):
    if size < 2:
        print("No se puede")
        return ""

    result = []
    for i in range(size):
        if (i == 0 or i == size-1):
            result.append(char * size)
        else:
            line = char + " " * (size - 2) + char
            result.append(line)

    return "\n".join(result)

print(envolver(4,"*"))
print(envolver(1,"#"))
print(envolver(2,"-"))
