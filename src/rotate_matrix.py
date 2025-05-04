import sys

# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, 
# write a method to rotate the image by 90 degrees. Can you do this in place?
def rotate_matrix(mtx: list, in_place: bool=False):
    print("Initial: \n", mtx)
    N = len(mtx)

    if N <= 1:
        return mtx

    if in_place:
        start = [0 , 0]
        
        while start[0] <= float((N - 1)) / 2:
            for k in range(N - 1 - (2 * start[0])):
                swap_start = (start[0], start[1] + k)
                curr_loc = swap_start
                curr_val = mtx[curr_loc[0]][curr_loc[1]]

                while True:
                    dest = (curr_loc[1], N - 1 - curr_loc[0])
                    displace_val = mtx[dest[0]][dest[1]]
                    
                    mtx[dest[0]][dest[1]] = curr_val
                    curr_loc = dest
                    curr_val = displace_val

                    # if we are back to the same location end loop
                    if (curr_loc == swap_start):
                        break

            start[0] += 1
            start[1] += 1
        
        return mtx

    else:
        result = [list() for _ in range(N)]

        for i in range(N):
            for j in range(N):
                result[i].append(mtx[N - 1 - j][i])

        return result


def main():
    result = None

    while(True):
        N = int(input("Enter the dimension of the square matrix (N): ").strip())
        elems = [int(i.strip()) for i in input("Now please enter a comma-separated list of the matrix elements row by row: ").strip().split(",")]

        if len(elems) != N**2:
            print("Mismatch in number of elements and dimensions, please try again.")
            continue
        
        mtx = [[[0] for _ in range(N)] for _ in range(N)]
        elems = iter(elems)

        for i in range(N):
            for j in range(N):
                mtx[i][j] = next(elems)

        break

    inPlace = input("Would you like this to be an in-place operation? (Yes/No): ").lower().strip()

    while(True):
        if inPlace == "yes":
            result = rotate_matrix(mtx=mtx, in_place=True)
            break
        elif inPlace == "no":
            result = rotate_matrix(mtx=mtx, in_place=False)
            break
        else:
            inPlace = input("Wrong input. Would you like this operation to be in-place? (Yes/No): ").lower().strip()
            continue

    print("Result: \n", result)
    return result

if __name__ == "__main__":
    main()