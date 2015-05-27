#!/usr/bin/python3

def main():
    abc=dict(m1=100,one=1,tow=2,five="five")
    d={"1":2,"domain":192,"domaine":5,"3":2}
    abc["saman"]="bazmi"
    for k in sorted(abc.keys()):
        print(k,abc[k])

if __name__=="__main__":main()
