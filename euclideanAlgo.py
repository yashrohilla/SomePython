#!/usr/bin/python3

def euclid(a,b):
    if (b == 0):
        return a
    else:
        return euclid(b,a%b)

if __name__ == "__main__":
    a = input("Enter a: ")
    b = input("Enter b: ")
    x = euclid(int(a),int(b))
    print(x)
