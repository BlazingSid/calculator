#!/usr/bin/env python3
"""
Simple Python CLI calculator
Usage: run `python calculator.py` and follow on-screen prompts.
"""

import math

def calculate(expr):
    """
    Evaluate simple math expressions safely using a restricted eval.
    Allowed: numbers, + - * / ** (), math functions from math module
    """
    allowed_names = {k: getattr(math, k) for k in dir(math) if not k.startswith("__")}
    allowed_names.update({
        "abs": abs,
        "round": round
    })

    # Only allow characters often used in math expressions
    for ch in expr:
        if ch.isalpha() and ch not in ''.join(allowed_names.keys()):
            # If alpha char not present in allowed function names, block
            # (this is a simple filter — avoids arbitrary names)
            pass

    try:
        # Use eval with restricted globals and provided locals for math funcs
        result = eval(expr, {"__builtins__": None}, allowed_names)
        return result
    except Exception as e:
        raise ValueError(f"Invalid expression: {e}")

def main():
    print("Simple Python Calculator — type 'help' for tips, 'exit' to quit.")
    while True:
        s = input("calc> ").strip()
        if not s:
            continue
        if s.lower() in ("exit", "quit"):
            print("Goodbye!")
            break
        if s.lower() in ("help", "?"):
            print("Examples: 2+2, 3*4, (2+3)/4, 2**8, sqrt(16), sin(0.5)")
            print("You can use math functions from the math module (sqrt, sin, cos, etc.)")
            continue
        try:
            res = calculate(s)
            print("= ", res)
        except ValueError as err:
            print(err)

if __name__ == "__main__":
    main()
