# SRA (Sequence Read Archive)
- https://ftp.ncbi.nlm.nih.gov/sra/reports/Metadata/SRA_Accessions.tab
- 2023/7/20現在：19GB
- wget するとなかなかに時間がかかる（そして途中で切れてやり直す。続きからではあるが）
- lftpかrsyncか。。。

```
$ lftp -e 'get /sra/reports/Metadata/SRA_Accessions.tab' ftp.ncbi.nlm.nih.gov
```


|Label|Study|Experiment|Run|Sample|
|-|-|-|-|-|
|Accession|SRP072219|ERX1858811|ERR4799434|SRS8633180|
|Submission|-|-|-|-|-|
|Status|live|live|live|live|
|Updated|2016-03-29T17:15:28Z|2017-01-16T11:47:05Z|2023-06-23T23:25:11Z|2021-04-03T15:03:54Z|
|Published|2016-03-29T17:15:28Z|2017-01-14T18:47:32Z|2021-11-10T12:53:11Z|2021-04-03T14:24:10Z|
|Received|2016-03-23T15:40:12Z|2017-01-14T18:45:45Z|2021-10-21T02:29:18Z|2021-04-03T14:24:10Z|
|Type|STUDY|EXPERIMENT|RUN|SAMPLE|
|Center|University of Michigan|SC|Foundation for Medical Research India|pda/tkenzaka|
|Visibility|public|public|public|public|
|Alias|The Bacterial Topography of the Healthy Human Respiratory Tract|SC_454_EXP_G7SLMNB01_MID1_ARI0073_07B00909_A|run.27899|1806-1-R1|
|Experiment|-|-|ERX4668851|-|
|Sample|-|ERS1474968|ERS5284491|-|
|Study|-|ERP020597|ERP124850|-|
|Loaded|-|-|1|-|
|Spots|-|-|43005251|-|
|Bases|-|-|298758550|-|
|Md5sum|31f54a7d209ad3ff984287aa820bf192|55fd3a3e05cb5b85da77cf08b6aa7c13|95296a7a7ab948204ffbf99b27aa0d79|59f22947f3b171d9961b1dc398a2429e|
|BioSample|-|SAMEA27640168|SAMEA7528020|SAMN18612635|
|BioProject|PRJNA316098|PRJEB18650|PRJEB41116|-|
|ReplacedBy|-|-|-|-|


## NGSデータの処理
- 以前は .fastq　での配布が主流だったかもしれないが、今は .sra　での配布（な気がする）
- .sra　を処理するにはsra-toolkitが必要
```
# Ubuntuの場合
$ sudo apt install sra-toolkit
```

- 前はfastq-dumpだったのだが、最近はマルチスレッド化したfasterq-dumpを用いる
```
# ダウンロードと展開
$ fasterq-dump SRR6504026
# .sraを自力でダウンロードして展開だけやってもよい
$ fasterq-dump SRR650402.sra
```

## Taxonomy Analysis
- SRA Run Browser にTaxonomy Analysisなる、当該SRA runデータがどの生物種に対応しているかの階層構造＋割合の図が出る
- 例：https://trace.ncbi.nlm.nih.gov/Traces/?view=run_browser&acc=DRR514089&display=analysis
- https://www.ncbi.nlm.nih.gov/sra/docs/sra-taxonomy-analysis-tool/
- このあたりについて紹介したNAR DB issueの論文：https://academic.oup.com/nar/article/50/D1/D387/6438001
- やっている解析についての論文：https://pubmed.ncbi.nlm.nih.gov/34544477/
- SQLをたたいて、ある生物種が含まれるSRAデータを検索できるのだとか：https://qiita.com/satoshi_kawato/items/896771fa6fae5452940a
- SQLをたたいて、の部分の詳細仕様：https://www.ncbi.nlm.nih.gov/sra/docs/sra-cloud-based-taxonomy-analysis-table/
