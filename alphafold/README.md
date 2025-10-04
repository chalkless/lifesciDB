# AlphaFold
## インストール
### GPUまわりのセットアップ
- https://github.com/chalkless/misc/blob/main/doc/nvidiaSetup.md を見よ
### インストール場所の確保（conda環境）
```
conda create -n alphafold
conda activate alphafold
```
### ソース等のダウンロード
- 場所が変わっている:https://github.com/deepmind/alphafold → https://github.com/google-deepmind/alphafold
- とはいえ、リダイレクトされるのであまり気にしなくて良さそう（2025年10月現在）
```
cd （alphafoldディレクトリを作る場所）
git clone https://github.com/deepmind/alphafold.git
cd ./alphafold
```
- https://github.com/google-deepmind/alphafold を見ながら
- aria2を入れろ、とのこと（ダウンロードのプログラム）
```
conda install aria2
```
### データベース類のダウンロード
- `scripts/download_all_data.sh`を実行する。
```
scripts/download_all_data.sh <DOWNLOAD_DIR>
```
- が、中身を見ると`scripts/download_xxx_sh`をダウンロードするだけになっている。
- 元のスクリプトは順番にダウンロードするようになっているが、自分で中身を見てダウンロードを並列でやった方が早い。
- https://github.com/google-deepmind/alphafold?tab=readme-ov-file#genetic-databases を見るにダウンロードするサイズは556 GBで展開すると2.62 TB。SSDにダウンロードすることが推奨。
- `reduced_dbs`をつけることで容量の削減は可能。
```
scripts/download_all_data.sh <DOWNLOAD_DIR> reduced_dbs
```
- 


