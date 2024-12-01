import numpy as np

def solve_A(filepath):
    '''run this to solve part A problem'''
    id1, id2  = format_input(filepath) 
    id1.sort()
    id2.sort()
    one_norm = np.linalg.norm(id1 - id2, ord=1)

    return one_norm

def solve_B(filepath):
    '''run this to solve part B problem'''
    id1, id2 = format_input(filepath)
    score = 0
    for locus in id1:
        frequency = np.count_nonzero(id2 == locus)
        score += locus * frequency

    return score

def format_input(filepath):
    '''open file and return the two required columns as numpy arrays'''
    col1_list = []
    col2_list = []
    with open(filepath, "r") as file:
        lines = file.readlines()
        for line in lines:
            linesplit = line.split()
            col1_list.append(int(linesplit[0]))
            col2_list.append(int(linesplit[1]))
    col1 = np.array(col1_list)
    col2 = np.array(col2_list)
    return col1, col2

if __name__ == "__main__":
    print(f"\nSolution to Part A is {solve_A('input.txt')}")
    print(f"\nSolution to Part B is {solve_B('input.txt')}")
