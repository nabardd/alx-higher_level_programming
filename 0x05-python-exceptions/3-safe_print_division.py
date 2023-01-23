#!/bin/usr/python3
def safe_print_division(a, b):
    try:
        result = a / b
        print(f"Inside result: {result:02d}")
    except Exception as e:
        result = None
        print(f"Inside result: {result}")
    finally:
        return (result)
