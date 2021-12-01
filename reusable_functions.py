# Ben Geyer

def read_ints_from_file(filename='input'):
    with open(filename) as f:
        return [int(line.strip()) for line in f.readlines() if len(line) > 0]
