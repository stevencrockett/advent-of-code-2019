
def main():
    with open('day-1/day-1_input.txt') as input:
        fuel_per_module = [(int(mass) // 3) - 2 for mass in input]
        print(sum(fuel_per_module))

if __name__ == '__main__':
    main()