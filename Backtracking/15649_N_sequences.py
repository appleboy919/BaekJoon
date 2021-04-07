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

    # set the first sequence and its number booleans to False
    for i in range(m):
        nums[i] = False
        seq.append(i + 1)
        end = False

    # start the loop printing out all the sequences
    while not end:
        current_num = seq[index]

        # print the until the last number reach the biggest possible number
        while True:
            print_list(seq)
            prv_num = current_num
            b_flag = True
            current_num += 1

            # find the next number for the last sequence number
            while current_num <= n:
                if nums[current_num - 1]:
                    nums[current_num - 1] = False
                    b_flag = False
                    break
                current_num += 1
            if b_flag:
                # this will exit the first inner loop
                break
            seq[index] = current_num
            nums[prv_num - 1] = True

        # increment previous index numbers
        backtrack = False
        while not end and not backtrack:
            nums[seq[index] - 1] = True
            index -= 1
            if index < 0:
                end = True
                break
            prv_num = seq[index]
            while seq[index] < n:
                seq[index] += 1
                if nums[seq[index] - 1]:
                    backtrack = True
                    nums[seq[index] - 1] = False
                    nums[prv_num - 1] = True
                    break

            # set the rest of the numbers
            if backtrack:
                while index < m - 1:
                    index += 1
                    new_num = 0
                    while new_num < n:
                        new_num += 1
                        if nums[new_num - 1]:
                            seq[index] = new_num
                            nums[new_num - 1] = False
                            break


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    print_sequences(M, N)
