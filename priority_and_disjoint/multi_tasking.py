import heapq

if __name__ == '__main__':

    n_procs, m_tasks = [x for x in map(int, input().split())]
    times = [x for x in map(int, input().split())]

    q = [(0, proc) for proc in range(n_procs)]
    heapq.heapify(q)

    for task in range(m_tasks):
        next_t, next_proc = heapq.heappop(q)
        print(next_proc, next_t)
        heapq.heappush(q, (next_t + times[task], next_proc))