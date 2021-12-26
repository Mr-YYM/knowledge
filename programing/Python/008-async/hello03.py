import time

def say_after(delay: int):
    print("hello")
    time.sleep(delay)
    print("world")

def main():
    say_after(1)
    say_after(1)
    say_after(1)

if __name__ == '__main__':
    main()