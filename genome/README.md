# NCBI Genome
- これまであったNCBI Genome　https://www.ncbi.nlm.nih.gov/genome は終了。NCBI Assemblyと一緒になってNCBI Datasets　のゲノムセクション https://www.ncbi.nlm.nih.gov/datasets/genome/ に移行した(２０２４年６月)。

# 昆虫ゲノムで目ごとにゲノムサイズを可視化してみる

## NCBI　Genomeからゲノムサイズデータをダウンロード
- [NCBI - Genome Information by Organism](https://ncbi.nlm.nih.gov/genome/browse#!/overview/)ページでFilterからAnimal　>　Insects　と絞り込み、Downloadボタンからデータをダウンロードする。（2,266 entries as of 23/07/05）
- genomes.insect.230705.csv として保存
- CSVからタブ区切りに変換
```
$ python3 csv2tab.py genomes.insect.230705.csv
```
- joinするためにsortしておく
```
$ sort genomes.insect.230705.tab > genomes.insect.sorted.230705.tab
```

## NCBI　Taxonomyデータの加工
- 目・科・属などのデータはrankedlineage.dmpに書かれている。
- .dmpから.tabに変換（.dmpは区切り文字が | な上に余計なスペース（タブ）が入っている）
```
$ taxonomy.dmp2tab.pl rankedlineage.dmp > rankedlineage.tab
```
- 昆虫データだけに絞り込んで、名前をアルファベット順にsort
```
$ perl -F"\t" -lane 'print $_ if $F[6] eq "Insecta"' rankedlineage.tab | sort -k 2 > rankedlineage.insecta.sorted.tab
```
- 不確定な名前は ' ' で囲われていることに注意

## ゲノムデータとTaxonomyデータのガッチャンコ
```
$ join -1 1 -2 2 -a 1 -t "  " -o 2.1,1.1,2.3,2.4,2.5,2.6,2.7,1.3 genomes.insect.sorted.230705.tab /data/taxonomy/230626/rankedlineage.insecta.sorted.tab > genomes.insect.arranged.230705.tab
```
```
$ cut -f 6 genomes.insect.arranged.230705.tab | sort | uniq -c | sort -rn | head
   1064 Lepidoptera
    438 Diptera
    338 Hymenoptera
    169 Coleoptera
     88 Hemiptera
     54
     35 Trichoptera
     15 Orthoptera
     13 Phasmatodea
      9 Plecoptera
```
- 54行分が分類群がアサインされてない
```
$ perl -F"\t" -lane 'print $_ if $F[5] eq ""' genomes.insect.arranged.230705.tab | sort > genomes.insect.nonassigned.230705.tab
$ join -j 2 -t "    " -o 2.7 genomes.insect.nonassigned.230705.tab /data/taxonomy/230626/rankedlineage.sorted.tab | sort | uniq -c | sort -rn
     50 Collembola     # トビムシ目
      3
```
- 空白の3行は
```
$ join -j 2 -t "    " -o 2.2,2.7 genomes.insect.nonassigned.230705.tab /data/taxonomy/230626/rankedlineage.sorted.tab | perl -F"\t" -lane 'print $_ if $F[1] eq ""'
Campodea augens
Catajapyx aquilonaris
unclassified Hexapoda
$ grep "Campodea augens" rankedlineage.tab 
438502  Campodea augens         Campodea        Campodeidae     Diplura        Arthropoda       Metazoa Eukaryota
2065805 Campodea augens associated virus 1                                     Viruses
chalkless@blenny:/data/taxonomy/230626$ grep "Catajapyx aquilonaris" rankedlineage.tab
438503  Catajapyx aquilonaris           Catajapyx       Japygidae       DipluraArthropoda       Metazoa Eukaryota
```
- Diplura = コムシ目
- ということで、空白のものは無視して良さそうなので元ファイルから削っておく
```
$ perl -F"\t" -lane 'print $_ if $F[5] ne ""' genomes.insect.arranged.230705.tab > genomes.insect.for_graph.230705.tab
```

## 可視化
- Google Colabで
https://github.com/chalkless/lifesciDB/blob/master/genome/insect_genome.ipynb
