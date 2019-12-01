from typing import List


def get_mass_readings_from_file(path_to_mass_readings: str) -> List[int]:
    with open(path_to_mass_readings) as input:
        return [(int(mass)) for mass in input]


def calculate_fuel_from_mass(mass: int) -> int:
    return (mass // 3) - 2


def calculate_all_fuel_requirements_for_module(mass: int) -> int:
    initial_requirement = calculate_fuel_from_mass(mass)
    extra_requirement = 0

    current_requirement = initial_requirement
    while (extra_fuel := calculate_fuel_from_mass(current_requirement)) > 0:
        extra_requirement += extra_fuel
        current_requirement = extra_fuel

    return initial_requirement + extra_requirement


def main():
    path_to_mass_readings = 'day-1/day-1_input.txt'
    mass_per_module = get_mass_readings_from_file(path_to_mass_readings)

    initial_fuel_per_module = [calculate_fuel_from_mass(mass) for mass in mass_per_module]
    total_initial_fuel = sum(initial_fuel_per_module)

    print(f'Part 1 answer: {total_initial_fuel}')

    total_fuel_per_module = [calculate_all_fuel_requirements_for_module(mass) for mass in mass_per_module]
    total_fuel = sum(total_fuel_per_module)

    print(f'Part 2 answer: {total_fuel}')


if __name__ == '__main__':
    main()
