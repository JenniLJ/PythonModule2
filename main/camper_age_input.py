def convert_to_months(x):
    return x*12

if __name__ == '__main__':
    x = input("Enter an age:")
    answer = convert_to_months(int(x))
    print(answer)
