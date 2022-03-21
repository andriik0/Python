def main():
    logs_count = int(input())
    queue = []
    for _ in range(logs_count):
        log_record = input()
        if 'EXTRA' in log_record.upper():
            rec = queue[0]
            queue = [x for ind, x in enumerate(queue) if ind > 0]
            queue.append(rec)
            continue

        if 'PASSED' in log_record.upper():
            q_len = len(queue)
            if q_len > 0:
                rec = queue[0]
                print(rec[rec.find(' ') + 1:])
                queue = [x for ind, x in enumerate(queue) if ind > 0]
                continue

        queue.append(log_record)



if __name__ == '__main__':
    main()
