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
selected_metric = "Final_Target"

batch_size = 2
batch_id = 2
batch_unit = 10

counter_total = 0
counter_batch = batch_id-1

with open("NDBench-testing.csv") as file:
    for line in file:
        counter_total += 1
        try:
            metric = line.rstrip().split(',')[metric_dict[selected_metric]]
            if metric.replace('.', '', 1).isdigit() == False:
                continue
            if (counter_total % (batch_unit) == 0) and (counter_total >= (batch_id*batch_unit)):
                counter_batch += 1
            if (counter_total >= batch_id*batch_unit) and (counter_total < (batch_id+batch_size)*batch_unit):
                print(counter_batch, counter_total, metric)
        except Exception:
            continue
        # print(line.rstrip().split(',')[0])  # rstrip()
