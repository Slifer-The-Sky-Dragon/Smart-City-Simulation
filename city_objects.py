from copy import deepcopy


class Car:
    VERTICAL = "v"
    HORIZONTAL = "h"

    def __init__(self, car_id, start_pos, end_pos, path_directions, start_road_id=None, winker_remaining=None):
        self.__id = car_id
        self.__start_road_id = start_road_id
        self.__road_id = start_road_id
        self.__route_time = 0
        self.__start_pos = deepcopy(start_pos)
        self.__cur_pos = deepcopy(start_pos)
        self.__end_pos = end_pos
        self.__road_remaining_length = 0
        self.__road_direction = [0, 0]
        self.__path_directions = path_directions
        self.__cur_direction_ind = -1
        self.__winker_remaining = winker_remaining

    def get_id(self):
        return self.__id

    def get_start_road_id(self):
        return self.__start_road_id

    def get_road_id(self):
        return self.__road_id

    def get_cur_pos(self):
        return self.__cur_pos

    def get_next_direction(self):
        return self.__path_directions[self.__cur_direction_ind + 1]

    def get_route_time(self):
        return self.__route_time

    def set_winker(self, winker_length):
        self.__winker_remaining = winker_length

    def get_winker(self):
        return self.__winker_remaining

    def start_new_road(self, road_length, road_direction, road_id=None):
        self.__road_remaining_length = road_length
        self.__road_direction = road_direction
        self.__road_id = road_id
        self.__cur_direction_ind += 1

    def __move_in_road(self):
        if self.__road_remaining_length == 1:
            self.__cur_pos[0] += self.__road_direction[0]
            self.__cur_pos[1] += self.__road_direction[1]
            self.__road_remaining_length -= 1
        elif self.__road_remaining_length > 0:
            self.__road_remaining_length -= 1
        elif self.__road_remaining_length == 0 and self.__winker_remaining is not None:
            if self.__winker_remaining > 0:
                self.__winker_remaining -= 1

    def forward(self):
        self.__move_in_road()
        self.__route_time += 1

    def is_at_destination(self):
        return self.__cur_pos == self.__end_pos

    def is_at_the_end_of_the_road(self):
        return self.__road_remaining_length == 0

    def __str__(self):
        return f"{str(self.__cur_pos)}, {str(self.__start_pos)}, {str(self.__end_pos)}, {str(self.__path_directions)}, {str(self.__road_remaining_length)}, {self.__winker_remaining}"

    def __repr__(self):
        return f"{str(self.__cur_pos)}, {str(self.__start_pos)}, {str(self.__end_pos)}, {str(self.__path_directions)}, {str(self.__road_remaining_length)}, {self.__winker_remaining}"


class Road:
    def __init__(self, road_id, start_pos, end_pos, road_direction, road_length):
        self.__id = road_id
        self.__start_pos = start_pos
        self.__end_pos = end_pos
        self.__road_direction = road_direction
        self.__road_length = road_length
        self.__cars = []

    def get_id(self):
        return self.__id

    def add_car(self, new_car: Car):
        self.__cars.append(new_car)

    def delete_car(self, car: Car):
        car_ind = 0
        for ind in range(len(self.__cars)):
            cur_car = self.__cars[ind]
            if cur_car.get_id() == car.get_id():
                car_ind = ind
        self.__cars.pop(car_ind)

    def get_road_cars_cnt(self):
        return len(self.__cars)

    def get_road_start_pos(self):
        return self.__start_pos

    def get_road_end_pos(self):
        return self.__end_pos

    def get_road_length(self):
        return self.__road_length

    def get_road_direction(self):
        return self.__road_direction

    def __str__(self):
        return f"({str(self.__start_pos)}, {str(self.__end_pos)}, len= {self.__road_length}, cars={self.__cars})"

    def __repr__(self):
        return f"({str(self.__start_pos)}, {str(self.__end_pos)}, len= {self.__road_length}, cars={self.__cars})"


class TrafficLight:
    GREEN = 0
    RED = 1

    def __init__(self, max_time):
        self.__state = -1
        self.__max_time = max_time
        self.__counter = 0

    def __switch_state(self):
        if self.__state == self.GREEN:
            self.__state = self.RED
        else:
            self.__state = self.GREEN

    def forward(self):
        self.__counter += 1
        if self.__counter == self.__max_time:
            self.__counter = 0
            self.__switch_state()

    def is_green(self):
        return self.__state == self.GREEN

    def set_green(self):
        self.__state = self.GREEN

    def set_red(self):
        self.__state = self.RED


class SmartTrafficLight:
    GREEN = 0
    RED = 1
    YELLOW = 2
    WINKER = 3

    def __init__(self):
        self.__state = -1

    def is_open(self):
        return self.__state == self.GREEN or self.__state == self.YELLOW

    def is_winker(self):
        return self.__state == self.WINKER

    def set_green(self):
        self.__state = self.GREEN

    def set_red(self):
        self.__state = self.RED

    def set_yellow(self):
        self.__state = self.YELLOW

    def set_winker(self):
        self.__state = self.WINKER


