# Create Decimal objects from strings or tuples
from decimal import Decimal


d1 = Decimal('0.1')
d2 = Decimal('0.2')
print(d1 + d2)  # Output: 0.3

# Creating Decimal objects from floats is possible but not recommended due to precision issues
d3 = Decimal(0.1)
print(d3)  # Output might be unexpected: 0.1000000000000000055511151231257827021181583404541015625

#float
x = 0.1 + 0.2
print(x)  # Output: 0.30000000000000004
#decimal
x = Decimal('0.1') + Decimal('0.2')
print(x)  # Output: 0.3