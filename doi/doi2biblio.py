#!/usr/bin/env python3                                                                                        

import os
import re
import requests
import argparse
import pprint

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', type=str)
args = parser.parse_args()

file_in = args.file

file_base = os.path.splitext(os.path.basename(file_in))[0]
file_ext = os.path.splitext(file_in)

file_out = str(file_base)+".out"+str(file_ext[1])
# print(file_out)      

url_base = "https://refindit.org/find"

with open(file_in) as f:
    with open(file_out, mode='w') as w:
        for doi_pre in f.readlines():
            doi = doi_pre.strip()

            params = {'search': 'simple', 'text': doi}

            response = requests.get(url_base, params=params)
            data = response.json()

            # pprint.pprint(data)                                                                             

            # 複数のDBに聞きに行くので、同じ結果が返ることがある。その重複をなくすための処理                  
            title_out = set()

            out = ""
            for eachdata in data:
                doi_out = eachdata['doi']
                title_pre = eachdata['title']
                year  = eachdata['year']

                if type(title_pre) == str:
                    ele = title_pre.split('\n')
                    ele = list(map(lambda x: x.strip(), ele))
                    ele = list(map(lambda x: re.sub(re.compile('<.*?>'), '', x), ele))
                    title = "".join(ele)
                elif type(title_pre) == dict:
                    title = "".join(title_pre).strip()

                # pprint.pprint(eachdata)                                                                     

                if doi_out == doi:
                    out = "\t".join([doi, title, str(year)])
                    break

            if out == "":
                out = "\t".join([doi, "-", "-"])

            print(out)
            w.write(out+"\n")

            out = ""
