from city_objects import Car, Road, TrafficLight, CrossRoad, \
    SmartTrafficLightController, SmartTrafficLight, SmartCrossRoad
import random
from copy import deepcopy


class SmartCity:
    VERTICAL_DIR = "v"
    HORIZONTAL_DIR = "h"

    def __init__(self, n, m, roads, cars):
        self.__n = n
        self.__m = m
        self.__pos_to_cross_road = {}
        self.__roads = deepcopy(roads)
        self.__cars = deepcopy(cars)
        self.__cross_roads = []
        self.__input_roads = []
        self.__output_roads = []

    def __clear(self):
        self.__cars_to_road = {}
        self.__road_to_cross_road = {}
        self.__cars = []
        self.__cross_roads = []

    def __initialize_vertical_roads(self):
        diff = 1
        cur_row = -1
        cur_col = 0
        while cur_col < self.__m:
            while -1 <= cur_row + diff <= self.__n:
                new_road_id = len(self.__roads)
                new_road_start_pos = [cur_row, cur_col]
                new_road_end_pos = [cur_row + diff, cur_col]
                new_road_direction = [diff, 0]
                new_road_length = random.randint(10, 40)
                new_road = Road(new_road_id, new_road_start_pos, new_road_end_pos, new_road_direction, new_road_length)
                self.__roads.append(new_road)
                if new_road_start_pos[0] == -1 or new_road_start_pos[0] == self.__n:
                    self.__input_roads.append(new_road)
                if new_road_end_pos[0] == -1 or new_road_end_pos[0] == self.__n:
                    self.__output_roads.append(new_road)
                cur_row += diff
            cur_col += 1
            diff *= -1

    def __initialize_horizontal_roads(self):
        diff = 1
        cur_row = 0
        cur_col = -1
        while cur_row < self.__n:
            while -1 <= cur_col + diff <= self.__m:
                new_road_id = len(self.__roads)
                new_road_start_pos = [cur_row, cur_col]
                new_road_end_pos = [cur_row, cur_col + diff]
                new_road_direction = [0, diff]
                new_road_length = random.randint(10, 40)
                new_road = Road(new_road_id, new_road_start_pos, new_road_end_pos, new_road_direction, new_road_length)
                self.__roads.append(new_road)
                if new_road_start_pos[1] == -1 or new_road_start_pos[1] == self.__m:
                    self.__input_roads.append(new_road)
                if new_road_end_pos[1] == -1 or new_road_end_pos[1] == self.__m:
                    self.__output_roads.append(new_road)
                cur_col += diff
            cur_row += 1
            diff *= -1

    def __initialize_city_roads(self):
        self.__initialize_vertical_roads()
        self.__initialize_horizontal_roads()

    def __find_cross_road_roads(self, i, j):
        vertical_roads = [None, None]
        horizontal_roads = [None, None]
        for road in self.__roads:
            road_start_pos = road.get_road_start_pos()
            road_end_pos = road.get_road_end_pos()
            if road_start_pos[0] == i and road_start_pos[1] == j:
                if road_start_pos[0] == road_end_pos[0]:
                    horizontal_roads[1] = road
                else:
                    vertical_roads[1] = road
            if road_end_pos[0] == i and road_end_pos[1] == j:
                if road_start_pos[0] == road_end_pos[0]:
                    horizontal_roads[0] = road
                else:
                    vertical_roads[0] = road
        return vertical_roads[0], vertical_roads[1], horizontal_roads[0], horizontal_roads[1]

    def __initialize_city_cross_roads(self):
        for i in range(self.__n):
            for j in range(self.__m):
                vertical_in_road, vertical_out_road, horizontal_in_road, horizontal_out_road = \
                    self.__find_cross_road_roads(i, j)
                new_vertical_traffic_light = SmartTrafficLight()
                new_horizontal_traffic_light = SmartTrafficLight()
                new_cross_road = SmartCrossRoad(vertical_in_road, vertical_out_road, horizontal_in_road,
                                                horizontal_out_road, new_vertical_traffic_light,
                                                new_horizontal_traffic_light)
                self.__cross_roads.append(new_cross_road)
                self.__pos_to_cross_road[(i, j)] = new_cross_road

    def __DFS(self, cur_pos, end_pos, cur_path):
        self.__mark[(cur_pos[0], cur_pos[1])] = 1
        if cur_pos[0] == end_pos[0] and cur_pos[1] == end_pos[1]:
            return cur_path
        if cur_pos[1] != -1 and cur_pos[1] != self.__m:
            new_pos = deepcopy(cur_pos)
            new_path = deepcopy(cur_path)
            new_path.append("v")
            death_flag = False
            if cur_pos[1] % 2 == 0:
                if cur_pos[0] == self.__n:
                    death_flag = True
                new_pos[0] += 1
            else:
                if cur_pos[0] == -1:
                    death_flag = True
                new_pos[0] -= 1
            if death_flag is False and (new_pos[0], new_pos[1]) not in self.__mark.keys():
                path_found = self.__DFS(new_pos, end_pos, new_path)
                if path_found != -1:
                    return path_found
        if cur_pos[0] != -1 and cur_pos[0] != self.__n:
            new_pos = deepcopy(cur_pos)
            new_path = deepcopy(cur_path)
            new_path.append("h")
            death_flag = False
            if cur_pos[0] % 2 == 0:
                if cur_pos[1] == self.__m:
                    death_flag = True
                new_pos[1] += 1
            else:
                if cur_pos[1] == -1:
                    death_flag = True
                new_pos[1] -= 1
            if death_flag is False and (new_pos[0], new_pos[1]) not in self.__mark.keys():
                path_found = self.__DFS(new_pos, end_pos, new_path)
                if path_found != -1:
                    return path_found
        return -1

    def __calculate_car_direction(self, start_pos, end_pos):
        self.__mark = {}
        return self.__DFS(start_pos, end_pos, [])

    def __initialize_city_cars(self):
        for car in self.__cars:
            self.__roads[car.get_start_road_id()].add_car(car)

    def __initialize_city_input_output_roads(self):
        for road in self.__roads:
            road_start_pos = road.get_road_start_pos()
            road_end_pos = road.get_road_end_pos()
            if road_start_pos[0] == -1 or road_start_pos[0] == self.__n or \
                    road_start_pos[1] == -1 or road_start_pos[1] == self.__m:
                self.__input_roads.append(road)
            if road_end_pos[0] == -1 or road_end_pos[0] == self.__n or \
                    road_end_pos[1] == -1 or road_end_pos[1] == self.__m:
                self.__output_roads.append(road)

    def initialize_city_objects(self):
        if len(self.__roads) == 0:
            self.__initialize_city_roads()
        else:
            self.__initialize_city_input_output_roads()
        self.__initialize_city_cross_roads()
        self.__initialize_city_cars()

    def forward(self):
        for cross_road in self.__cross_roads:
            cross_road.forward()
        roads_backup = deepcopy(self.__roads)
        for car in self.__cars:
            if car.is_at_destination():
                continue
            if car.is_at_the_end_of_the_road() is True:
                car_cur_pos = car.get_cur_pos()
                car_next_dir = car.get_next_direction()
                car_winker_remaining = car.get_winker()
                cur_cross_road = self.__pos_to_cross_road[(car_cur_pos[0], car_cur_pos[1])]
                if car_winker_remaining is not None and car_winker_remaining == 0:
                    new_road = cur_cross_road.get_output_road(car_next_dir)
                    self.__roads[car.get_road_id()].delete_car(car)
                    new_road.add_car(car)
                    car.start_new_road(new_road.get_road_length(), new_road.get_road_direction(), new_road.get_id())
                    car.set_winker(None)
                elif cur_cross_road.is_road_active(car_next_dir):
                    new_road = cur_cross_road.get_output_road(car_next_dir)
                    self.__roads[car.get_road_id()].delete_car(car)
                    new_road.add_car(car)
                    car.start_new_road(new_road.get_road_length(), new_road.get_road_direction(), new_road.get_id())
                elif car_winker_remaining is None and cur_cross_road.is_road_winker():
                    road_inp1, road_inp2 = cur_cross_road.get_input_roads()
                    cross_road_traffic = roads_backup[road_inp1.get_id()].get_road_cars_cnt() + \
                                         roads_backup[road_inp2.get_id()].get_road_cars_cnt()
                    car.set_winker(2 ** cross_road_traffic)
            car.forward()

    def are_all_cars_at_destination(self):
        for car in self.__cars:
            if car.is_at_destination() is False:
                return False
        return True

    def calculate_all_cars_route_time(self):
        result = 0
        for car in self.__cars:
            result += car.get_route_time()
        return result

    def print_city(self):
        for car in self.__cars:
            print(car)
