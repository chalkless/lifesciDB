import requests
import os
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

url_base = "http://refindit.org/find"

with open(file_in) as f:
    with open(file_out, mode='w') as w:
        for doi_pre in f.readlines():
            doi = doi_pre.strip()
            params = {'search': 'simple', 'text': doi}
            response = requests.get(url_base, params=params)
            data = response.json()

            #      pprint.pprint(data)

            # 複数のDBに聞きに行くので、同じ結果が返ることがある。その重複をなくすための処理
            title_out = set()
            title = ""

            for eachdata in data:
                doi_out = eachdata['doi']
                title_pre = eachdata['title']

                if type(title_pre) == str:
                    title = title_pre
                elif type(title_pre) == dict:
                    title = "".join(title_pre).strip()                    
                
                if doi_out == doi:
                    #          print("\t".join([doi, title]))
                    title_out.add(title)

                    for eachtitle in title_out:
                        str_out = "\t".join([doi, eachtitle])
                        print(str_out)
                        w.write(str_out+"\n")
