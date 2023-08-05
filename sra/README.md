# SRA (Sequence Read Archive)
- https://ftp.ncbi.nlm.nih.gov/sra/reports/Metadata/SRA_Accessions.tab
- 2023/7/20現在：19GB
- wget するとなかなかに時間がかかる（そして途中で切れてやり直す。続きからではあるが）
- lftpかrsyncか。。。

```
$ lftp -e 'get /sra/reports/Metadata/SRA_Accessions.tab' ftp.ncbi.nlm.nih.gov
```


|Label|Study|Experiment|Run|Sample|
|-|-|-|-|-|-|
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
