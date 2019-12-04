from typing import List
from enum import Enum, auto


def process_wire_path(wire_path: str):
    raw_steps = wire_path.strip().split(',')

    def extract_step(raw_step: str):
        return raw_step[0], int(raw_step[1:])
    return [extract_step(raw_step) for raw_step in raw_steps]


def generate_coordinates_for_path(path):
    x, y = 0, 0
    coordinates = set()
    for direction, distance in path:
        if direction == 'U':
            for i in range(distance):
                y += 1
                coordinates.add((x, y))
        elif direction == 'D':
            for i in range(distance):
                y -= 1
                coordinates.add((x, y))
        elif direction == 'L':
            for i in range(distance):
                x -= 1
                coordinates.add((x, y))
        else:
            for i in range(distance):
                x += 1
                coordinates.add((x, y))
    return coordinates


def main():
    path_to_wire_path = 'day-3/day-3_input.txt'

    with open(path_to_wire_path) as file:
        steps_for_each_wire = [process_wire_path(wire_path) for wire_path in file]

    steps_for_first_wire = steps_for_each_wire[0]
    coordinates_for_first_wire = generate_coordinates_for_path(steps_for_first_wire)

    steps_for_second_wire = steps_for_each_wire[1]
    coordinates_for_second_wire = generate_coordinates_for_path(steps_for_second_wire)

    intersecting_points = coordinates_for_first_wire & coordinates_for_second_wire

    smallest_manhattan_distance_from_origin = min([abs(x) + abs(y) for (x, y) in intersecting_points])
    print(smallest_manhattan_distance_from_origin)


if __name__ == '__main__':
    main()
