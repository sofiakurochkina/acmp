nums = list(map(int, input().split()))

i=0
maxx = 0

count_plus = 1
count_minus = 1


while nums[i] != 0:

    if nums [i+1] > nums [i]:
        count_plus +=1
        if count_plus > maxx:
            maxx = count_plus
            
    if nums [i+1] < nums [i]:
        count_minus +=1
        if count_minus > maxx:
            maxx = count_minus

    i+=1

print (maxx)

# no answer
