import sys


def main():

    lines = sys.stdin.readlines()
    # file = open(filename, 'r')
    # lines = file.readlines()
    # file.close()
    process(lines)
    # final = delete_node(lines)
    # finalize(final)
    result = []
    temp = []
    limit = lines[0][0]
    lines[0].append('r')
    result.append(lines[0][0] - 1)
    count = 1
    i = 1
    transfer = []
    while i < len(lines):
        if limit == 'end':
            break
        if count <= limit:
            temp.append(lines[i])
            count += 1
            i += 1
        else:
            delete_node(temp, limit)
            limit = lines[i][0]
            lines[i].append('r')
            count = 1

            if limit != 'end':
                result.append(lines[i][0] - 1)
            else:
                result.append(lines[i][0])
                break

            temp.clear()
            i += 1
    print(0)


def delete_node(digraph, order):

    arcs_deleted = 0
    node = len(digraph) - 1
    for i in range(len(digraph) - 1, -1, -1):
        if node == order - 3:
            arcs_deleted += len(digraph[i])
            digraph.pop(i)
            node -= 1
        else:
            for j in range(len(digraph[i]) - 1, -1, -1):
                if digraph[i][j] == order - 3:
                    arcs_deleted += 1
                    digraph[i].pop(j)
                elif digraph[i][j] > order - 3:
                    digraph[i][j] -= 1
            node -= 1
    order -= 1
    digraph.append([arcs_deleted])
    digraph.insert(0, [order])
    for i in range(len(digraph)):
        if digraph[i] == []:
            print("")
        else:
            for j in range(len(digraph[i])):
                if j == len(digraph[i]) - 1:
                    print(digraph[i][j])
                else:
                    print(digraph[i][j], end=" ")

    """
    lines = process(lines)
    order = lines[0][0]
    if order == 'end':
        return lines
    node = 0
    check_remove = order - 3
    arcs_removed = 0
    i = 1
    lines[0][0] -= 1
    while i < len(lines):

        if order == 'end' or order == 0:
            lines = lines[0:i]
            lines[-1] = 0
            break
        elif node == order - 3:

            if lines[i] != ['\n']:
                arcs_removed += len(lines[i])

            lines[i].append('r')

            node += 1
            i += 1
        elif node == order - 1:

            if lines[i + 1] == ['end']:
                if (order - 3) in lines[i]:
                    lines[i].remove(order - 3)
                    arcs_removed += 1

                for j in range(len(lines[i]) - 1, -1, -1):
                    if lines[i][j] > (order - 3):
                        lines[i][j] -= 1
                lines.insert(i + 1, arcs_removed)

                break

            if (order - 3) in lines[i]:
                lines[i].remove(order - 3)
                arcs_removed += 1

            for j in range(len(lines[i]) - 1, -1, -1):
                if lines[i][j] > (order - 3):
                    lines[i][j] -= 1
            lines.insert(i + 1, arcs_removed)
            order = lines[i + 2][0]
            lines[i + 2][0] -= 1
            i += 3
            node = 0
            arcs_removed = 0
        else:

            if (order - 3) in lines[i]:
                lines[i].remove(order - 3)
                arcs_removed += 1

            for j in range(len(lines[i]) - 1, -1, -1):
                if lines[i][j] > (order - 3):
                    lines[i][j] -= 1

            node += 1
            i += 1

    for i in range(len(lines) - 1, -1, -1):
        try:
            if 'r' in lines[i]:
                lines.pop(i)
        except TypeError:
            continue

    return lines
    """


def process(lines):

    for i in range(len(lines)):
        if lines[i] == '\n':
            lines[i] = []
        elif lines[i] == '0':
            lines[i] = ['end']
        else:
            lines[i] = lines[i].split(' ')
            for j in range(len(lines[i])):
                lines[i][j] = int(lines[i][j])

    return lines


"""
def finalize(lines):
    for i in range(len(lines)):
        if lines[i] == ['\n']:
            lines[i] = [""]
        elif lines[i] == []:
            lines[i] = [""]

    for i in range(len(lines)):
        try:
            for j in range(len(lines[i])):
                if lines[i][j] == 'end':
                    print('0')
                    break
                else:
                    if j == len(lines[i]) - 1:
                        print(lines[i][j])
                    else:
                        print(lines[i][j], end=" ")
        except:
            print(lines[i])
"""

main()
