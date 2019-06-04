from __future__ import division
from matplotlib import pyplot as plt
import numpy as np
import functools

def line_chart():
    #LINE CHART
    variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
    bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
    total_error = [x + y for x, y in zip(variance, bias_squared)]
    xs = [i for i, _ in enumerate(variance)]

    plt.plot(xs, variance, 'g-', label='variance') # green solid line
    plt.plot(xs, bias_squared, 'r-.', label='bias^2') # red dot-dashed line
    plt.plot(xs, total_error, 'b:', label='total error') # blue dotted line

    # because we've assigned labels to each series
    # we can get a legend for free
    # loc=9 means "top center"
    plt.legend(loc=9)
    plt.xlabel("model complexity")
    plt.title("The Bias-Variance Tradeoff")
    plt.show()

def scatter_plots():
    #SCATTER PLOTS
    friends = [ 70, 65, 72, 63, 71, 64, 60, 64, 67]
    minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

    plt.scatter(friends, minutes)
    # label each point
    for label, friend_count, minute_count in zip(labels, friends, minutes):
        plt.annotate(label,
            xy=(friend_count, minute_count), # put the label with its point
            xytext=(5, -5), # but slightly offset
            textcoords='offset points')
    plt.title("Daily Minutes vs. Number of Friends")
    plt.xlabel("# of friends")
    plt.ylabel("daily minutes spent on the site")
    plt.show()

def scatter_test():
    #SCATTER TEST
    companies = [ 'c1', 'c2', 'c3', 'c4', 'c5' ]
    sizeInWorkers = [ 30, 40, 50, 20, 20 ]
    averageExpertise = [ 30, 10, 10, 50, 20 ]

    plt.scatter(sizeInWorkers, averageExpertise)
    for company, workers, expertise in zip(companies, sizeInWorkers, averageExpertise):
        plt.annotate(company, xy=(workers, expertise), xytext = (5, -5), textcoords = 'offset points')
    plt.title( ' Expertise on companies' )
    plt.xlabel( 'Size (workers)' )
    plt.ylabel( 'Average expertise' )
    plt.show()


line_chart()
scatter_plots()
scatter_test()
