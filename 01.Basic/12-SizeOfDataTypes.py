# Code 12: Print size of data types in C
import sys

integer_size = sys.getsizeof(0)
float_size = sys.getsizeof(0.0)
string_size = sys.getsizeof("")
bool_size = sys.getsizeof(False)
none_size = sys.getsizeof(None)

print(f"Integer object: {integer_size} bytes")
print(f"Float object: {float_size} bytes")
print(f"String object: {string_size} bytes")
print(f"Boolean object: {bool_size} bytes")
print(f"None object: {none_size} bytes")