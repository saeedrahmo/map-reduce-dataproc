#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

batch_current = 0
metric_value_min = 0
metric_value_max = 0
metric_value_med = 0
batch_current_counter=1
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    line = line.rstrip()
    # parse the input we got from mapper.py
    batch_id_current, metric_value, metric_selected, batch_unit = line.split('\t')
    # convert count (currently a string) to int
    try:
        batch_id_current = int(batch_id_current)
        batch_unit = int(batch_unit)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    if batch_current != batch_id_current:
        if(batch_current != 0) and (batch_id_current != 1) and (batch_id_current-batch_current == 1):
            print('batch_id: {}\t metric: {}\t min: {}\t max: {}\t med: {}'.format(
                batch_current, metric_selected, metric_value_min, metric_value_max, metric_value_med))
        batch_current = batch_id_current
        metric_value_min = metric_value
        batch_current_counter=1
        continue
    else:
        metric_value_max = metric_value
        batch_current_counter += 1
        if batch_current_counter == (batch_unit/2):
            metric_value_med = metric_value
        continue

print('batch_id: {}\t metric: {}\t min: {}\t max: {}\t med: {}'.format(
    batch_current, metric_selected, metric_value_min, metric_value_max, metric_value_med))
