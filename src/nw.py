import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--A',
                        type=str,
                        required=True,
                        help='Sequence A')
    parser.add_argument('--B',
                        type=str,
                        required=True,
                        help='Sequence B')
    parser.add_argument('--gap',
                        type=int,
                        default=-2,
                        help='Gap penalty (default: -2)')
    parser.add_argument('--miss',
                        type=int,
                        default=-1,
                        help='Mismatch penalty (default: -1)')
    parser.add_argument('--match',
                        type=int,
                        default=1,
                        help='Match score (default: 1)')
    return parser.parse_args()


def nw_fill_matrix(A, B, gap, miss, match):
    H = [[0 for j in range(len(B) + 1)] for i in range(len(A) + 1)]


    for i in range(1, len(A) + 1):
        H[i][0] = H[i-1][0] + gap

    for j in range(1, len(B) + 1):
        H[0][j] = H[0][j-1] + gap   

    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            H[i][j] = max( H[i-1][j-1] + (match if A[i-1] == B[j-1] else miss),
                           H[i-1][j] + gap,
                           H[i][j-1] + gap)

    return H

def nw_traceback(H, A, B, gap, miss, match):
    i = len(A)
    j = len(B)
    score = H[i][j]
    align_A = []
    align_B = []
    while i > 0 or j > 0:
        if H[i][j] == H[i-1][j-1] + (match if A[i-1] == B[j-1] else miss):
            align_A.append(A[i-1])
            align_B.append(B[j-1])
            i -= 1
            j -= 1
        elif H[i][j] == H[i-1][j] + gap:
            align_A.append(A[i-1])
            align_B.append('-')
            i -= 1
        elif H[i][j] == H[i][j-1] + gap:
            align_A.append('-')
            align_B.append(B[j-1])
            j -= 1
        else:
            break
    return ''.join(align_A[::-1]), ''.join(align_B[::-1]), score

def main():
    args = get_args()

    H = nw_fill_matrix(args.A, args.B, args.gap, args.miss, args.match)

    align_A, align_B, score = nw_traceback(H,
                                           args.A,
                                           args.B,
                                           args.gap,
                                           args.miss,
                                           args.match)
    print(align_A)
    print(align_B)
    print('Score:', score)

if __name__ == '__main__':
    main()