class SmartTrafficLightController:
    VERTICAL_ROAD = 1
    CAUTION_V = 2
    HORIZONTAL_ROAD = 3
    CAUTION_H = 4
    WINKER = 5
    WINKER_THRESHOLD = 5

    def __init__(self, vertical_traffic_light, horizontal_traffic_light, max_count):
        self.__vertical_traffic_light = vertical_traffic_light
        self.__horizontal_traffic_light = horizontal_traffic_light
        self.__state = self.VERTICAL_ROAD
        self.__last_vertical_road_max_count = max_count
        self.__last_vertical_car_cnt = 30
        self.__last_horizontal_road_max_count = max_count
        self.__last_horizontal_car_cnt = 30
        self.__max_count = max_count
        self.__counter = 0

    def forward(self, cnt_v, cnt_h):
        next_state = self.VERTICAL_ROAD
        if self.__state == self.VERTICAL_ROAD:
            if self.__counter < self.__max_count - 3:
                self.__vertical_traffic_light.set_green()
                self.__horizontal_traffic_light.set_red()
                self.__counter += 1
                next_state = self.VERTICAL_ROAD
            elif self.__max_count - 3 <= self.__counter < self.__max_count:
                self.__vertical_traffic_light.set_yellow()
                self.__horizontal_traffic_light.set_red()
                self.__last_vertical_road_max_count = self.__max_count
                self.__counter += 1
                next_state = self.CAUTION_V
        if self.__state == self.CAUTION_V:
            if self.__counter < self.__max_count:
                self.__vertical_traffic_light.set_yellow()
                self.__horizontal_traffic_light.set_red()
                self.__counter += 1
                next_state = self.CAUTION_V
            elif self.__counter >= self.__max_count and (cnt_v + cnt_h) >= self.WINKER_THRESHOLD:
                self.__vertical_traffic_light.set_red()
                self.__horizontal_traffic_light.set_green()
                self.__counter = 0
                self.__max_count = max(5, min(30, self.__last_horizontal_road_max_count +
                                              (cnt_h - self.__last_horizontal_car_cnt)))
                self.__last_horizontal_car_cnt = cnt_h
                next_state = self.HORIZONTAL_ROAD
            elif self.__counter >= self.__max_count and (cnt_v + cnt_h) < self.WINKER_THRESHOLD:
                self.__vertical_traffic_light.set_winker()
                self.__horizontal_traffic_light.set_winker()
                self.__counter = 0
                self.__last_horizontal_car_cnt = cnt_h
                self.__last_vertical_car_cnt = cnt_v
                self.__last_vertical_road_max_count = 5
                self.__last_horizontal_road_max_count = 5
                next_state = self.WINKER
        if self.__state == self.HORIZONTAL_ROAD:
            if self.__counter < self.__max_count - 3:
                self.__vertical_traffic_light.set_red()
                self.__horizontal_traffic_light.set_green()
                self.__counter += 1
                next_state = self.HORIZONTAL_ROAD
            elif self.__max_count - 3 <= self.__counter < self.__max_count:
                self.__vertical_traffic_light.set_red()
                self.__horizontal_traffic_light.set_yellow()
                self.__counter += 1
                self.__last_horizontal_road_max_count = self.__max_count
                next_state = self.CAUTION_H
        if self.__state == self.CAUTION_H:
            if self.__counter < self.__max_count:
                self.__vertical_traffic_light.set_red()
                self.__horizontal_traffic_light.set_yellow()
                self.__counter += 1
                next_state = self.CAUTION_H
            elif self.__counter >= self.__max_count and (cnt_v + cnt_h) >= self.WINKER_THRESHOLD:
                self.__vertical_traffic_light.set_green()
                self.__horizontal_traffic_light.set_red()
                self.__counter = 0
                self.__max_count = max(5, min(30, self.__last_vertical_road_max_count +
                                              (cnt_v - self.__last_vertical_car_cnt)))
                self.__last_vertical_car_cnt = cnt_v
                next_state = self.VERTICAL_ROAD
            elif self.__counter >= self.__max_count and (cnt_v + cnt_h) < self.WINKER_THRESHOLD:
                self.__vertical_traffic_light.set_winker()
                self.__horizontal_traffic_light.set_winker()
                self.__counter = 0
                self.__last_horizontal_car_cnt = cnt_h
                self.__last_vertical_car_cnt = cnt_v
                self.__last_vertical_road_max_count = 5
                self.__last_horizontal_road_max_count = 5
                next_state = self.WINKER
        if self.__state == self.WINKER:
            if cnt_h + cnt_v < self.WINKER_THRESHOLD:
                self.__vertical_traffic_light.set_winker()
                self.__horizontal_traffic_light.set_winker()
                self.__last_vertical_car_cnt = cnt_v
                self.__last_horizontal_car_cnt = cnt_h
                next_state = self.WINKER
            elif cnt_h + cnt_v >= self.WINKER_THRESHOLD and cnt_v > cnt_h:
                self.__vertical_traffic_light.set_green()
                self.__horizontal_traffic_light.set_red()
                self.__counter = 0
                self.__max_count = max(5, min(30, self.__last_vertical_road_max_count +
                                              (cnt_v - self.__last_vertical_car_cnt)))
                self.__last_vertical_car_cnt = cnt_v
                next_state = self.VERTICAL_ROAD
            elif cnt_h + cnt_v >= self.WINKER_THRESHOLD and cnt_v <= cnt_h:
                self.__vertical_traffic_light.set_red()
                self.__horizontal_traffic_light.set_green()
                self.__counter = 0
                self.__max_count = max(5, min(30, self.__last_horizontal_road_max_count +
                                              (cnt_h - self.__last_horizontal_car_cnt)))
                self.__last_horizontal_car_cnt = cnt_h
                next_state = self.HORIZONTAL_ROAD

        self.__state = next_state


