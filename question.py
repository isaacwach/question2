# Sudo Code
# 1. Get the number of keys per number
# 2. Note that from 1 to 6, the number of keys to the the maximum A's is the same to the number.
# 3. Find a relevant pattern from number 7 onwards

def maximumA(N):
# if N is less than 6
    if (N<7):
        return N

    screenEntries = [0] * N
    for n in range(1, 7):
        screenEntries[n - 1] = n 

    for n in range(7, N+1):
        screenEntries[n - 1] = maximum(
            2* screenEntries[n-4], 8

            maximum(
                3* screenEntries[n-6], 9
            )
        )
    return screenEntries[N-1]     
