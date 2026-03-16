def knapsack(ttime,marks,time,n):
    if n == 0 or ttime == 0:
        return 0
    elif time[n-1]>ttime:
        return 0
    else:
        return max(marks[n-1]+knapsack(ttime-time[n-1],marks,time,n-1),knapsack(ttime,marks,time,n-1))


n = 3
ttime = 50
marks = [60,100,120]
time = [10,20,30]

print(knapsack(ttime,marks,time,n))
