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
