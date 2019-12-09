from enum import Enum
from Maze2Graph import Maze2Graph
from queue import PriorityQueue
from Utils import ShortestPathBFS


class GraphAlgorithm(Enum):
    ASTAR = 1,
    DIJKSTRA = 2


class Graph:
    def __init__(self, maze, algorithm_type):
        self.MyMaze = maze
        self.graph_nodes, self.graph_edges = Maze2Graph(maze.maze_cells, maze.cell_size).transform2Graph()
        self.graph_algorithm = algorithm_type

    def find_shortest_path(self):
        ## Path for the debugging_level.lvl
        # remove this line when running your code.
        #return [self.graph_nodes[0][0], self.graph_nodes[2][0], self.graph_nodes[1][0], self.graph_nodes[3][0]]
        ########################

        if self.graph_algorithm == GraphAlgorithm.ASTAR:
            return self.__run_astar()

        if self.graph_algorithm == GraphAlgorithm.DIJKSTRA:
            return self.__run_dijkstra()

    def __run_astar(self):
        Distance = []
        Parent = []
        MaxInt = 10e7
        StartNode = 0
        TargetNode = len(self.graph_edges) - 1
        NodesNumber = len(self.graph_edges)

        for i in range(NodesNumber):
            Distance.append(MaxInt)
            Parent.append(-1)

        MyQueue = PriorityQueue()
        Distance[StartNode] = 0
        MyQueue.put((self.graph_nodes[0][1], StartNode))

        while not MyQueue.empty():
            CurrentNode = MyQueue.get()

            if CurrentNode[1] == TargetNode:
                break

            for AdjacentNode in self.graph_edges[CurrentNode[1]]:
                if Distance[AdjacentNode[0]] > Distance[CurrentNode[1]] + AdjacentNode[1]:
                    Distance[AdjacentNode[0]] = Distance[CurrentNode[1]] + AdjacentNode[1]
                    Parent[AdjacentNode[0]] = CurrentNode[1]
                    MyQueue.put((AdjacentNode[1] + self.graph_nodes[AdjacentNode[0]][1], AdjacentNode[0]))

        Path = []
        MyNode = TargetNode
        CurrentParent = Parent[MyNode]
        FinalPath = []
        while CurrentParent != -1:
            Path = ShortestPathBFS.get_shortest_path(self.MyMaze.maze_cells, self.graph_nodes[TargetNode][0],
                                                     self.graph_nodes[CurrentParent][0])
            for i in Path:
                FinalPath.append(i)

            MyNode = CurrentParent
            CurrentParent = Parent[MyNode]

        return FinalPath

    def __run_dijkstra(self):
        Distance = []
        Parent = []
        MaxInt = 10e7
        StartNode = 0
        TargetNode = len(self.graph_edges) - 1
        NodesNumber = len(self.graph_edges)

        for i in range(NodesNumber):
            Distance.append(MaxInt)
            Parent.append(-1)

        MyQueue = PriorityQueue()
        Distance[StartNode] = 0
        MyQueue.put((0, StartNode))

        while not MyQueue.empty():
            CurrentNode = MyQueue.get()

            if CurrentNode[1] == TargetNode:
                break

            for AdjacentNode in self.graph_edges[CurrentNode[1]]:
                if Distance[AdjacentNode[0]] > Distance[CurrentNode[1]] + AdjacentNode[1]:
                    Distance[AdjacentNode[0]] = Distance[CurrentNode[1]] + AdjacentNode[1]
                    Parent[AdjacentNode[0]] = CurrentNode[1]
                    MyQueue.put((AdjacentNode[1],AdjacentNode[0]))

        Path = []
        MyNode = TargetNode
        CurrentParent = Parent[MyNode]
        FinalPath=[]
        while CurrentParent != -1:
            Path = ShortestPathBFS.get_shortest_path(self.MyMaze.maze_cells,self.graph_nodes[TargetNode][0],
                                                            self.graph_nodes[CurrentParent][0])
            for i in Path:
                FinalPath.append(i)

            MyNode = CurrentParent
            CurrentParent = Parent[MyNode]


        return FinalPath


