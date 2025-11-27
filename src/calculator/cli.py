"""
Calculator command line client
"""

import argparse
from calculator.basics import Calculator

def main():
    """
    Performs an addition
    """
    parser = argparse.ArgumentParser(description='Calculator')
    parser.add_argument('a', type=int)
    parser.add_argument('b', type=int)
    args = parser.parse_args()
    calc = Calculator()
    print(calc.add(args.a, args.b))
