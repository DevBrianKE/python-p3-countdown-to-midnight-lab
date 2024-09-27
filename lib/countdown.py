import time

def countdown(n):
    """Count down from n to 1, printing each second."""
    while n > 0:
        print(f'{n} SECOND(S)!')
        n -= 1
    print('HAPPY NEW YEAR!')

def countdown_with_sleep(n):
    """Count down from n to 1 with a 1-second pause between each count."""
    while n > 0:
        print(f'{n} SECOND(S)!')
        time.sleep(1)  # Pause for 1 second
        n -= 1
    print('HAPPY NEW YEAR!')
