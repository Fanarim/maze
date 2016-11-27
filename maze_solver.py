#!/usr/bin/env python3

import numpy
import maze_generator
import copy


class MazeCell(object):
    """
    Object representing single maze position
    """

    def __init__(self, distance_to_target, direction_to_target, is_reachable,
                 is_wall, is_target):
        self.distance_to_target = distance_to_target
        self.direction_to_target = direction_to_target
        self.is_reachable = is_reachable
        self.is_wall = is_wall
        self.is_target = is_target
        self.is_clear = not is_wall

    def __repr__(self):
        if self.is_wall:
            return '██'
        if self.is_target:
            return 'XX'
        return str(self.distance_to_target) + self.direction_to_target

class MazeSolution(object):
    """
    TODO: Class representing maze solution object
    """
    pass


class MazeSolver(object):
    """
    Class implementing maze solution algorithm.
    TODO: refactor
    TODO: return MaseSolution
    TODO: add borders if not already present
    """

    @staticmethod
    def solution(maze):
        # create array of MazeCells based on input array
        result_maze = numpy.empty(shape=maze.shape, dtype=object)
        result_maze[maze == -1] = MazeCell(0, '0', False, True, False)
        result_maze[maze == 0] = MazeCell(0, '0', False, False, False)
        result_maze[maze == 1] = MazeCell(0, '0', False, False, True)

        # implement Breadth-first search, starting at target
        def is_target_func(cell):
            return cell.is_target

        # get location of target
        is_target = numpy.vectorize(is_target_func)
        target = numpy.where(is_target(result_maze) == True)

        # start traveling through maze
        new_cells_positions = numpy.transpose(target)
        while len(new_cells_positions):
            current_cells_positions = new_cells_positions
            new_cells_positions = []
            print(current_cells_positions)
            for cell_position in current_cells_positions:
                cell = result_maze[cell_position[0], cell_position[1]]

                # get surrounding cells that weren't visited before and are not
                # walls
                cell_up_position = (cell_position[0]-1, cell_position[1])
                cell_down_position = (cell_position[0]+1, cell_position[1])
                cell_right_position = (cell_position[0], cell_position[1]+1)
                cell_left_position = (cell_position[0], cell_position[1]-1)

                if (result_maze[cell_up_position].is_clear and
                        result_maze[cell_up_position].direction_to_target == '0'
                        and not result_maze[cell_up_position].is_target):
                    result_maze[cell_up_position] = MazeCell(cell.distance_to_target + 1,
                                                             'v',
                                                             True,
                                                             False,
                                                             False)
                    new_cells_positions.append(list(cell_up_position))

                if (result_maze[cell_down_position].is_clear and
                        result_maze[cell_down_position].direction_to_target == '0'
                        and not result_maze[cell_down_position].is_target):
                    result_maze[cell_down_position] = MazeCell(cell.distance_to_target + 1,
                                                             '^',
                                                             True,
                                                             False,
                                                             False)
                    new_cells_positions.append(list(cell_down_position))

                if (result_maze[cell_left_position].is_clear and
                        result_maze[cell_left_position].direction_to_target == '0'
                        and not result_maze[cell_left_position].is_target):
                    result_maze[cell_left_position] = MazeCell(cell.distance_to_target + 1,
                                                             '>',
                                                             True,
                                                             False,
                                                             False)
                    new_cells_positions.append(list(cell_left_position))

                if (result_maze[cell_right_position].is_clear and
                        result_maze[cell_right_position].direction_to_target == '0'
                        and not result_maze[cell_right_position].is_target):
                    result_maze[cell_right_position] = MazeCell(cell.distance_to_target + 1,
                                                             '<',
                                                             True,
                                                             False,
                                                             False)
                    new_cells_positions.append(list(cell_right_position))


            print(result_maze)



        return result_maze


def analyze(maze):
    return MazeSolver.solution(maze)


def main():
    maze = maze_generator.generate_maze(14, 7)
    maze = maze_generator.convert_maze(maze)

    solution = analyze(maze)
    # print(solution)


if __name__ == "__main__":
    main()
