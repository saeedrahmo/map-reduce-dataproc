#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys
import math

def median(lst):    
    lstLen = len(lst)
    index = (lstLen - 1) // 2
   
    if (lstLen % 2):
        return lst[index]
    else:
        return (lst[index] + lst[index + 1])/2.0

batch_current = 0

metric_list = []
# input comes from STDIN (standard input)
with open("NDBench-testing-mapped.csv") as file:
    for line in file:#sys.stdin
       # remove leading and trailing whitespace
       line = line.strip()
       line = line.rstrip()
       # parse the input we got from mapper.py
       batch_id_current, metric_value, metric_selected = line.split('\t')
       # convert count (currently a string) to int
       try:
           batch_id_current = int(batch_id_current)
           metric_value = float(metric_value)
       except ValueError:
           # count was not a number, so silently
           # ignore/discard this line
           continue
       if batch_current != batch_id_current:
           if(batch_current != 0) and (batch_id_current != 1) and (batch_id_current-batch_current == 1):
               # Number of observations
               batch_unit=len(metric_list)
               # Mean of the data
               metric_mean=sum(metric_list)/batch_unit
               metric_med=median(metric_list)
               # Square deviations
               deviations = [(x - metric_mean) ** 2 for x in metric_list]
               # Variance
               variance = sum(deviations) / batch_unit
               # Standard deviation
               std_dev = math.sqrt(variance)
               print('batch_id: {}\t metric: {}\t min: {}\t max: {}\t med: {}\t std_dev: {}'.format(
                   batch_current, metric_selected.lower(), metric_list[0], metric_list[-1], metric_med, std_dev))
               metric_list.clear()
           metric_list.append(metric_value)
           batch_current = batch_id_current
           continue
       else:
           metric_list.append(metric_value)
           continue


# Number of observations
batch_unit=len(metric_list)
# Mean of the data
metric_mean=sum(metric_list)/batch_unit
metric_med=median(metric_list)
# Square deviations
deviations = [(x - metric_mean) ** 2 for x in metric_list]
# Variance
variance = sum(deviations) / batch_unit
# Standard deviation
std_dev = math.sqrt(variance)

print('batch_id: {}\t metric: {}\t min: {}\t max: {}\t med: {}\t std_dev: {}'.format(
                batch_current, metric_selected.lower(), metric_list[0], metric_list[-1], metric_med, std_dev))
