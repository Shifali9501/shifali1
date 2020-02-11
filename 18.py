#https://visualalsgo.net/bn/sorting

#insertion sort
def insertionSort(data):
        for i in range(1,len(data)):
            key=data[i]
            j=i-1
            while data[j]>data[i] and j>=0 :
                data[j+1] = data[j]
                        j-=1
            data[j+1] = key





ages = [12,11,67,45,9]
insertionSort(ages)
for age in ages:
    print(ages,end=" ")