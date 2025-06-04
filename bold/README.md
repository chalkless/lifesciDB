# BOLD (Barcode of Life System)
- DNAバーコードを集めるプロジェクトのデータベース
- https://boldsystems.org/
- 2024年にv5がリリースされた

## データのダウンロード
- ヘッダ部分の Data → Data Packages。ページの真ん中あたりにLatestと書かれたリンクがある → https://bench.boldsystems.org/index.php/datapackages/Latest
  - Summary: 6kB	
  - Data Package Metadata: 30kB	
  - Data package (tar.gz compressed) * :	3GB (tar.gz compressed)
  - Sequences in Fasta format (gz compressed) * :	2GB (gz compressed)
- `*` はログイン必要
- もしかして週1更新???

### Data package
- 解凍すると26GBのtsvと31kBのJSON
- JSONファイルは各列の解説：https://github.com/chalkless/lifesciDB/blob/master/bold/BOLD_Public.23-May-2025.datapackage.json
- 上記 LATEST ページにも同じ解説があるが、実際にデータ加工しようとすると列番号が重要なので上のJSONを見るのが便利

## データ利用例
- 昆虫だけに絞り込んで、必要なところだけをファイルに書き出す
```
$ perl -F"\t" -lane 'print $_ if $F[15] eq "Insecta"' /data/bold/250530/datapackage/BOLD_Public.23-May-2025.tsv | cut -f 1,2,4,5,6,8,13,69,71,74 > bold.250523.insect.slim.tab
```

```
 1	processid
 2	sampleid
 4	museumid
 5  record_id
 6	specimenid
 8  bin_uri
13  taxid
69  insdc_acs
71	markercode    <- gene name
74  sequence_run_site  <- "Mined from GenBank, NCBI"はここに
```

