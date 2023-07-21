import sys
print("Hello from example.py")
try:
    1 / 1
except Exception as e:
    sys.exit(e)
