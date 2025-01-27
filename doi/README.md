# DOI (Digital Object Identifier)
- デジタルなコンテンツに対して共通のIDの形で採番して、URLの形でデータにアクセスを担保したり、URLが変わっても追随してデータにアクセスできるようにする仕組み
- 論文、データセットなどにDOIが振られる。
- 例：10.3389/fevo.2022.966605
- https://doi.org/ の後ろにDOIを記述するとURL解決されて当該ページにリダイレクトされる
  - https://doi.org/10.3389/fevo.2022.966605 → https://www.frontiersin.org/journals/ecology-and-evolution/articles/10.3389/fevo.2022.966605/full
 
# DOIからの書誌情報の取得
- doi2biblio.py

## refindit.org
- https://refindit.org/ のAPIを用いている
- 返ってくるデータの中身の例
```
{'authors': [['Ya-nan', 'Wang'],
             ['Lei', 'Wang'],
             ['Yiu Fai', 'Tsang'],
             ['Xiaohua', 'Fu'],
             ['Jiajun', 'Hu'],
             ['Huan', 'Li'],
             ['Yiquan', 'Le']],
 'doi': '10.1016/j.ibiod.2016.03.002',
 'epage': '112',
 'firstauthor': ['Ya-nan', 'Wang'],
 'href': 'https://doi.org/10.1016/j.ibiod.2016.03.002',
 'id': '10.1016/j.ibiod.2016.03.002',
 'isParsed': True,
 'publicationDate': '2016-9',
 'publishedIn': 'International Biodeterioration &amp; Biodegradation',
 'score': 0,
 'source': 'CrossRef',
 'spage': '105',
 'title': 'The variability in carbon fixation characteristics of several '
          'typical chemoautotrophic bacteria at low and high concentrations of '
          'CO 2 and its mechanism',
 'type': 'journal-article',
 'volume': '113',
 'year': 2016}
```
```
{'authors': [['Michael', 'Friedrich'], ['Bernhard', 'Schink']],
 'doi': '10.1007/BF02529961',
 'epage': '279',
 'firstauthor': ['Michael', 'Friedrich'],
 'href': 'https://www.mendeley.com/catalogue/6d999c33-1004-31a8-bb0b-be7e73954d2d/',
 'id': {'doi': '10.1007/BF02529961',
        'issn': '03028933',
        'pii': 'BF02529961',
        'pui': '225183746',
        'scopus': '2-s2.0-0028827408',
        'sgr': '0028827408'},
 'isParsed': True,
 'issue': '4',
 'publishedIn': 'Archives of Microbiology',
 'source': 'Mendeley',
 'spage': '271',
 'title': 'Isolation and characterization of a desulforubidin-containing '
          'sulfate-reducing bacterium growing with glycolate',
 'volume': '164',
 'year': 1995}
```
```
{'abstract': 'Oxidative stress is thought to be related to many diseases. '
             'Furthermore, it is hypothesized that radiofrequency '
             'electromagnetic fields (RF-EMF) may induce excessive oxidative '
             'stress in various cell types and thereby have the potential to '
             'compromise human and animal health. The objective of this '
             'systematic review (SR) is to summarize and evaluate the '
             'literature on the relation between the exposure to RF-EMF in the '
             'frequency range from 100\xa0kHz to 300\xa0GHz and biomarkers of '
             'oxidative stress.',
 'authors': [['Felix', 'Meyer'],
             ['Annette', 'Bitsch'],
             ['Henry Jay', 'Forman'],
             ['Athanassios', 'Fragoulis'],
             ['Pietro', 'Ghezzi'],
             ['Bernd', 'Henschenmacher'],
             ['Rupert', 'Kellner'],
             ['Jens', 'Kuhne'],
             ['Tonia', 'Ludwig'],
             ['Dmitrij', 'Sachno'],
             ['Gernot', 'Schmid'],
             ['Katya', 'Tsaioun'],
             ['Jos', 'Verbeek'],
             ['Robert', 'Wright']],
 'doi': '10.1016/j.envint.2024.108940',
 'firstauthor': ['Felix', 'Meyer'],
 'href': 'http://dx.doi.org/10.1016/j.envint.2024.108940',
 'id': {'pubmed': '39566441'},
 'infoUrl': 'http://www.ncbi.nlm.nih.gov/pubmed/39566441',
 'isParsed': True,
 'publishedIn': 'Environment international',
 'source': 'PubMed',
 'spage': '108940',
 'title': 'The effects of radiofrequency electromagnetic field exposure on '
          'biomarkers of oxidative stress in vivo and in vitro: A systematic '
          'review of experimental studies.',
 'volume': '194',
 'year': '2024'}
```

## doi.org
- https://citation.doi.org/api-docs.html
```
$ curl https://citation.doi.org/metadata?doi=10.1145/2783446.2783605
```
