from city import City
from smart_city import SmartCity
from copy import deepcopy
from tqdm import tqdm
import matplotlib.pyplot as plt
import numpy as np

EXP_NUM = 3


def make_plot(normal_city_results, smart_city_results):
    grid = np.arange(300, 1001, 100)
    plt.plot(grid, normal_city_results, 'r')
    plt.plot(grid, smart_city_results, 'g')
    plt.legend(["Normal City", "Smart City"], loc="lower right")
    plt.show()


normal_city_results = []
smart_city_results = []

for car_cnt in tqdm(range(300, 1001, 100)):
    normal_city_sum = 0.0
    smart_city_sum = 0.0
    for j in tqdm(range(EXP_NUM)):
        my_city = City(5, 5)
        city_roads, city_cars = my_city.initialize_city_objects(car_cnt)
        city_roads_copy = deepcopy(city_roads)
        city_cars_copy = deepcopy(city_cars)
        while my_city.are_all_cars_at_destination() is False:
            my_city.forward()
        normal_city_cars_all_route_time = my_city.calculate_all_cars_route_time()
        normal_city_sum += normal_city_cars_all_route_time

        my_smart_city = SmartCity(5, 5, city_roads_copy, city_cars_copy)
        my_smart_city.initialize_city_objects()
        while my_smart_city.are_all_cars_at_destination() is False:
            my_smart_city.forward()
        smart_city_cars_all_route_time = my_smart_city.calculate_all_cars_route_time()
        smart_city_sum += smart_city_cars_all_route_time
    normal_city_results.append(normal_city_sum / EXP_NUM)
    smart_city_results.append(smart_city_sum / EXP_NUM)

make_plot(normal_city_results, smart_city_results)

