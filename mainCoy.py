import time

def print_with_delay(*args):
    i = 0
    while i < len(args):
        if isinstance(args[i], str):
            text = args[i]
            delay = args[i+1]
            for char in text:
                print(char, end='', flush=True)
                time.sleep(delay)
            i += 2
        elif isinstance(args[i], float) or isinstance(args[i], int):
            time.sleep(args[i])
            i += 1
    print()  

def lyricnich():
    print_with_delay("No need a vow", 0.09)
    time.sleep(2)
    print_with_delay("I can keep myself ", 0.1, 2, "within", 0.1)
    time.sleep(4.5)
    print_with_delay("Your deepest love,",0.1,1 ,"your comfort zone, ", 0.1,1.2,"even your bad day",0.1)
    time.sleep(7)
    print_with_delay("Maybe we can't talk", 0.1)
    time.sleep(3)
    print_with_delay("But baby,",0.1,1, " we don't need it all", 0.1)
    time.sleep(2.5)
    print_with_delay("Cuz maybe,",0.1,1, "we just find ourself", 0.1)
    time.sleep(2.3)
    print_with_delay("In the peak of love", 0.1)
    time.sleep(1)
    print_with_delay('............', 0.5)

lyricnich()
