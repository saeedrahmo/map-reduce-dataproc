#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

batch_current = 0
metric_value_min = 0
metric_value_max = 0
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    line = line.rstrip()
    # parse the input we got from mapper.py
    batch_id_current, metric_value, metric_selected = line.split('\t')
    print('batch_id: {}\t value: {}\t metric: {}'.format(batch_id_current, metric_value, metric_selected))