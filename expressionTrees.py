import sys
# import io


def main():
    lines = sys.stdin.readlines()
    # file = open(filename, 'r')
    # lines = file.readlines()
    # file.close()
    process(lines)
    for i in range(0, len(lines), 2):
        root = lines[i].index(-1)
        lines[i] = create_adjlist(lines[i])
        final = calculate(root, lines[i], lines[i+1])
        print(final)


def calculate(root, array, values):
    if values[root] != '+' and values[root] != '*':
        return values[root]
    child_values = []
    for child in array[root]:
        child_values.append(calculate(child, array, values))
    if values[root] == '+':
        summation = sum(child_values)
        return summation
    else:
        if len(child_values) == 1:
            return child_values[0]
        else:
            product = child_values[0]
            for i in range(1, len(child_values)):
                product *= child_values[i]
            return product


def create_adjlist(line):
    adj_list = []
    for i in range(len(line)):
        adj_list.append([i])
    count = 0
    while count < len(line):
        temp = []
        for i in range(len(line)):
            if line[i] == count:
                temp.append(i)
        adj_list[count] += temp
        count += 1
    for l in adj_list:
        l.pop(0)
    return adj_list


def process(lines):
    for i in range(len(lines)):
        lines[i] = lines[i].split(',')
        if '\n' in lines[i][-1]:
            lines[i][-1] = lines[i][-1][:-1]
        for j in range(len(lines[i])):
            if lines[i][j] not in '+*':
                lines[i][j] = int(lines[i][j])


main()
