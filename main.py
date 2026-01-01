# Show demo scatter plot of pie charts
# From https://stackoverflow.com/questions/66512564/matplotlib-pie-charts-as-scatter-plot#:~:\
# text=def%20plot_pie%28x%2C%20ax%2C,%29%20ax.set_frame_on%28True%29

import matplotlib.pyplot as plt
import pandas as pd
import random

def rand(): #simulate some random data
    return [random.randint(0,100) for _ in range(10)]

# from https://stackoverflow.com/questions/66512564/matplotlib-pie-charts-as-scatter-plot#:~:text=def%20plot_pie%28x
# %2C%20ax%2C,%29%20ax.set_frame_on%28True%29
def plot_pie(x, ax):
    ax.pie(x[['a', 'b', 'c']], center=(x['lat'], x['lon']), radius=1, colors=['r', 'b', 'g'],
           wedgeprops={'clip_on': True}, frame=True)

def scatter_pie_plots():
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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Running main demo')
    scatter_pie_plots()
