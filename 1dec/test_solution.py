from solution import solve_A, solve_B

def test_example_A():
    assert solve_A('sample.txt') == 11

def test_example_B():
    assert solve_B('sample.txt') == 31