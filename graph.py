class Graph:
    n = 0
    Matrix = []
    for i in range(n):
        Matrix.append([])

    def __init__(self, n):
        self.n = n

    def create_matrix(self):
        for i in range(self.n + 1):
            self.Matrix.append([])
            for j in range(self.n + 1):
                self.Matrix[i].append(0)

    def connect(self, a, b):
        self.Matrix[a][b] = 1