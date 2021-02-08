# This is the general format. Defaults to printing 15 decimals
print("Pi is approximately {0:12}".format(22 / 7))
# The f specifies floating-point value. Defaults to 6 decimals
print("Pi is approximately {0:12f}".format(22 / 7))
# Also floating point format with an added precision of 50 decimals
print("Pi is approximately {0:12.50f}".format(22 / 7))
# Print the same but in different field widths
print("Pi is approximately {0:52.50f}".format(22 / 7))
print("Pi is approximately {0:62.50f}".format(22 / 7))
print("Pi is approximately {0:72.50f}".format(22 / 7))
