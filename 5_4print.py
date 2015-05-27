#!/usr/bin/python3

def main():
    n = 42.
#    s = "this is a {} number!".format(n)
    s="this is a %d number!" % n
    s='''
this is a %d number!
text is complited.
''' % n
    print(s)
if __name__=="__main__":main()
