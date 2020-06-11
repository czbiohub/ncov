#!/usr/bin/env python3

import pandas as pd
import argparse
import re

def get_county(row):
    division = row['division']
    location = row['location']
    if isinstance(division, str) and isinstance(location, str):
        if division.lower()=='california':
            county = location

            if division.lower() == 'grand princess' or location.lower() == 'grand princess cruise ship':
                return 'Grand Princess Cruise Ship'

            if 'county' in location.lower():
                county = re.search('(.+)\scounty', location.lower()).group(1)
                county = ' '.join([s.capitalize() for s in county.split()])
            if 'davis' in location.lower():
                county = 'Yolo'

            return county

    return '?'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--metadata', help='nextstrain metadata TSV')
    parser.add_argument('--output', help='output metadata file (default: metadata.tsv)', default='metadata.tsv')
    
    args = parser.parse_args()

    meta = pd.read_csv(args.metadata, sep='\t')
    meta['county'] = meta.apply(get_county, axis=1)

    meta.to_csv(args.output, sep='\t', index=False)

if __name__ == '__main__':
    main()