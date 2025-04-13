import sys
import torch
from torch import Tensor

# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, 
# write a method to rotate the image by 90 degrees. Can you do this in place?
def rotateMatrix(mtx: torch.Tensor, inPlace: bool=False):
    print(mtx)
    N = mtx.shape[0]
    if inPlace:
        # TODO: implement implace version
        current_idx = dest_idx = next_idx = (0, 0)
        num_modified = 0
        while num_modified < N**2:

            dest_idx[0] = current_idx[1]
            dest_idx[1] = N - 1 - current_idx[0]

            temp = mtx[ dest_idx[0], dest_idx[1] ]
            mtx[ dest_idx[0], dest_idx[1] ] = mtx[ current_idx[0], current_idx[1] ] if num_modified < 1 else temp
            num_modified += 1

            current_idx = dest_idx

        return

    pass

def main():
    while(True):
        size = int(input("Enter the dimension of the square matrix (N): ").strip())
        elems = [int(i.strip()) for i in input("Now please enter a comma-separated list of the matrix elements row by row: ").strip().split(",")]
        if len(elems) != size**2:
            print("Mismatch in number of elements and dimensions, please try again.")
            continue
        mtx = torch.tensor(elems).view(size, size)
        break

    inPlace = input("Would you like this to be an in-place operation? (Yes/No): ").lower().strip()
    while(True):
        if inPlace == "yes":
            inPlace = True
        elif inPlace == "no":
            inPlace = False
        else:
            inPlace = input("Wrong input. Would you like this operation to be in-place? (Yes/No): ").lower().strip()
            continue
        break

    return rotateMatrix(mtx=mtx, inPlace=inPlace)

if __name__ == "__main__":
    main()