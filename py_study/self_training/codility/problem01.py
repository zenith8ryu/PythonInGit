def solution(N):
    for i in range(1, N + 1):
        if i % 15 == 0:
            print("FizzBuzz")
            continue
        if i % 21 == 0:
            print("FizzWoof")
            continue
        if i % 35 == 0:
            print("BuzzWoof")
            continue
        if i % 3 == 0:
            print("Fizz")
            continue
        if i % 5 == 0:
            print("Buzz")
            continue
        if i % 7 == 0:
            print("Woof")
            continue
        print(i)


solution (24)