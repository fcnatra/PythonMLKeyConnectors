
def get_row(A, i):
    return A[i]

def get_column(A, j):
    return [A_i[j] for A_i in A]

"""returns a num_rows x num_cols matrix whose (i,j)th entry is entry_fn(i, j)"""
def make_matrix(num_rows, num_cols, entry_fn):
    return [[entry_fn(i, j) for j in range(num_cols)] for i in range(num_rows)] # create one list for each i

"""1's on the 'diagonal', 0's everywhere else"""
def is_diagonal(i, j):
    return 1 if i == j else 0
