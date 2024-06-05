def main():
    a = int(input())
    b = int(input())
    c = int(input())
    x = int(input())

    if b > 50 or c > 50:
        print("No")
        exit()

    count = 0

    for i in range(a + 1):
        for j in range(b + 1):
            for k in range(c + 1):
                sum = i * 500 + j * 100 + k * 50
                if x == sum:
                    count += 1

    print("\nOutput: {}".format(count))


if __name__ == "__main__":
    main()
