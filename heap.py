
import heapq


def execute_command(heap, cmd):

    if cmd.startswith('Insert'):
        action, value = cmd.split()
        heapq.heappush(heap, -int(value))
    elif cmd.startswith('ExtractMax'):
        print(-heapq.heappop(heap))
    else:
        pass


if __name__ == "__main__":

    n_strings = int(input())
    heap = []
    heapq.heapify(heap)

    cmds = []
    for i in range(n_strings):
        cmds.append(input())

    for cmd in cmds:
        execute_command(heap, cmd)
