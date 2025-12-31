# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import matplotlib.pyplot as plt
import pandas as pd
import random

def rand(): #simulate some random data
    return [random.randint(0,100) for _ in range(10)]

def plot_pie(x, ax):
    ax.pie(x[['a', 'b', 'c']], center=(x['lat'], x['lon']), radius=1, colors=['r', 'b', 'g'],
           wedgeprops={'clip_on': True}, frame=True)

# my data is stored in a similar styled dataframe that I read from a csv and the data is static
sim_data = pd.DataFrame({'a':rand(),'b':rand(),'c':rand(), 'lat':rand(),'lon':rand()})

fig, ax = plt.subplots()
plt.scatter(x=sim_data['lat'], y=sim_data['lon'], s=1000, facecolor='none',edgecolors='r')
y_init = ax.get_ylim()
x_init = ax.get_xlim()

sim_data.apply(lambda x : plot_pie(x,ax), axis=1)
ax.set_ylim(y_init)
ax.set_xlim(x_init)
plt.show()

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
