"""
remove judged documents from run file
"""
import argparse
from collections import defaultdict


def read_qrels(qrel_file):
    qrels = {}
    with open(qrel_file) as f:
        for line in f:
            cols = line.split()
            qid = cols[0]
            if qid not in qrels:
                qrels[qid] = set()
            docid = cols[2]
            qrels[qid].add(docid)
    return qrels


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('qrel_file')
    parser.add_argument('src_file')
    parser.add_argument('dest_file')
    parser.add_argument('--limit', type=int, default=1000)
    args=parser.parse_args()

    qrels = read_qrels(args.qrel_file)

    counts = defaultdict(int)
    with open(args.dest_file, 'w') as of:
        with open(args.src_file) as f:
            for line in f:
                cols = line.split()
                qid = cols[0]

                if counts[qid] >= args.limit:
                    continue
                docid = cols[2]
                if (
                    qid not in qrels
                    or docid not in qrels[qid]
                ):
                    counts[qid] += 1
                    of.write(line)


if __name__=='__main__':
    main()