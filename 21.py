aa1=int(input())
l1=list(map(int,input().split()))
avg=int(aa/2)
lb11=l[:avg]
lb12=l[avg::]
if ((sum(lb11)//len(lb11))==(sum(lb12)//len(lb12))):
    print("yes")
else:
    print("no")
