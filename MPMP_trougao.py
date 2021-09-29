
Skip to content
Pull requests
Issues
Marketplace
Explore
@StokicDusan
StokicDusan /
Python-misc
Public

1
0

    0

Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights

    Settings

Python-misc/MPMP9_trougao.py /
@StokicDusan
StokicDusan committed new script
Latest commit 39f9c3b on Apr 13
History
1 contributor
53 lines (43 sloc) 1.07 KB
# my solution for MPMP9
# https://www.think-maths.co.uk/trianglepuzzle
from os import system


def Continue(n):
    while(1):
        x = str(input('continue?(Y\\N) :'))
        if x.upper() == "N":
            return 0
        elif x.upper() == "Y":
            print()
            return 1


def shift(a):
    tri = [a[2], 0, 0]
    for i in range(2, 0, -1):
        tri[i] = a[i-1]
    return tri


def new_tri(a, n):
    tri = [0, 0, 0]
    tri[0] = abs(a[0]-a[1])
    tri[1] = abs(a[1]-a[2])
    tri[2] = abs(a[2]-a[0])
    if n % 2 != 0:
        tri = shift(tri)
    return tri


def main():
    a, b, c = eval(input('numbers : '))
    n = int(input('length='))
    trougao = [a, b, c]
    current_sum, terminate, i = 0, 0, 2
    while(i < n+2):
        print(i-1, '\t: ', trougao, '\t\t  sum : ', sum(trougao))
        trougao = new_tri(trougao, i)
        if sum(trougao) == current_sum:
            terminate += 1
        if terminate > 3:
            break
        current_sum = sum(trougao)
        i += 1


cont = 1
while cont:
    main()
    cont = Continue(cont)
    system('cls')

    © 2021 GitHub, Inc.
    Terms
    Privacy
    Security
    Status
    Docs

    Contact GitHub
    Pricing
    API
    Training
    Blog
    About

Loading complete
