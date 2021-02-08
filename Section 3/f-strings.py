# This won't work on Python versions earlier than 3.6

# Floating point format with an added precision of 50 decimals
# The f formats the string which replaces values inside the curly braces {}
print(f"Pi is approximately {22 / 7:12.50f}")
# Another way to do this
pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")