class CrossRoad:
    def __init__(self, vertical_in_road: Road, vertical_out_road: Road, horizontal_in_road: Road,
                 horizontal_out_road: Road, vertical_traffic_light: TrafficLight,
                 horizontal_traffic_light: TrafficLight):
        self.__vertical_in_road = vertical_in_road
        self.__vertical_out_road = vertical_out_road
        self.__horizontal_in_road = horizontal_in_road
        self.__horizontal_out_road = horizontal_out_road
        self.__vertical_traffic_light = vertical_traffic_light
        self.__vertical_traffic_light.set_green()
        self.__horizontal_traffic_light = horizontal_traffic_light
        self.__horizontal_traffic_light.set_red()

    def forward(self):
        self.__vertical_traffic_light.forward()
        self.__horizontal_traffic_light.forward()

    def is_road_active(self, direction):
        if direction == "v":
            return self.__vertical_traffic_light.is_green()
        else:
            return self.__horizontal_traffic_light.is_green()

    def get_output_road(self, direction):
        if direction == "v":
            return self.__vertical_out_road
        else:
            return self.__horizontal_out_road

    def __str__(self):
        result = "{\n"
        result += f"Vertical Road In: {self.__vertical_in_road}\n"
        result += f"Vertical Road Out: {self.__vertical_out_road}\n"
        result += f"Horizontal Road In: {self.__horizontal_in_road}\n"
        result += f"Horizontal Road Out: {self.__horizontal_out_road}\n"
        result += "}\n"
        return result

    def __repr__(self):
        result = "{\n"
        result += f"Vertical Road In: {self.__vertical_in_road}\n"
        result += f"Vertical Road Out: {self.__vertical_out_road}\n"
        result += f"Horizontal Road In: {self.__horizontal_in_road}\n"
        result += f"Horizontal Road Out: {self.__horizontal_out_road}\n"
        result += "}\n"
        return result


class SmartCrossRoad:
    def __init__(self, vertical_in_road: Road, vertical_out_road: Road, horizontal_in_road: Road,
                 horizontal_out_road: Road, vertical_traffic_light: SmartTrafficLight,
                 horizontal_traffic_light: SmartTrafficLight):
        self.__vertical_in_road = vertical_in_road
        self.__vertical_out_road = vertical_out_road
        self.__horizontal_in_road = horizontal_in_road
        self.__horizontal_out_road = horizontal_out_road
        self.__vertical_traffic_light = vertical_traffic_light
        self.__horizontal_traffic_light = horizontal_traffic_light
        self.__traffic_light_controller = SmartTrafficLightController(self.__vertical_traffic_light,
                                                                      self.__horizontal_traffic_light, 30)

    def forward(self):
        self.__traffic_light_controller.forward(self.__vertical_in_road.get_road_cars_cnt(),
                                                self.__horizontal_in_road.get_road_cars_cnt())

    def is_road_active(self, direction):
        if direction == "v":
            return self.__vertical_traffic_light.is_open()
        else:
            return self.__horizontal_traffic_light.is_open()

    def is_road_winker(self):
        return self.__vertical_traffic_light.is_winker()

    def get_traffic_value(self):
        return self.__horizontal_in_road.get_road_cars_cnt() + self.__vertical_in_road.get_road_cars_cnt()

    def get_output_road(self, direction):
        if direction == "v":
            return self.__vertical_out_road
        else:
            return self.__horizontal_out_road

    def get_input_roads(self):
        return self.__vertical_in_road, self.__horizontal_in_road

    def __str__(self):
        result = "{\n"
        result += f"Vertical Road In: {self.__vertical_in_road}\n"
        result += f"Vertical Road Out: {self.__vertical_out_road}\n"
        result += f"Horizontal Road In: {self.__horizontal_in_road}\n"
        result += f"Horizontal Road Out: {self.__horizontal_out_road}\n"
        result += "}\n"
        return result

    def __repr__(self):
        result = "{\n"
        result += f"Vertical Road In: {self.__vertical_in_road}\n"
        result += f"Vertical Road Out: {self.__vertical_out_road}\n"
        result += f"Horizontal Road In: {self.__horizontal_in_road}\n"
        result += f"Horizontal Road Out: {self.__horizontal_out_road}\n"
        result += "}\n"
        return result
