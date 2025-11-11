import numpy as np

#random creation of data
np.random.seed(seed=42)
sales_data_1d = np.random.randint(low=10, high=75, size=12)
#printing in 1d
print(f"Here is our 1d sales data: \n{sales_data_1d}")
#reshaping data in 2d
print("rows = Days, Columns = Products")

sales_table_2d = sales_data_1d.reshape(4, 3)

print (f"Here is our 2d sales data: \n{sales_table_2d}")

# t shirts
# caps
# mugs

# 4 days
#Monday = 4
#Tuesday = 3
#Wednesday =3 3
#Thursday = 3

