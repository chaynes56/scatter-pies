# Generate scatter plot of pie charts of precinct data in csv file
# Assumes header row with format: PRECINCT,AttGen %,Turnout %,hs_vacp,hs_ownp,hs_renp,hs_vctp

# To access data file: data_file_path = os.path.join(os.path.dirname(__file__), 'data/FILE.csv')
# per https://pynsist.readthedocs.io/en/latest/faq.html#building-on-other-platforms

import matplotlib.pyplot as plt
import csv
import os
import argparse

# pie chart colors
colors = ['green', 'red', 'yellow', 'blue'] # also 'magenta', 'cyan'
color_key = ['hs_vacp', 'hs_ownp', 'hs_renp', 'hs_vctp']

parser = argparse.ArgumentParser()
parser.add_argument("--csv_file", type=str, default = "../data/BL-data.csv",
                    help="The name of a CSV precinct data file).")
# Optional argument example:
# parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose output (optional flag).")

args = parser.parse_args()

def scatter_pie_plots(data) -> None :
    # data is a list of row lists
    data = data[1:] # remove header row
    data = [[row[0]] + [float(x) for x in row[1:]] for row in data] # float all but the precinct name

    transposed_data = [list(row) for row in zip(*data)] # a list of columns
    precinct, x, y = transposed_data[:3]

    fig, ax = plt.subplots(figsize=(8, 8)) # 100 dpi default
    plt.scatter(x, y) ## s=1000, facecolor='none',edgecolors='r' ??
    y_init = ax.get_ylim()
    x_init = ax.get_xlim()

    for row in data:
        ax.pie(row[3:], center=(row[1], row[2]), radius=0.02, colors=colors, frame=True)

    ax.set_ylim(y_init)
    ax.set_xlim(x_init)
    ax.grid(True)
    plt.xlabel('Dems %')
    plt.ylabel('Turnout %')
    base = os.path.basename(args.csv_file)
    name, _ = os.path.splitext(base)
    plt.savefig('../images/' + name + '.jpg', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == '__main__':
    print('Generating scatter plot of pie charts for data in ', args.csv_file)
    with open(args.csv_file, newline='') as csvfile:
        csv_data = list(csv.reader(csvfile))
    scatter_pie_plots(csv_data)
