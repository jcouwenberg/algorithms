import sys
import math
import heapq


def main():
    lines = sys.stdin.readlines()
    # file = open(filename, 'r')
    # lines = file.readlines()
    # file.close()
    process(lines)
    for line in lines:
        l = create_adjlist(line)
        distance = Dijkstra(l)
        if distance[-1] == math.inf:
            print(-1)
        else:
            print('{:.2f}'.format(distance[-1]))


def process(lines):
    for i in range(len(lines)):
        lines[i] = lines[i].split(',')
        lines[i].pop(0)


def create_adjlist(line):
    result = []
    for i in range(0, len(line), 2):
        source = [float(line[i]), float(line[i+1])]
        temp = []
        node = 0
        for j in range(0, len(line), 2):
            if j != i:
                boulder = [float(line[j]), float(line[j+1])]
                if math.dist(source, boulder) <= 100:
                    temp.append((node, math.dist(source, boulder)))
            node += 1
        result.append(temp)
    return result


def Dijkstra(adj_list):
    seen = set()
    dist = [math.inf] * len(adj_list)
    dist[0] = 0
    priority_heap = []
    heapq.heappush(priority_heap, (0, 0))
    while len(priority_heap) > 0:
        current_node, d = heapq.heappop(priority_heap)
        seen.add(d)
        for neighbour, n_dist in adj_list[current_node]:
            if neighbour not in seen:
                distance = d + n_dist
                if distance < dist[neighbour]:
                    dist[neighbour] = distance
                    heapq.heappush(priority_heap, (neighbour, distance))
    return dist


main()
