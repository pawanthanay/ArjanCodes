# 1. From class to dataclass

# Convert the following classes into dataclasses such that the initializers that the dataclass generates have the same behavior as the regular class:
'''
class A:
  def __init__(self) -> None:
    self._length = 0

class B:
  def __init__(self, x: int, y: str = "hello", l: list[int] | None = None) -> None:
    self.x = x
    self.y = y
    self.l = [] if not l else l

class C:
  def __init__(self, a: int = 3) -> None:
    self.a = a
    self.b = a + 3

'''
from dataclasses import dataclass,field
from datetime import datetime


@dataclass
class A:
    _length: int = field(init=False, default= 0)

@dataclass
class B:
    x: int
    y: str = "hello"
    l: list[int] = field(default_factory=list)

@dataclass
class C:
    a: int = 3
    b: int = field(init=False)



'''
2. Let's sell some phones

The mobile phone company PhonyPhones needs to create a system for managing their customers' phone plans and they need to get better insight into the data that they need to store. 
Because their CEO knows a bit of Python, he asks you to write a few dataclasses representing the data structure of their application. 
In short, they have customers (name, address, email address), phones (brand, model, price, serial number) and plans (which refer to a customer, a phone, a start date, 
the total number of months in the contract, a monthly price, and whether the phone is included in the contract).

Write dataclasses that can represent this data. You may take some freedom in how things like addresses etc. are represented.

'''

@dataclass
class Customer:
    name: str
    address: str
    email: str

@dataclass
class Phone:
    brand: str
    model: str
    price: str
    serial: int

@dataclass
class Plans:
    customer: Customer
    phone: Phone
    startDate: datetime
    duration_months: int
    price: int
    
