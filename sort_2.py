# sort_2
def main():
    pass
    l=input()
    n=list(map(int,input().split()))
    for i in range(len(n)):
        for k in range (i+1,len(n)):
            if n[k]<n[i]:
                n[i],n[k]=n[k],n[i]
    print(' '.join(map(str,n)))

if __name__ == '__main__':
    main()
