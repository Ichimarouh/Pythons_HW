# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    speed = 0
    color = ''
    name = ''
    is_police = ''

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Car {self.name} is start driving'

    def stop(self):
        return f'Car {self.name} is stopped'

    def turn(self, direction):
        return f'Car {self.name} is turned {direction}'

    def show_speed(self):
        return self.speed

class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return 'Speed is exceeded'
        else:
            return 'Speed is allowed'

class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return 'Speed is exceeded'
        else:
            return 'Speed is allowed'

class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

sport_car = SportCar(140, 'Blue', 'Ford Mustang', False)
town_car = TownCar(50, 'Black', 'Nissan Leaf', False)
work_car = WorkCar(45, 'Yellow', 'Gazelle Next', False)
police_car = PoliceCar(70, 'White',  'Lada Vesta', True)

print(f'{police_car.go()} with speed {police_car.show_speed()} km/h.')
print(f'{town_car.turn("right")} after {sport_car.stop()}.')
print(f'{police_car.turn("left")}.')
print(f'{sport_car.name} driving {sport_car.show_speed()} km/h.')
print(f'{work_car.name} driving {work_car.show_speed()}.')