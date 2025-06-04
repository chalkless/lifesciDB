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


