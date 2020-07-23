class Car:
    """Car class"""
    engine_status = "Off"
    wheels = 4

    def __init__(self, brand, model, wheels):
        """Class constructor"""
        self.brand = brand
        self.model = model
        self.wheels = wheels

    def get_my_car(self):

        self.my_car = self.brand + self.model

    def start_engine(self):
        """Starting car engine"""
        self.engine_status = "On"
        print(f"Engine of {self.my_car} started.")

    def go(self):
        """Start driving the car"""
        if self.engine_status != "On":
            self.start_engine()
        print(f"The {self.my_car} is driving.")

    def turn_off_engine(self):
        """Turn car engine off"""
        if self.engine_status == "On":
            self.engine_status = "Off"
            print(f"Engine of {self.my_car} is turned off")
        else:
            print(f"Engine of {self.my_car} is already off")


toyota_camry = Car(brand="Toyota", model="Camry", wheels=4)
honda_civic = Car(brand="Honda", model="Civic", wheels=4)
print(toyota_camry)
print(honda_civic)
toyota_camry.start_engine()
toyota_camry.go()
# toyota_camry.turn_off_engine()
# honda_civic.turn_off_engine()

class BrowserDriver:
    browser

    def __init__(self, browser):
        self.browser = browser

BrowserDriver('chrome')


class APIClient():

    host = '127.0.0.1'

    def __init__(self, host):
        self.host = host

    def check_status(self):
        pass
    def get_method(self):
        pass

class Test_test(APIClient):

    def setUp(self, host):
        self.api = APIClient(host)

    def test_check(self):
        self.api.check_status()

    def test_get(self):
        self.api.get_method()

