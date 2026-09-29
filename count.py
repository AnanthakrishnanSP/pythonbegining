# count of those 3 digit numver that contain digit 3
def co():
counts=0
i=100
while i<=999:
    s=str(i)
    if '3' in s:
        count=count+1
    i+=1
print(count)
co()