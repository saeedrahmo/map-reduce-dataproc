#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

batch_current = 0

metric_list = []
# input comes from STDIN (standard input)
for line in sys.stdin:
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
           #metric_mean=sum(metric_list)/batch_unit
           #metric_med=median(metric_list)
           # Square deviations
           deviations = 1
           #deviations = [(x - metric_mean) ** 2 for x in metric_list]
           # Variance
           variance = 1
           #variance = sum(deviations) / batch_unit
           # Standard deviation
           std_dev = 1
           print('batch_id: {}\t metric: {}\t min: {}\t max: {}\t med: {}\t std_dev: {}'.format(
               batch_current, metric_selected, 1, 1, 1, batch_unit))           
       metric_list.append(metric_value)
       batch_current = batch_id_current
       continue
   else:
       metric_list.append(metric_value)
       continue


# Number of observations
batch_unit=len(metric_list)
# Mean of the data
#metric_mean=sum(metric_list)/batch_unit
#metric_med=median(metric_list)
# Square deviations
deviations = 1
# Variance
variance = 1
# Standard deviation
std_dev = 1

print('batch_id: {}\t metric: {}\t min: {}\t max: {}\t med: {}\t std_dev: {}'.format(
                batch_current, metric_selected, 1, 1, 1, batch_unit))
