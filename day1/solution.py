# Ben Geyer
# Solves part 1 and 2 of the advent with a single function by simply changing the window_size from 1 to 3

def perform_comparisons(lines, window_size=1):
    # compares windows for increasing, decreasing, and equal changes in sum for validation
    inc_count = 0
    dec_count = 0
    eq_count = 0
    for idx in range(len(lines)):
        start = idx
        stop = idx+window_size
        curr_window = lines[start:stop]
        next_window = lines[start+1:stop+1]
        curr = sum(curr_window)
        next = sum(next_window)
        if len(curr_window) == window_size and len(next_window) == window_size:
            # ensures only windows of proper size are considered
            if curr < next:
                inc_count += 1
            elif curr > next:
                dec_count += 1
            else:
                eq_count += 1
    print(f'Window Size: {window_size} \
            \nIncreasing Windows: {inc_count} \
            \nDecreasing Windows: {dec_count} \
            \nEqual Windows: {eq_count} \
            \nTotal Comparisons: {inc_count+dec_count+eq_count}')
    return inc_count

if __name__ == "__main__":
    with open('input') as fp:
        lines = [int(line.strip()) for line in fp.readlines() if len(line) > 0]
        # change window_size here from 3 to 1 for Part 1 instead of Part 2
        inc = perform_comparisons(lines, window_size=3)
