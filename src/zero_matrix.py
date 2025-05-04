from collections import defaultdict

# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and columns are set to 0.

def zero_matrix(mtx):
    M = len(mtx)
    N = len(mtx[0])

    zero_rows = defaultdict(int)
    zero_cols = defaultdict(int)

    for i in range(M):
        for j in range(N):
            if mtx[i][j] == 0:
                zero_rows[i] += 1
                zero_cols[j] += 1

    for i in range(M):
        for j in range(N):
            if zero_rows[i] > 0 or zero_cols[j] > 0:
                mtx[i][j] = 0


def zero_matrix2(mtx):
    M = len(mtx)
    N = len(mtx[0])

    zero_rows = defaultdict(int)
    zero_cols = defaultdict(int)

    for i in range(M):
        for j in range(N):
            if zero_rows[i] > 0:
                break

            if zero_cols[j] > 0:
                continue

            if mtx[i][j] == 0:    
                zero_rows[i] += 1
                zero_cols[j] += 1
                zero_row_col(mtx, i, j)

def zero_row_col(mtx, row_idx, col_idx):
    M = len(mtx)
    N = len(mtx[0])

    for i in range(M):
        mtx[i][col_idx] = 0

    for j in range(N):
        mtx[row_idx][j] = 0

def main():
    while(True):
        M, N = [int(d.strip()) for d in input("Enter the dimensions of the  matrix - comma separated (M , N): ").strip().split(",")]
        elems = [int(i.strip()) for i in input("Now please enter a comma-separated list of the matrix elements row by row: ").strip().split(",")]

        if len(elems) != M*N:
            print("Mismatch in number of elements and dimensions, please try again.")
            continue
        
        mtx = [[[0] for _ in range(N)] for _ in range(M)]
        elems = iter(elems)

        for i in range(M):
            for j in range(N):
                mtx[i][j] = next(elems)

        break
    
    zero_matrix2(mtx)

    print("Result: \n", mtx)
    return mtx

if __name__ == "__main__":
    main()