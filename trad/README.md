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
# lftp編
$ cd /data
$ lftp -e 'mirror -r --parallel=3 --delete --only-newer --verbose --include-glob "gbpri*" --include-glob "gbrod*" genbank/ ./; quit' ftp.ncbi.nlm.nih.gov
```
- FTPサイトのURLは`ftp.ncbi.nih.gov/genbank/`であるので、末尾にドメイン部分、ホスト側の設定を`genbank/`としている。最後の/を忘れないこと。忘れるとgenbankディレクトリが作られてコピーされる
- ローカル側もディレクトリ指定すると（つまり/で終わる形にすると）当該ディレクトリにファイルがコピーされる
- サブディレクトリも同期しようとするので -r　(--no-recursion) つける
- `--just-print` をつけると画面表示だけされる
- parallel で並列コピーされるし、経験的にこちらが段違いで早い
- PRI、ROD、MAM、VRT、INV、PLN、BCTで1.6TB程度（2025年9月現在）


```
# rsync編
$ cd /data/genbank
$ rsync -avz rsync://ftp.ncbi.nlm.nih.gov:/genbank/ ./ --include=gbbct100?.seq.gz --exclude=*

Warning Notice!

You are accessing a U.S. Government information system which includes this
computer, network, and all attached devices. This system is for
Government-authorized use only. Unauthorized use of this system may result in
disciplinary action and civil and criminal penalties. System users have no
expectation of privacy regarding any communications or data processed by this
system. At any time, the government may monitor, record, or seize any
communication or data transiting or stored on this information system.

-------------------------------------------------------------------------------

Welcome to the NCBI rsync server.


receiving incremental file list
gbbct1000.seq.gz
...
gbbct1009.seq.gz

sent 247 bytes  received 1,327,000,187 bytes  4,816,698.49 bytes/sec
total size is 1,326,446,303  speedup is 1.00
```
- include と exclude　の順番を変えないこと。前から解釈されるので、逆にすると何もダウンロードされない（if include=XXX then XXX; elsif exclude=XXX then XXX ...　という解釈だと思えば良い）
- rsync://のあたりはanonymousでつなぐことと思えば良い


## release noteのダウンロード

```
$ lftp -e 'mirror -r --parallel=3 --delete --only-newer --verbose genbank/release.notes/ ./; quit' ftp.ncbi.nlm.nih.gov
```
