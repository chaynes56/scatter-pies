#!/usr/bin/env python3
"""
Generate a scatter plot of pie charts of precinct data in csv file.
Assumes header row with format: PRECINCT,AttGen %,Turnout %,hs_vacp,hs_ownp,hs_renp,hs_vctp.
"""
import matplotlib.pyplot as plt
import csv
import os
from argparse import ArgumentParser

# pie chart colors
colors = ['green', 'red', 'yellow', 'blue'] # others include 'magenta', 'cyan'
color_key = ['hs_vacp', 'hs_ownp', 'hs_renp', 'hs_vctp']

# command line argument parsing
parser = ArgumentParser(prog='spie.py', epilog=__doc__)
parser.add_argument('csv_file', type=str, default = '../data/BL-data.csv',
                    help='The name of a precinct CSV file.')
parser.add_argument('-i', '--image', type=str,
                    help='The name of a file in which to save the plot figure.')
args = parser.parse_args()

def scatter_pie_plots(data) -> None :
    """Generate a scatter plot of pie charts of precinct data in csv file.
    :param data: a list of row lists
    """
    data = data[1:] # remove header row
    data = [[row[0]] + [float(x) for x in row[1:]] for row in data] # float all but the precinct name

    transposed_data = [list(row) for row in zip(*data)] # a list of columns
    precinct, x_values, y_values = transposed_data[:3]

    fig, ax = plt.subplots()
    plt.scatter(x_values, y_values)
    x_init = ax.get_xlim()
    y_init = ax.get_ylim()

    for row in data:
        precinct, x, y = row[0:3]
        pie_values = row[3:]
        ax.pie(pie_values, center=(x, y), radius=0.02, colors=colors, frame=True)
        ax.text(x, y, str(precinct), ha='left', va='top', fontsize=6, color='black')

    ax.set_ylim(y_init)
    ax.set_xlim(x_init)
    ax.grid(True)
    plt.xlabel('Dems %')
    plt.ylabel('Turnout %')

    base = os.path.basename(args.csv_file)
    file_name, _ = os.path.splitext(base)

    # add pie chart color legend and title
    text_legend = ''
    for c, key in zip(colors, color_key):
        text_legend += c + ': ' + key + '\n'
    plt.figtext(0.7, 0.5, text_legend)
    plt.figtext(0.4, 0.9, 'Precincts of ' + file_name, size=12)

    if args.image:
        plt.savefig(args.image, bbox_inches='tight', dpi=300)
    plt.show()

if __name__ == '__main__':
    print('Generating scatter plot of pie charts for data in', args.csv_file)
    with open(args.csv_file, newline='') as csvfile:
        csv_data = list(csv.reader(csvfile))
    scatter_pie_plots(csv_data)
