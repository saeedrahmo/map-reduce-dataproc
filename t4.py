"""
    "rfw_id": 1,
    "benchmark_type":"ndbench",
    "workload_metric":"networkout_average",
    "batch_unit":1000,
    "batch_id":2,
    "batch_size":2,
    "data_type":"testing"

    ">=", req.body.batch_unit * req.body.batch_id
    "<", req.body.batch_unit * (req.body.batch_id + req.body.batch_size
"""

metric_dict = {
    "CPUUtilization_Average": 0,
    "NetworkIn_Average": 1,
    "NetworkOut_Average": 2,
    "MemoryUtilization_Average": 3,
    "Final_Target": 4
}
metric_selected = "MemoryUtilization_Average"

batch_size = 5
batch_id = 2
batch_unit = 10

counter_total = 0
counter_batch = batch_id-1

metric_current = ""

with open("NDBench-testing-mapped.csv") as file:
    for line in file:
        # remove leading and trailing whitespace
        line = line.strip()
        line = line.rstrip()
        # parse the input we got from mapper.py
        counter_batch, metric_selected, metric = line.split('\t')
        if metric_current != metric_selected:
            metric_selected = metric_selected

        counter_total += 1
        try:
            metric = line.rstrip().split(',')[metric_dict[metric_selected]]
            if metric.replace('.', '', 1).isdigit() == False:
                continue
            if (counter_total % (batch_unit) == 0) and (counter_total >= (batch_id*batch_unit)):
                counter_batch += 1
            if (counter_total >= batch_id*batch_unit) and (counter_total < (batch_id+batch_size)*batch_unit):
                print('{}\t{}\t{}\n'.format(
                    counter_batch, metric_selected, metric))
                with open("NDBench-testing-mapped.csv", "a+") as f:
                    # \n is for test
                    f.write('{}\t{}\t{}\n'.format(counter_batch,
                            metric_selected, metric))
        except Exception:
            continue
