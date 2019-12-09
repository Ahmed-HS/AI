# todo: get a map as input, transform the map to a graph based on BFS algorithm.
#       For each edge calculate the cost and for each node, calculate the Heuristic
from Maze import MazeCellType
from Utils import ShortestPathBFS
import math
class Maze2Graph:
    def __init__(self, maze_2d, cell_size):
        self.maze = maze_2d
        self.cell_size = cell_size

    def EuclidianDistance(self,Source,Target):
        X1 = Source[0]
        Y1 = Source[1]
        X2 = Target[0]
        Y2 = Target[1]
        return math.sqrt(math.pow(X2 - X1,2) + math.pow(Y2 - Y1,2))

    def transform2Graph(self):
        graph_nodes = [[[row, col], 1] for row in range(len(self.maze)) for col in range(len(self.maze[row]))
                 if self.maze[row][col] == MazeCellType.DOOR]
        start = [[[row, col], 1] for row in range(len(self.maze)) for col in range(len(self.maze[row]))
                 if self.maze[row][col] == MazeCellType.START_DOOR][0]
        target = [[[row, col], 1] for row in range(len(self.maze)) for col in range(len(self.maze[row]))
                 if self.maze[row][col] == MazeCellType.TARGET_DOOR][0]

        graph_nodes.insert(0, start)
        graph_nodes.append(target)

        graph_edges = []

        for i in range(len(graph_nodes)):
            graph_edges.append([])

        ## Student Code: Connect Edges,
        # for each node,
        #   Find the reachable doors. Hint: use BFS on the given array
        #   Add an edge between the current node and each reachable doors
        #
        #
        ##############################################################

        ## Student Code: Calculate H(n)
        #   After adding the edges, loop on the node and calculate the H(n) where n is the node index
        #   H(n) is saved as the second value in the node,
        #   where the first value is its original location in the maze
        #   Hint: H(n) is the euclidian distance between the node and the Target Node
        #
        #
        ##############################################################

        for i in range(len(graph_nodes)):
            graph_nodes[i][1] = self.EuclidianDistance(graph_nodes[i][0], target[0])
            for j in range(len(graph_nodes)):
                if i != j and self.maze[graph_nodes[j][0][0]][graph_nodes[j][0][0]] == MazeCellType.DOOR:
                    ShortestPath = ShortestPathBFS.get_shortest_path(self.maze, graph_nodes[i][0], graph_nodes[j][0])
                    if len(ShortestPath) != 0:
                        graph_edges[i].append((j, len(ShortestPath)))
                        graph_edges[j].append((i, len(ShortestPath)))

        ## Output for Test Case: debugging_level.lvl
        # Comment/remove this line when you are done
        """return graph_nodes, [
            [(2, 2)],
            [(2, 4), (3, 4)]
            , [(0, 2), (1, 4)],
            [(1, 4)]
        ]"""
        #########################################################################################

        return (graph_nodes, graph_edges)
