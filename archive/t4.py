batch_current = 0
metric_value_min = 0
metric_value_max = 0

with open("NDBench-testing-mapped.csv") as file:
    for line in file:
        # remove leading and trailing whitespace
        line = line.strip()
        line = line.rstrip()
        # parse the input we got from mapper.py
        batch_id_current, metric_selected, metric_value = line.split('\t')

        # convert count (currently a string) to int
        try:
            batch_id_current = int(batch_id_current)
        except ValueError:
            # count was not a number, so silently
            # ignore/discard this line
            continue

        if batch_current != batch_id_current:
            if(batch_current != 0) and (batch_id_current != 1) and (batch_id_current-batch_current == 1):
                print('batch_id: {}\t metric: {}\t min: {}\t max: {}\n'.format(
                    batch_current, metric_selected, metric_value_min, metric_value_max))

            batch_current = batch_id_current
            metric_value_min = metric_value
        else:
            metric_value_max = metric_value

print('batch_id: {}\t metric: {}\t min: {}\t max: {}\n'.format(
    batch_current, metric_selected, metric_value_min, metric_value_max))
