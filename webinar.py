import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pandas.plotting import register_matplotlib_converters

import numpy as np
import datetime as dt

# omazinai
plt.style.use('ggplot')
font = {'family' : 'meiryo'}
matplotlib.rc('font', **font)

# code
df = pd.read_csv("./webinar-member.csv", parse_dates=["メンバー日"])
dfdates = df["メンバー日"]
times = []
min30s=[]
gh=0

while gh >= 49:
    min30s = min30s+[gh]

# print(df.dtypes)
for dfdate in dfdates:
    
    hour = dfdate.hour
    minute = dfdate.minute
    th = hour
    
    if minute >= 0 and minute < 16:
        tm = 0
        th = hour
        print("less than 16")
    elif minute >= 16 and minute < 46:
        tm = 30
        th = hour
        print("less than 46")
    elif minute >= 46:
        th += 1
        tm = 0
        print("more than 46")

    
    print((dfdate))
    print((hour, minute))
    print((th, tm))

    dfdate = dfdate.replace(hour=th, minute=tm, second=0, microsecond=0)
    print((dfdate))

    times = times + [dfdate]
    print("=========================")

print((times))

gh = 00
gm = 0

while gh <= 23:

    ndt = dt.time(gh,0,0,0)
    min30s = min30s + [ndt]
    ndt = dt.time(gh,30,0,0)
    min30s = min30s + [ndt]
    
    gh+=1


    # datestr = f'2019/08/02 {gh}:00:00'
    # ndt = dt.datetime.strptime(datestr, '%Y/%m/%d %H:%M:%S')
    # x = x + [ndt]

    # datestr = f'2019/08/02 {gh}:30:00'
    # ndt = dt.datetime.strptime(datestr, '%Y/%m/%d %H:%M:%S')
    # x = x + [ndt]
    
    # gh+=1

print("=================")
print((min30s[3]))


counts = []
strmin30s = []
for min30 in min30s:
    strfmin30 = min30.strftime('%X')
    count = 0

    for time in times:
        strftime = time.strftime('%X')
        
        if strfmin30 == strftime:
            count += 1
            
    
    counts = counts + [count]
    strmin30s = strmin30s + [strfmin30]
    # counts = counts + {min30, count}

mydict = {"min30s": min30s, "apply": counts}
my_df = pd.DataFrame.from_dict(mydict)

print("=================")
print((mydict))

print("=================")
print((my_df))

nDF = pd.DataFrame(my_df)
# nDF.plot.bar()


plt.plot(min30s, counts, label="apply", color='r')
dt_labels = [dt.strftime('%H:%M') for dt in nDF['min30s']]
print((dt_labels))
plt.xticks(min30s[::1], dt_labels[::1], rotation=90, size='small')
# nDF.plot.show()
# plt.bar(min30s, counts)
plt.show()
# print(dfdates)

# ndf = pd.DataFrame({'counts', counts})