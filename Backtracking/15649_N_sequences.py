import sys


def print_list(list):
    for i in list:
        sys.stdout.write(str(i) + ' ')
    sys.stdout.write('\n')


def print_sequences(m, n):
    nums = [True] * n
    seq = []
    current_num = m
    index = m - 1

    for i in range(m):
        nums[i] = False
        seq.append(i)
   
    while True:
        while True:
            print_list(seq)
            prv_num = current_num
            while current_num <= n:
                current_num += 1
                if nums[current_num-1]:
                    nums[current_num-1] = False
                    break
            if prv_num == current_num:
                #this is end of loop
                break
            seq[m-1] = current_num
            nums[prv_num] = True

        # increment previous index number
        while True:
            index += 1
            while seq[index] <= n:
                seq[index] += 1
                if nums[seq[index]]:
                    break

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    print_sequences(M, N)
