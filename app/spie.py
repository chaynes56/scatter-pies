# Generate scatter plot of pie charts of precinct data in csv file
# Assumes header row with format: PRECINCT,AttGen %,Turnout %,hs_vacp,hs_ownp,hs_renp,hs_vctp

# To access data file: data_file_path = os.path.join(os.path.dirname(__file__), 'data/FILE.csv')
# per https://pynsist.readthedocs.io/en/latest/faq.html#building-on-other-platforms

import matplotlib.pyplot as plt
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("csv_file", type=str,
                    default = "data/BL-data.csv",
                    help="The name of a CSV precinct data file).")
# parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose output (optional flag).")
args = parser.parse_args()

# from https://stackoverflow.com/questions/66512564/matplotlib-pie-charts-as-scatter-plot#:~:text=def%20plot_pie%28x
# %2C%20ax%2C,%29%20ax.set_frame_on%28True%29
def plot_pie(x, ax):
    ax.pie(x[['a', 'b', 'c']], center=(x['lat'], x['lon']), radius=1, colors=['r', 'b', 'g'],
           wedgeprops={'clip_on': True}, frame=True)

def scatter_pie_plots(data):
    # data is a list of row lists
    transposed_data = [list(row) for row in zip(*data)[1:]] # a list of columns, skipping header row
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

if __name__ == '__main__':
    print('Generating scatter plot of pie charts for data in ', args.csv_file)
    with open(args.csv_file, newline='') as csvfile:
        data = list(csv.reader(csvfile))
    scatter_pie_plots(data)
