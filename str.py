# indexes of strings
test = "hi it's a test that make by R.N.C-star"


print(test[:2])
print(test[3:6])
print(test[2:])
print("--------------------------------")
# ----------------------------------------------------------------
# modify
print(test.upper())
print(test.lower())
print(test.replace("h", "t"))
print(test.strip())
print("--------------------------------")
# ----------------------------------------------------------------
# format        we want to fix a bug in python

name = "my name is reza \t {}"
ageReza = 22
# print(name+"  "+ageReza)   it is not working properly
print(name.format(ageReza))
