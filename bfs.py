import sys


def main():
    lines = sys.stdin.readlines()
    # file = open(filename, 'r')
    # lines = file.readlines()
    # file.close()
    process(lines)
    result = temp = []
    limit = lines[0][0]
    lines[0].append('r')
    count = 1
    i = 1
    check = []
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
            result.append(BFS(temp))
            check.append(result[-1])
            temp.clear()
            i += 1

    for i in range(len(check)):
        max_distance = 0
        highest_index = []
        for j in range(len(check[i])):
            if check[i][j] >= max_distance:
                highest_index.append(j)
                max_distance = check[i][j]
        if len(highest_index) == 1:
            print(max_distance, end=" ")
            print(highest_index[0])
        else:
            print(max_distance, end=" ")
            print(max(highest_index))


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


def BFS(digraph):
    queue = []
    color = [-1] * len(digraph)
    pred = [-1] * len(digraph)
    d = [-1] * len(digraph)
    for i in range(len(digraph)):
        color[i] = 'white'
        pred[i] = None
    end = BFS_visit(1, digraph, queue, color, pred, d)
    return end


def BFS_visit(node, digraph, queue, color, pred, d):
    color[node] = 'grey'
    d[node] = 0
    queue.append(node)
    while len(queue) != 0:
        temp = queue[0]
        for i in range(len(digraph[temp])):
            if color[digraph[temp][i]] == 'white':
                color[digraph[temp][i]] = 'grey'
                pred[digraph[temp][i]] = temp
                d[digraph[temp][i]] = d[temp] + 1
                queue.append(digraph[temp][i])
        queue.pop(0)
        color[temp] = 'black'
    return d


main()
