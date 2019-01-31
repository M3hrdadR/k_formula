from graph import Graph


def graph_create(m):
    g = Graph(m)
    g.create_matrix()
    return g


def graph_read(g):
    i = j = 0
    while i != -1 and j != -1:
        print("Enter the name of  two vertices that are connected in your graph (i j) :")
        i, j = input().split()
        i = int(i)
        j = int(j)
        if i != -1 and j != -1:
            g.connect(i, j)
    return g


def first_step(matrix):
    Lst = []
    for i in range(len(matrix)):
        tmp = ''
        tmp_2 = ''
        count = 0
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                tmp = tmp + str(j)
                count += 1
        for _ in range(count):
            tmp_2 += '*'
        if tmp:
            Lst.append(tmp_2 + str(i) + tmp)
    return Lst


def longest_element(lst):
    m = -1
    index = -1
    for i in range(len(lst)):
        if len(lst[i]) > m:
            m = len(lst[i])
            index = i
    return index


def find_another_element(lst, index, element):
    for j in range(len(lst)):
        middle = len(lst[j]) // 2
        if index != j and lst[j][middle] == element:
            return j
    return -1


def replace(lst, index_of_longest, index_for_replacement, element_index):
    # for _ in range(x-1):
    #     tmp += ' '
    lst[index_of_longest] = lst[index_of_longest][:element_index] + lst[index_for_replacement] + \
                            lst[index_of_longest][element_index + 1:]
    size = len(lst[index_for_replacement])
    del (lst[index_for_replacement])
    return size


def k_formula(lst):
    while len(lst) > 1:
        index = longest_element(lst)
        mid = len(lst[index]) // 2
        for i in range(mid+1, len(lst[index])):
            index_for_replace = find_another_element(lst, index, lst[index][i])
            if index_for_replace != -1:
                print("OK")
                size = replace(lst, index, index_for_replace, i)
                i += size // 2 + 1
                if index > index_for_replace:
                    index -= 1
            if i >= len(lst[index]):
                break
            print(lst[index])
    print(lst)


def making_graph(formula):
    lst = []
    while len(formula) != 1:
        star_count = 0
        star_index = -1
        while formula[star_index] != '*':
            star_index -= 1
        mid_char_index = star_index + 1
        while formula[star_index] == '*':
            star_count += 1
            star_index -= 1
            if star_index < -1 * len(formula):
                break
        star_index += 1
        tmp_index = mid_char_index + 1
        x = star_count
        while x != 0:
            lst.append(formula[mid_char_index] + formula[tmp_index])
            tmp_index += 1
            x -= 1
        formula = formula[:star_index] + formula[mid_char_index] + formula[star_index + 2*star_count + len(formula) + 1:]


def start_getting_graph():
    n = int(input('Enter number of vertices: '))
    G = graph_create(n)
    G = graph_read(G)
    M = G.Matrix
    Lst = first_step(M)
    k_formula(Lst)


def start_getting_formula():
    n = int(input("Enter the number of vertices:"))
    formula = input("Enter k_formula: ")
    making_graph(formula, n)
