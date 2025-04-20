import sys

# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, 
# write a method to rotate the image by 90 degrees. Can you do this in place?
def rotate_matrix(mtx: list, in_place: bool=False):
    print(mtx)
    N = len(mtx)

    result = [list() for _ in range(N)]

    if in_place:
        # TODO: implement in place version
        current_idx = dest_idx = next_idx = (0, 0)
        num_modified = 0
        while num_modified < N**2:

            dest_idx[0] = current_idx[1]
            dest_idx[1] = N - 1 - current_idx[0]

            temp = mtx[ dest_idx[0], dest_idx[1] ]
            mtx[ dest_idx[0], dest_idx[1] ] = mtx[ current_idx[0], current_idx[1] ] if num_modified < 1 else temp
            num_modified += 1

            current_idx = dest_idx

    else:
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