def students_info(*args):
    info = []
    for i in range(len(args)):
        info.append(args[i])

    return info


print(students_info(["ali", "hassan"], [80, 90]))
