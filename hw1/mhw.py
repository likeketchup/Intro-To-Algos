# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 22:23:45 2021

@author: Toma
"""
def main():
    count = int(input("positive integer:"))
    for i in range(count):
        print("Hello, "+input("inputs:")+"!")

# def main():
#     s = input("").split("\n")
#     for i in range(int(s[0])):
#         print("Hello, "+s[i+1]+"!")
if __name__ == "__main__":
    # execute only if run as a script
    main()
    
