"""
merge results produced for round 1 queries with results produced for round 2 queries
"""
import argparse
from collections import defaultdict


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--round1_input', type=str, metavar='run', help='input run', required=True)
    parser.add_argument('--round2_input', type=str, metavar='run', help='input run', required=True)
    parser.add_argument('--runtag', type=str, metavar='runtag', help='runtag', required=True)
    parser.add_argument('--output', type=str, metavar='run', help='output run', required=True)
    parser.add_argument(
        '--k', type=int, default=1000,
        help='the number of results to keep per-topic'
    )
    args=parser.parse_args()

    counts = defaultdict(int)

    with open(args.output, 'w') as output_f:
        with open(args.round1_input) as input1_f:
            for line in input1_f:
                cols = line.split()
                qid = cols[0]

                if int(qid) >30:
                    continue
                docid = cols[2]
                score = cols[4]

                if counts[qid] >= args.k:
                    continue

                else:
                    counts[qid] += 1
                    output_f.write(f'{qid} Q0 {docid} {counts[qid]} {score} {args.runtag}\n')

        with open(args.round2_input) as input2_f:
            for line in input2_f:
                cols = line.split()
                qid = cols[0]

                if int(qid) <= 30:
                    continue
                docid = cols[2]
                score = cols[4]

                if counts[qid] >= args.k:
                    continue

                else:
                    counts[qid] += 1
                    output_f.write(f'{qid} Q0 {docid} {counts[qid]} {score} {args.runtag}\n')



if __name__=='__main__':
    main()
