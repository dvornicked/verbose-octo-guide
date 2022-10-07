import os, re

config = {
    "LOG_DIR": "./log"
}


def main():
    log_name = os.listdir(config.get('LOG_DIR'))[-1]
    pattern = re.compile(r'\"[A-Z]+ (\S+) .* (\d+\.\d+)\n')
    data = {}
    total_count = 0
    with open(f'{config.get("LOG_DIR")}/{log_name}', 'r') as file:
        for line in file:
            result = pattern.findall(line)
            total_count += 1
            if not len(result): continue
            url, time = result[0]
            if url not in data: data[url] = []
            data[url].append(float(time))

    for key in data:
        count = len(data[key])
        print(f'URL: {key}'
              f'\tcount: {count}'
              f'\n\tcount_perc: {count/total_count * 100}'
              f'\n\ttime_avg: {sum(data[key])/count}'
              f'\n\ttime_max: {max(data[key])}'
              f'\n\ttime_med: {data[key][count//2]}')


if __name__ == "__main__":
    main()
