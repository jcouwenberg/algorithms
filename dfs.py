import sys
import io

color = [None]
seen = [None]
done = [None]
pred = [None]


def main(filename):
    # lines = sys.stdin.readlines()
    file = open(filename, 'r')
    lines = file.readlines()
    result = []
    process(lines)
    temp = []
    limit = lines[0][0]
    lines[0].append('r')
    count = 1
    i = 1
    file.close()
    check = []
    cross_arcs = 0
    back_arcs = 0
    while i < len(lines):
        if limit == 'end':
            break
        if count <= limit:
            temp.append(lines[i])
            count += 1
            i += 1
        else:
            limit = lines[i][0]
            lines[i].append('r')
            count = 1
            transfer = temp
            check.append(transfer)
            print(temp)
            result.append(DFS_traverse(temp, back_arcs, cross_arcs))
            temp.clear()
            i += 1

    orders = []
    for i in range(len(lines) - 1, -1, -1):
        if 'r' in lines[i]:
            orders.append(lines.pop(i))
    orders.reverse()
    orders.pop(-1)
    dg = 0
    order = orders[dg][0]
    node = 0
    seen = result[dg][1]
    done = result[dg][2]
    pred = result[dg][0]

    for i in range(len(lines)):
        if node == order - 1:
            for j in range(len(lines[i])):
                if seen[lines[i][j]] < seen[node] < done[node] < done[lines[i][j]]:
                    back_arcs += 1
                elif seen[lines[i][j]] < done[lines[i][j]] < seen[node] < done[node]:
                    cross_arcs += 1
            print(back_arcs, end=" ")
            print(cross_arcs)
            if dg == len(orders) - 1:
                break
            dg += 1
            order = orders[dg][0]
            node = 0
            seen = result[dg][1]
            done = result[dg][2]
            back_arcs = 0
            cross_arcs = 0
        else:
            for j in range(len(lines[i])):
                if seen[lines[i][j]] < seen[node] < done[node] < done[lines[i][j]]:
                    back_arcs += 1
                elif seen[lines[i][j]] < done[lines[i][j]] < seen[node] < done[node]:
                    cross_arcs += 1
            node += 1


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


def DFS_traverse(digraph, back_arcs, cross_arcs):
    color = [-1] * len(digraph)
    pred = [-1] * len(digraph)
    seen = [-1] * len(digraph)
    done = [-1] * len(digraph)
    time = [0]
    for i in range(len(digraph)):
        color[i] = 'white'
        pred[i] = None

    for j in range(len(digraph)):
        if color[j] == 'white':
            DFS_visit(j, digraph, time, color, pred,
                      seen, done, back_arcs, cross_arcs)

    return [pred, seen, done]


def DFS_visit(node, digraph, time, color, pred, seen, done, back_arcs, cross_arcs):
    color[node] = 'grey'
    seen[node] = time[-1]
    time.append(time[-1] + 1)
    if digraph[node] != []:
        for i in range(len(digraph[node])):
            if color[digraph[node][i]] == 'white':
                pred[digraph[node][i]] = node
                DFS_visit(digraph[node][i], digraph,
                          time, color, pred, seen, done, back_arcs, cross_arcs)

    color[node] = 'black'
    done[node] = time[-1]
    time.append(time[-1] + 1)


main("samplein.txt")
