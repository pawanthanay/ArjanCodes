age = 10
name = "pawan"
my_list: list[int | float | str | bool] = [1,10,30.5,"pawan",False]

def verify_password(submitted_password: str, stored_hash: str="123456") -> bool:
    return True

class Car:
    def __init__(self, name:str, address:str, cost:float):
        self.name = name
        self.address = address
        self.cost = cost

my_car = Car("BMW","India",100000.30)
