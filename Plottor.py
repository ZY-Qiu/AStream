import csv
from locale import atoi
from turtle import color
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
from collections import Counter
import scipy.stats as stats
import numpy as np
import pandas as pd

def main():
    c1 = r"C:\Users\QiuGeGe\Desktop\Network Modeling and Analysis\ExperimentProject\c1.csv"
    c2 = r"C:\Users\QiuGeGe\Desktop\Network Modeling and Analysis\ExperimentProject\c2.csv"

    c = {'INITIAL_BUFFERING': 'violet', 'PLAY': 'lightcyan', 'BUFFERING': 'lightpink'}

    dash = pd.read_csv(c1)
    dash = dash.tail(200)
    dash = dash.loc[dash.CurrentPlaybackState.isin(c.keys() )]

    c1_req = []
    start = 0
    end = 0
    dash.reset_index(drop=True, inplace=True)
    for i in range(dash.EpochTime.size):
        if(i > 0 and dash.Action[i]=="Writing" and dash.Action[i-1]!="Writing"):
            start = dash.EpochTime[i-1]
        if(i > 0 and dash.Action[i]!="Writing" and dash.Action[i-1]=="Writing"):
            end = dash.EpochTime[i-1]
            c1_req.append((start, end))
    x1 = []
    y1 = []
    for (start, end) in c1_req:
        x1.append(start)
        x1.append(start)
        y1.append(0)
        y1.append(1)
        x1.append(end)
        x1.append(end)
        y1.append(1)
        y1.append(0)

    # for index, s in states.iterrows():
    #     plt.axvspan(s['startTime'], s['endTime'],  color=c[s['startState']], alpha=1) 

    plt.plot(dash[dash.Action=="Writing"].EpochTime, dash[dash.Action=="Writing"].Bitrate / 1000000.0, 'bx', label="Player-1 requested bitrate")

    dash = pd.read_csv(c2)
    dash = dash.tail(200)
    dash = dash.loc[dash.CurrentPlaybackState.isin(c.keys() )]
    c2_req = []
    start = 0
    end = 0
    dash.reset_index(drop=True, inplace=True)
    for i in range(dash.EpochTime.size):
        if(i > 0 and dash.Action[i]=="Writing" and dash.Action[i-1]!="Writing"):
            start = dash.EpochTime[i-1]
        if(i > 0 and dash.Action[i]!="Writing" and dash.Action[i-1]=="Writing"):
            end = dash.EpochTime[i-1]
            c2_req.append((start, end))
    x2 = []
    y2 = []
    for (start, end) in c2_req:
        x2.append(start)
        x2.append(start)
        y2.append(0)
        y2.append(1)
        x2.append(end)
        x2.append(end)
        y2.append(1)
        y2.append(0)


    # for index, s in states.iterrows():
    #     plt.axvspan(s['startTime'], s['endTime'],  color=c[s['startState']], alpha=1) 

    plt.plot(dash[dash.Action=="Writing"].EpochTime, dash[dash.Action=="Writing"].Bitrate / 1000000.0, 'r*', label="Player-2 requested bitrate")
    plt.xlabel("Time (s)")
    plt.ylabel("Mbps")

    axes = plt.gca()
    left, right = axes.get_xlim()
    axes.hlines(y=0.8, xmin=left, xmax=right, linestyles='dashed', label="Fair share of the avail-bw")

    two_active = []
    for (start1, end1) in c1_req:
        for (start2, end2) in c2_req:
            if(end2 < start1 or end1 < start2): 
                continue
            # must intersect
            s = max(start1, start2)
            e = min(end1, end2)
            if(s < e):
                two_active.append((s, e))

    plt.plot(x1, y1, color="pink")
    plt.plot(x2, y2, color="pink")
    axes.hlines(y=1, xmin=c2_req[-1][0], xmax=c2_req[-1][1], color="pink", label="When at least one play is active")


    x = []
    y = []
    for (start, end) in two_active:
        x.append(start)
        x.append(start)
        y.append(0)
        y.append(2)
        x.append(end)
        x.append(end)
        y.append(2)
        y.append(0)
    # plt.plot(x1, y1, color="green")
    plt.plot(x, y, color="yellow", label="When two players both are active")


    c1_tp = r"C:\Users\QiuGeGe\Desktop\Network Modeling and Analysis\ExperimentProject\c1_download_rate.csv"
    c2_tp = r"C:\Users\QiuGeGe\Desktop\Network Modeling and Analysis\ExperimentProject\c2_download_rate.csv"

    dash = pd.read_csv(c1_tp).tail(102)
    plt.plot(dash["time"], dash["Download Rate"] / 1000000.0, 'm', label="Player-1 chunk throughput")
    dash = pd.read_csv(c2_tp).tail(102)
    plt.plot(dash["time"], dash["Download Rate"] / 1000000.0, 'g-.', label="Player-2 chunk throughput")

    # find the overlap time when both request


    plt.legend(loc='upper left')
    plt.show()

if __name__ == '__main__':
    main()