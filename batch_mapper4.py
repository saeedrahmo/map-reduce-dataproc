#!/usr/bin/env python
"""mapper.py"""

import sys

metric_dict = {
    "CPUUtilization_Average": 0,
    "NetworkIn_Average": 1,
    "NetworkOut_Average": 2,
    "MemoryUtilization_Average": 3,
    "Final_Target": 4
}
metric_selected = "CPUUtilization_Average"

batch_size = 5
batch_id = 2
batch_unit = 10

counter_total = 0
batch_id_current = batch_id-1
# input comes from STDIN (standard input)
with open("NDBench-testing.csv") as file:
    for line in file:#sys.stdin
        counter_total += 1
        try:
            metric_value = line.rstrip().split(
                ',')[metric_dict[metric_selected]]
            if metric_value.replace('.', '', 1).isdigit() == False:                        
                continue
            elif (counter_total % (batch_unit) == 0) and (counter_total >= (batch_id*batch_unit)):
                batch_id_current += 1            
            elif (counter_total >= batch_id*batch_unit) and (counter_total < (batch_id+batch_size)*batch_unit):
                print('{}\t{}\t{}\t{}'.format(
                    batch_id_current, metric_value, metric_selected, batch_unit))
                with open("NDBench-testing-mapped.csv", "a+") as f:
                    # \n is for test
                    f.write('{}\t{}\t{}\t{}\n'.format(batch_id_current, metric_value, metric_selected, batch_unit))
            else:           
                continue
        except Exception:
            continue
