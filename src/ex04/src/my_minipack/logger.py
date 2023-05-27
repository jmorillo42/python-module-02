import functools
import getpass
import time
from random import randint


def log(func):
    @functools.wraps(func)
    def wrapper(*args):
        user_name = getpass.getuser()
        func_name = func.__name__.replace("_", " ").title()
        exec_time = time.time_ns()
        result = func(*args)
        exec_time = (time.time_ns() - exec_time) / 1000000000
        if exec_time < 0.001:
            unit = 'ms'
            exec_time = exec_time * 1000
        else:
            unit = 's'
        with open('machine.log', 'a') as log_file:
            log_file.write(f'({user_name})Running: {func_name:18} [ exec-time = {exec_time:.3f} {unit} ]\n')
        return result

    return wrapper


class CoffeeMachine:
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")
