#!/usr/bin/python3
def main():
    x=dict(x=42)
    y=dict(x=42)
    print(x==y,type(x==y))
    print(x is y)
if __name__=="__main__":main()
