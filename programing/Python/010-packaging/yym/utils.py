"""
简单的 echo
"""
import sys


def echo(s: str):
    print(s)


def main():
    echo(sys.argv[1])
