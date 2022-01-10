# python3
import sys


def compute_min_refills(distance, tank, stops):
    def compute_min_refills_inner(stops, previous_stop_position, number_of_moves):
        if len(stops) == 0:
            return number_of_moves

        if stops[0] > (previous_stop_position + tank):
            return -1

        number_of_gas_stations_to_skip = -1

        # stops = [10, 20, 30]
        # tank = 45

        # stops = [20, 30]
        for i in range(len(stops)):
            if stops[i] >= (tank + previous_stop_position):
                previous_stop_position = stops[i-1]
                break

            if i == len(stops)-1:
                return number_of_moves

            number_of_gas_stations_to_skip = i

        # if number_of_gas_stations_to_skip == -1:
        #     number_of_gas_stations_to_skip = len(stops)

        return compute_min_refills_inner(stops[number_of_gas_stations_to_skip:], previous_stop_position, number_of_moves + 1)

    # write your code here
    stops.append(distance)
    return compute_min_refills_inner(stops, 0, 0)

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
