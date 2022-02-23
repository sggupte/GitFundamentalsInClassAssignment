a = "The sky is blue"
print(a)


for letter in a:
    print(letter)


def calc_square_root(n):
    try:
        answer = n^2
        return answer
    except TypeError:
        print("String arguement. Cannot complete operation")
    


def main():
    calc_square_root("hello")

if __name__ == "__main__":
    main()
