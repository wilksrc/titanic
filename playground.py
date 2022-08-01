import pandas as pd

mydf = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
mymin = mydf.min(axis=0)
mymin2 = mydf.min(axis=1)

mymin = pd.DataFrame(mymin)
myt = mymin.transpose()

a = [1, 2, 3]
b = [4, 5, 6]




# https://cmdlinetips.com/2019/10/how-to-make-a-plot-with-two-different-y-axis-in-python-with-matplotlib/
# # create figure and axis objects with subplots()
# fig, ax = plt.subplots()
# ax.plot(stuff['level1'], stuff['freq'], color='blue', marker='o')
# ax.set_xlabel('age_g1', fontsize=12)
# ax.set_ylabel('freq', color='blue', fontsize=12)
# plt.show()
#
# # twin object for two different y-axis on the sample plot
# ax2 = ax.twinx()
# # make a plot with different y-axis using second axis object
# ax2.plot(stuff['level1'], stuff['rec'], color='grey', marker='o')
# ax2.set_ylabel('policies', color='grey', fontsize=12)
# plt.show()

# https://stackoverflow.com/questions/53901718/plot-bar-and-line-in-same-plot-different-y-axes-using-matplotlib-no-pandas
# plt.figure(1, figsize=(5, 5))
# barchart = plt.bar(stuff['level1'], stuff['freq'], color='grey')
# plt.twinx()
# linechart = plt.plot(stuff['level1'], stuff['rec'], color='blue')
