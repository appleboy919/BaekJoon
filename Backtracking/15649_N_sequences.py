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
        seq.append(i + 1)

    while True:
        while True:
            print_list(seq)
            prv_num = current_num
            b_flag = True
            current_num += 1
            while current_num <= n:
                if nums[current_num - 1]:
                    nums[current_num - 1] = False
                    b_flag = False
                    break
                current_num += 1
            if b_flag:
                # this is end of loop
                break
            seq[index] = current_num
            nums[prv_num - 1] = True

        # increment previous index number
        loop_flag = True
        while loop_flag:
            index -= 1
            prv_num = seq[index]
            while seq[index] <= n:
                seq[index] += 1
                if nums[seq[index] - 1]:
                    loop_flag = False
                    nums[seq[index] - 1] = False
                    nums[prv_num - 1] = True
                    break
        # start the other later indices numbers to the smallest numbers
        # code here


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    print_sequences(M, N)
