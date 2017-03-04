import pandas as pd, numpy as np

# 1dimension
s = pd.Series([1.0,3.0,5.0,7.0,9.0])
print(s)

# 2dimension
a = pd.DataFrame([
		[10,20,30],
		[40,50,60],
		[70,80,90]
	])
print(a)

# dictionary
tbl = pd.DataFrame({
		"weight":[80.0,70.4,65.5,45.9,51.2],
		"height":[170,180,155,143,154],
		"type":["f","n","n","t","t"]
	})
print(tbl["weight"])

print(tbl[["weight","height"]])

print("2-3")
print(tbl[2:4])

print("higher than 160")
print(tbl[tbl.height > 160])

print("convert to NumPy")
print(tbl.as_matrix())