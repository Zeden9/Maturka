def streak(list:list):
    for n in list:
        print(list[n-1], n)

streaks = [4,5,64,75]

streak(streaks)
print("test push")