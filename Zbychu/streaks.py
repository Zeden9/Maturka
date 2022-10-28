def streak(list:list): 
    '''
    Returns positive streak duration, and beggining index in list
    '''
    currentStreak = 0
    maxStreak = 0
    begginingIndex = 1
    for n in range(len(list)):
        if(list[n-1] < list[n]):
            currentStreak += 1
            if(currentStreak > maxStreak):
                maxStreak = currentStreak
                begginingIndex = n - currentStreak + 1
        else:
            currentStreak = 1
    return maxStreak, begginingIndex
