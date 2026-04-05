def first_fit(blocks, processes):
    allocation = [-1] * len(processes)
    b = blocks.copy()

    for i in range(len(processes)):
        for j in range(len(b)):
            if b[j] >= processes[i]:
                allocation[i] = j
                b[j] -= processes[i]
                break

    return allocation, b


def best_fit(blocks, processes):
    allocation = [-1] * len(processes)
    b = blocks.copy()

    for i in range(len(processes)):
        best_idx = -1
        for j in range(len(b)):
            if b[j] >= processes[i]:
                if best_idx == -1 or b[j] < b[best_idx]:
                    best_idx = j

        if best_idx != -1:
            allocation[i] = best_idx
            b[best_idx] -= processes[i]

    return allocation, b


def worst_fit(blocks, processes):
    allocation = [-1] * len(processes)
    b = blocks.copy()

    for i in range(len(processes)):
        worst_idx = -1
        for j in range(len(b)):
            if b[j] >= processes[i]:
                if worst_idx == -1 or b[j] > b[worst_idx]:
                    worst_idx = j

        if worst_idx != -1:
            allocation[i] = worst_idx
            b[worst_idx] -= processes[i]

    return allocation, b


def calculate_utilization(blocks, remaining):
    total_memory = sum(blocks)
    used_memory = total_memory - sum(remaining)
    utilization = (used_memory / total_memory) * 100
    fragmentation = sum(remaining)

    return utilization, fragmentation


def display(strategy, allocation, processes, remaining, blocks):
    print(f"\n--- {strategy} ---")
    print("Process No.\tProcess Size\tBlock No.")

    for i in range(len(processes)):
        if allocation[i] != -1:
            print(f"{i+1}\t\t{processes[i]}\t\t{allocation[i]+1}")
        else:
            print(f"{i+1}\t\t{processes[i]}\t\tNot Allocated")

    util, frag = calculate_utilization(blocks, remaining)
    print(f"Memory Utilization: {util:.2f}%")
    print(f"Total Fragmentation: {frag}")


# INPUT
blocks = [100, 500, 200, 300, 600]
processes = [212, 417, 112, 426]

# RUN STRATEGIES
ff_alloc, ff_rem = first_fit(blocks, processes)
bf_alloc, bf_rem = best_fit(blocks, processes)
wf_alloc, wf_rem = worst_fit(blocks, processes)

# DISPLAY RESULTS
display("First Fit", ff_alloc, processes, ff_rem, blocks)
display("Best Fit", bf_alloc, processes, bf_rem, blocks)
display("Worst Fit", wf_alloc, processes, wf_rem, blocks)
