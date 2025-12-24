"""
Determines the numbers that are not summable
by unique squares. The list is finite and the
last element is 128
"""

def main():

    THRESHOLD = 10000
    n = 2
    summable = {0, 1}

    while 1:
        square = n ** 2
        summable |= {num + square for num in summable}
        if n ** 2 > THRESHOLD:
            break
        n += 1

    unsummable = [i for i in range(1, THRESHOLD) if i not in summable]

    print(f"summable: {summable}")
    print(f"unsummable: {unsummable}")
    print(f"len: {len(unsummable)}")
    print(f"threshold: {THRESHOLD}")

if __name__ == "__main__":
    main()