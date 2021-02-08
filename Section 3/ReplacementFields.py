# {0}, {1}, {2}, {3} are called replacement fields

# Python 2 way of doing before the introduction of replacement fields
age = 27
print("My age is " + str(age) + " years")
# Introduced in Python 3
print("My age is {0} years".format(age))

# Other examples
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} & {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))
# Does the same thing as below
print("There are {0} days in Jan, Mar, May, Jul, Aug, Oct & Dec\n".format(31))

print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}, Jul: {2}, Aug: {2}, Sep: {1}, Oct: {2}, "
      "Nov: {1}, Dec: {2}\n".format(28, 30, 31))

# Similar as above but with Triple quotes
print("""Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
Jun: {1}
Jul: {2}
Aug: {2}
Sep: {1}
Oct: {2}
Nov: {1}
Dec: {2}""".format(28, 30, 31))
