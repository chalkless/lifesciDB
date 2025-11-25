# MeSH (Medical Subject Headings)
- PubMedのindex用（＝索引付け用）キーワード集
- 階層構造になっている
- さまざまな分野の用語が集められている（器官・組織名、生物名、疾患、物質名、生命現象など）
- データの入手先：https://www.nlm.nih.gov/mesh/meshhome.html
- MeSHの各用語の詳細をウェブから確認したいとき：https://www.ncbi.nlm.nih.gov/mesh
- 毎年12月頃に更新される

## データの入手
- https://www.nlm.nih.gov/mesh/meshhome.html にアクセスする
- Obtain MeSH Data 欄に [Download MeSH Data](https://www.nlm.nih.gov/databases/download/mesh.html) があるのでクリックする
- XML, ASCII, RDFなどの形式でファイルが配布されているが、人間が加工しやすいのはASCII形式。過去のファイルもこのページからアクセスできる
- [Download Current Production Year MeSH in ASCII format](https://nlmpubs.nlm.nih.gov/projects/mesh/MESH_FILES/asciimesh/) にアクセスする
- ファイルが3つ置かれていいる（数字は最新版の西暦）
  - c2025.bin：Substance Names。つまりは物質名などのリスト。MeSHにも物質名があるが、それとは別でこちらの方が数が多い。2025年版は118MB。
  - d2025.bin：MeSH本体。2025年版は30MB。
  - q2025.bin：Qualifier。修飾語。あまり使わなくてもいい気はしないでもない
- これの他に、MeSHの階層構造をまとめたファイルがある
  - https://nlmpubs.nlm.nih.gov/projects/mesh/MESH_FILES/meshtrees/ に置かれている（さきほどのASCII形式のファイル群の1つ上の階層からたどれる）
  - mtrees2025.bin：用語と階層構造の場所を記載したファイル。2025年版は2.6MB

## データ例
- MeSH（生物種データ）
```
*NEWRECORD
RECTYPE = D
MH = Bacillus subtilis      ← 用語
AQ = CH CL CY DE EN GD GE IM IP ME PH PY RE UL VI
PRINT ENTRY = Natto Bacteria|T007|NON|NRW|NLM (2004)|030507|abcdef
ENTRY = Bacillus subtilis (natto)|T007|NON|NRW|NLM (2004)|030507|abcdef    ← Entry Term。この語が来たら、当該MeSH用語に変換される。別の表現と思えばよい。
ENTRY = Bacillus subtilis subsp. natto|T007|NRW|NLM (2020)|191001|abdef
ENTRY = Bacillus subtilis var. natto|T007|NON|NRW|NLM (2004)|030507|abcdef
MN = B03.300.390.400.158.218.725    ← Tree ID。用語が階層構造になっているので、その親子関係を表す。複数可。親の用語は末尾の.XXXを削ったID
MN = B03.353.500.100.218.725
MN = B03.510.100.100.218.725
MN = B03.510.415.400.158.218.725
MN = B03.510.460.410.158.218.725
MH_TH = NLM (1966)
ST = T007
RN = txid1423    ← Registry Number。この場合はここにTaxonomy IDが書かれている。今回はBacillus subtilisのTaxonomy ID
RR = txid86029   ← こちらはRelated Registry Number。今回の場合は、Bacillus subtilis subsp. nattoのTaxonomy ID
MS = A species of gram-positive bacteria that is a common soil and water saprophyte.
LU = 20230522
DC = 1
DX = 19660101
UI = D001412    ← 用語自体のID
```

- mtreesXXXX.bin
```
 Body Regions;A01   ← Tree IDの若い順に並んでいる
 Anatomic Landmarks;A01.111 ← 先頭に1文字空白文字が入っていることに注意
 Breast;A01.236
 Mammary Glands, Human;A01.236.249
 Nipples;A01.236.500
 Extremities;A01.378
 Amputation Stumps;A01.378.100
 ...
 Bacillus subtilis;B03.300.390.400.158.218.725   ← 同じ用語がTreeの複数の箇所にあるので、当該Tree IDのところで複数回同じ用語が出てくる
 ...
 Bacillus subtilis;B03.353.500.100.218.725  ← よく見ると、末尾付近の数字が一緒だが、これはグラフで言うと途中で分かれてまた戻るDAGになっているから
 ...
 Bacillus subtilis;B03.510.100.100.218.725
 ...
 Bacillus subtilis;B03.510.415.400.158.218.725
 ...
 Bacillus subtilis;B03.510.460.410.158.218.725
 ...
```
