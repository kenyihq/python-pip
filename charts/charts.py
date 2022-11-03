import matplotlib.pyplot as plt
import numpy as np


def generate_pie_chart():
    labels = ['A', 'B', 'C', 'D', 'E', 'F']
    values = np.linspace(100, 500, 6) 

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png')
    plt.close


