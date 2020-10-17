n = input()
ar =input().split( ) 
def sockMerchant(n,ar):
    totalpair = 0
    test= list(set(ar))
    for i in test :
        pair = 0
        for j in ar :
            if i==j:
                pair+=1
        if pair>=2:
            totalpair=totalpair+int(pair/2)


    return totalpair
print(sockMerchant(n,ar))
