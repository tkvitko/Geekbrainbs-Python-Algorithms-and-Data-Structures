import sys
import ctypes
import struct

a = 5
b = 125.54
c = 'Hello World!'

print(id(a))
print(sys.getsizeof(a))

#print(ctypes.string_at(id(a), sys.getsizeof(a)))
#print(struct.unpack('LLLd', ctypes.string_at(id(b), sys.getsizeof(b))))