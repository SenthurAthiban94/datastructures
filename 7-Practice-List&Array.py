import numpy as np

temperature = np.array([],dtype=int)
temps = []
def init():
    totalNumbers = int(input(f'Enter the number of days:'))
    totaltemp = 0
    for i in range(totalNumbers):
        temp = input(f'Enter the Temperature for Day {i+1}:')
        temps.append(float(temp))
        totaltemp+=float(temp)
    avg = round(totaltemp/totalNumbers,2)
    
    abvAvgDays = 0
    for temp in temps:
        if(temp>avg): abvAvgDays+=1

    return (avg,abvAvgDays)

(averageTemperature, AboveAverageTemperatureDays) = init()
print(f'Total Avg Temperature for 1 day is {averageTemperature}\nTotal Above average temperature days are {AboveAverageTemperatureDays}')