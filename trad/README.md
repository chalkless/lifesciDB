# trad.: GenBank/EMBL/DDBJ

trad. (traditional)とは、歴々 収集されてきた塩基配列・アミノ酸配列のことで、ようするにGenBank/EMBL/DDBJのこと（NucleotideとかProteinとか）

- GenBank FTP site: https://ftp.ncbi.nlm.nih.gov/genbank/


## INSDCでの生物種カテゴリ(Division)
- See https://www.ncbi.nlm.nih.gov/genbank/samplerecord/#GenBankDivisionB

| Category | Description |
|---|---|
| PRI | primate sequences |
| ROD | rodent sequences |
| MAM | other mammalian sequences |
| VRT | other vertebrate sequences |
| INV | invertebrate sequences |
| PLN | plant, fungal, and algal sequences |
| BCT | bacterial sequences |
| VRL | viral sequences |
| PHG | bacteriophage sequences |
| SYN | synthetic sequences |
| UNA | unannotated sequences |
| EST | EST sequences (expressed sequence tags) |
| PAT | patent sequences |
| STS | STS sequences (sequence tagged sites) |
| GSS | GSS sequences (genome survey sequences) |
| HTG | HTG sequences (high-throughput genomic sequences) |
| HTC | unfinished high-throughput cDNA sequencing |
| ENV | environmental sampling sequences |

## データの一括ダウンロード
```
$ cd /data
$ lftp -e 'mirror -r --parallel=3 --delete --only-newer --verbose --include-glob "gbpri*" --include-glob "gbrod*" genbank ./genbank; quit' ftp.ncbi.nlm.nih.gov
```
- リモートとローカルが同じ名前でかつ/で終わらない時だけ中身がコピーされ、他はgenbankディレクトリができてその中にコピーされるので、1つ上に移動してlftpをかけている（ローカル側が/で終わらない時は中身がコピーされる）
- サブディレクトリも同期しようとするので -r　(--no-recursion) つける
- `--just-print` をつけると画面表示だけされる






