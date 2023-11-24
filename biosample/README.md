# BioSample
## データの取得
```
https://ddbj.nig.ac.jp/public/ddbj_database/biosample/
	Parent Directory	 	-
 	biosample_set.xml.gz	2023-11-23 22:22	2.5G
 	ddbj_biosample_set.xml.gz	2023-11-24 01:33	16M
 	ddbj_summary.txt	2023-11-24 01:32	15M
 	schema/	2014-09-25 10:02	-
```

```
https://ftp.ncbi.nlm.nih.gov/biosample/
Parent Directory                             -   
biosample_set.xml.gz    2023-11-23 08:22  2.5G  
```

- DDBJではNCBIのファイルがミラーされている（と信じている）


## BioSampleデータの中身

```
$ head biosample_set.xml
<?xml version="1.0" encoding="UTF-8"?>
<BioSampleSet>
<BioSample submission_date="2008-04-04T08:44:24.950" last_update="2022-09-25T02:00:02.729" publication_date="2008-04-04T00:00:00.000" access="public" id="2" accession="SAMN00000002">
  <Ids>
    <Id db="BioSample" is_primary="1">SAMN00000002</Id>
    <Id db="WUGSC" db_label="Sample name">19655</Id>
    <Id db="SRA">SRS000002</Id>
  </Ids>
  <Description>
    <Title>Alistipes putredinis DSM 17216</Title>
```

```
$ head ddbj_biosample_set.xml 
<?xml version="1.0" encoding="ISO-8859-1"?>
<BioSampleSet>
        <BioSample last_update="2022-04-05T17:24:38.000+09:00" publication_date="2014-04-07T00:00:00.000+09:00" access="public">
                <Ids>
                        <Id namespace="BioSample" is_primary="1">SAMD00000001</Id>
                </Ids>
                <Description>
                        <SampleName>Bradyrhizobium sp. DOA9</SampleName>
                        <Title>MIGS Cultured Bacterial/Archaeal sample from Bradyrhizobium sp. DOA9</Title>
                        <Organism taxonomy_id="1126627">
```

## BioSampleデータのparse
```
#!/usr/bin/env python3                                                           

import argparse
import xml.etree.ElementTree as ET

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', type=str)
args = parser.parse_args()

file_in = args.file

tree = ET.parse(file_in)
root = tree.getroot()

for biosample in root:
    for sample in biosample:
        print(sample.tag)
```

```
$ python3 /share/bin/bio/parse.biosample.py -f ddbj_biosample_set.xml | head
Ids
Description
Owner
Models
Attributes
Links
...

$ python3 /share/bin/bio/parse.biosample.py -f ddbj_biosample_set.xml | sort | uniq -c
 442332 Attributes
 442332 Description
 442332 Ids
  11554 Links
 442332 Models
 442332 Owner
```
