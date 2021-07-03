import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.dates as mdates
from datetime import date
from dateutil.relativedelta import relativedelta

# read data from csv
data = pd.read_csv('lesage_timeline.csv')

# convert dates to datetime
data.start = pd.to_datetime(data.start)
data.end = pd.to_datetime(data.end)

# convert datetime to numeric value
startdate=mdates.date2num(data.start)

# initialize plot
fig, ax1 = plt.subplots()

# set figure size [width, height]
fig.set_size_inches(18.0, 5.0, forward=True)

# collect all categories for barplots while removing duplicates
categories=[]
for i in range(len(data.index)):
	if data.category[i] not in categories:
		if data.category[i] != "Milestone":
#			categories.append(data.category[i])
			if data.category[i] != "Travel":
				categories.append(data.category[i])

# plot categories as barplots
for i in range(len(data.index)):
	if data.category[i] in categories:
		if data.category[i] == "Living":
			ax1.barh( categories.index(data.category[i])+1, (data.end[i]-data.start[i]), left=data.start[i], color='tab:blue', edgecolor='black', zorder=9999)
		if data.category[i] == "Schooling":
			ax1.barh( categories.index(data.category[i])+1, (data.end[i]-data.start[i]), left=data.start[i], color='tab:orange', edgecolor='black', zorder=9999)
		if data.category[i] == "Work":
			ax1.barh( categories.index(data.category[i])+1, (data.end[i]-data.start[i]), left=data.start[i], color='tab:green', edgecolor='black', zorder=9999)
#		if data.category[i] == "Travel":
#			ax1.barh( categories.index(data.category[i])+1, (data.end[i]-data.start[i]), left=data.start[i], color='tab:purple', edgecolor='black', zorder=9999)

# plot event category as text in corresponding category barplot
for i in range(len(data.index)):
	if data.category[i] != "Milestone":
		if data.category[i] == "Living":
			ax1.text(s=data.description[i], x=startdate[i], y=categories.index(data.category[i])+1, color="k", verticalalignment="center", size=10, zorder=9999)
		if data.category[i] == "Schooling":
			ax1.text(s=data.description[i], x=startdate[i], y=categories.index(data.category[i])+1, color="k", verticalalignment="center", size=10, zorder=9999)
		if data.category[i] == "Work":
			ax1.text(s=data.description[i], x=startdate[i], y=categories.index(data.category[i])+1, color="k", verticalalignment="center", size=10, zorder=9999)
#		if data.category[i] == "Travel":
#			ax1.text(s=data.description[i], x=startdate[i], y=categories.index(data.category[i])+1, color="k", verticalalignment="center", size=10, zorder=9999)

# plot categories labeled as events in standard timeline format
# initialize levels counter
counter = 0
# plot main timeline
ax1.plot(( min(data.start), max(data.end) ), (0, 0), 'k', alpha=.5)
# iterate through data
for i in range(len(data.index)):
	if data.category[i] == "Milestone":
		# counter has 3 levels
		if (counter % 3) == 0:
			level = -1
		elif (counter % 3) == 1:
			level = -2
		elif (counter % 3) == 2:
			level = -3
		# plot dot on main timeline
		ax1.scatter(data.start[i], 0, s=100, facecolor='w', edgecolor='k', zorder=9999)
		# plot a line from dot on main timeline up to where the event text will go
		ax1.plot((data.start[i], data.start[i]), (0, level), c='tab:red', alpha=.7)
		# plot event text
		ax1.text(data.start[i], level, data.description[i], ha='left', va='bottom', fontsize=10, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round'), zorder=9999)
		counter += 1

# set y-axis ticks as labels of bar plot events
yticks=[]
for i in range(len(categories)+1):
	if i == 0:
		yticks.append('Milestones')
	else:
		yticks.append(categories[i-1])
plt.yticks( range(len(categories)+1), yticks )

# plot title
ax1.set_title('Stephen Lesage Timeline')

# plot x-axis title
ax1.set_xlabel('YYYY-MM-DD')
# plot x-axis limits
ax1.set_xlim([pd.to_datetime('1993-09-01'), pd.to_datetime(date.today().strftime("%Y-%m-%d"))+relativedelta(months=4)])
# x-axis major ticks every 6 months
ax1.xaxis.set_major_locator( mdates.MonthLocator(interval=6) )
# text in the x axis will be displayed in 'YYYY-mm_dd' format
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
# x-axis minor ticks every month
ax1.xaxis.set_minor_locator( mdates.MonthLocator() )
# format the x-axis coords message box, i.e. the numbers displayed as the cursor moves across the axes within the interactive GUI
ax1.format_xdata = mdates.DateFormatter('%Y-%m-%d')
# plot x-axis major ticks grid
ax1.grid(True)
# rotates and right aligns the x-axis labels, and moves the bottom of the axes up to make room for them
fig.autofmt_xdate()

# save figure
fig.savefig('lesage_timeline.png', dpi=100)

# display plot
plt.show()

