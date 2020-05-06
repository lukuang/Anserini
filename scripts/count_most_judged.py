"""
Count the most number of judged documents per-topic
"""

import argparse


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
    args=parser.parse_args()

    qrels = read_qrels(args.qrel_file)

    max_count = max(map(len, qrels.values()))
    print (f'max count: {max_count}')


if __name__=='__main__':
    main()
