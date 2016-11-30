#!/usr/bin/env python3

import numpy
import maze_generator
import copy


class MazeSolution(object):
    """
    TODO: Class representing maze solution object
    """
    def __init__(self, maze_solved):
        self.maze_solved = maze_solved
        self.distances = self._distances()
        self.directions = self._directions()
        self.is_reachable = self._is_reachable()

    def _distances(self):
        return self.maze_solved[:, :, 0]

    def _directions(self):
        return self.maze_solved[:, :, 1]

    def _is_reachable(self):
        return ' ' not in self.maze_solved[:, :, 1]

    def path(self, x, y):
        if self.maze_solved[x, y, 1] == '#' or\
                self.maze_solved[x, y, 1] == ' ':
            raise Exception("Cell is not reachable. ")

        path = []
        current_position = (x, y)
        while self.maze_solved[current_position][1] != 'X':
            path.append(current_position)
            if self.maze_solved[current_position][1] == '>':
                current_position = (current_position[0], current_position[1]+1)
            elif self.maze_solved[current_position][1] == '<':
                current_position = (current_position[0], current_position[1]-1)
            elif self.maze_solved[current_position][1] == '^':
                current_position = (current_position[0]-1, current_position[1])
            elif self.maze_solved[current_position][1] == 'v':
                current_position = (current_position[0]+1, current_position[1])

        path.append(current_position)
        return path


class MazeSolver(object):
    """
    Class implementing maze solution algorithm.
    TODO: add borders if not already present
    """

    @staticmethod
    def solution(maze):
        # create array of MazeCells based on input array
        result_maze = numpy.empty(shape=(maze.shape[0], maze.shape[1], 2), dtype="<U15")

        # directions
        result_maze[(maze == -1, 1)] = '#'  # wall
        result_maze[(maze == 0, 1)] = ' '   # path
        result_maze[(maze == 1, 1)] = 'X'   # target

        # distances
        result_maze[:, :, 0] = '-1'

        # implement Breadth-first search, starting at target
        # get location of target
        target = numpy.where(result_maze == 'X')[:2]

        # start traveling through maze
        new_cells_positions = numpy.transpose(target)
        while len(new_cells_positions):
            current_cells_positions = new_cells_positions
            new_cells_positions = []

            for cell_position in current_cells_positions:
                cell = result_maze[cell_position[0], cell_position[1]]

                # get surrounding cells that weren't visited before and are not
                # walls
                cell_up_position = (cell_position[0]-1, cell_position[1])
                cell_down_position = (cell_position[0]+1, cell_position[1])
                cell_right_position = (cell_position[0], cell_position[1]+1)
                cell_left_position = (cell_position[0], cell_position[1]-1)

                # path up
                if (result_maze[cell_up_position][1] == ' ' and  # is a path
                        result_maze[cell_up_position][0] == '-1'):  # not visited before
                        # set direction
                        result_maze[cell_up_position][1] = 'v'
                        # set distance
                        result_maze[cell_up_position][0] = str(int(cell[0]) + 1)
                        new_cells_positions.append(list(cell_up_position))

                # path down
                if (result_maze[cell_down_position][1] == ' ' and  # is a path
                        result_maze[cell_down_position][0] == '-1'):  # not visited before
                        # set direction
                        result_maze[cell_down_position][1] = '^'
                        # set distance
                        result_maze[cell_down_position][0] = str(int(cell[0]) + 1)
                        new_cells_positions.append(list(cell_down_position))

                # path left
                if (result_maze[cell_left_position][1] == ' ' and  # is a path
                        result_maze[cell_left_position][0] == '-1'):  # not visited before
                        # set direction
                        result_maze[cell_left_position][1] = '>'
                        # set distance
                        result_maze[cell_left_position][0] = str(int(cell[0]) + 1)
                        new_cells_positions.append(list(cell_left_position))

                # path right
                if (result_maze[cell_right_position][1] == ' ' and  # is a path
                        result_maze[cell_right_position][0] == '-1'):  # not visited before
                        # set direction
                        result_maze[cell_right_position][1] = '<'
                        # set distance
                        result_maze[cell_right_position][0] = str(int(cell[0]) + 1)
                        new_cells_positions.append(list(cell_right_position))

        return MazeSolution(result_maze)


def analyze(maze):
    return MazeSolver.solution(maze)


def main():
    maze = maze_generator.generate_maze(14, 7)
    maze = maze_generator.convert_maze(maze)

    solution = analyze(maze)
    print(solution.distances)
    print(solution.directions)
    print(solution.is_reachable)
    print(solution.path(1, 2))

    # print(solution)


if __name__ == "__main__":
    main()
