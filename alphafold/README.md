# AlphaFold
## インストール
### GPUまわりのセットアップ
- https://github.com/chalkless/misc/blob/main/doc/nvidiaSetup.md を見よ

### ソース等のダウンロード
- 場所が変わっている:https://github.com/deepmind/alphafold → https://github.com/google-deepmind/alphafold
- とはいえ、リダイレクトされるのであまり気にしなくて良さそう（2025年10月現在）
```
cd （alphafoldディレクトリを作る場所）
git clone https://github.com/deepmind/alphafold.git
cd ./alphafold
```

### インストール場所の確保（conda環境）
```
conda create -n alphafold python=3.11
conda activate alphafold
```
- docker/Dockerfile を見るに、Pythonのバージョンの3.11を要求しているようなので3.11で構築する

### ダウンロードツールaria2のインストール
- https://github.com/google-deepmind/alphafold を見ながら
- aria2を入れろ、とのこと（ダウンロードのプログラム）
```
conda install aria2
```
### データベース類のダウンロード
- https://qiita.com/Ag_smith/items/7c76438906b3f665af38 に詳しい
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
- この間に必要なモジュールとかのインストールができる

### 必要なモジュールのインストール
- `requrements.txt`に必要なモジュール類が書いてある
```
absl-py==1.0.0
biopython==1.79
dm-haiku==0.0.12
docker==5.0.0
jax==0.4.26
matplotlib==3.8.0
ml-collections==0.1.0
numpy==1.24.3
pytest<8.5.0
scipy==1.11.1
setuptools<72.0.0
tensorflow-cpu==2.16.1
```
- docker/Dockerfileの中を見るとpipで入れるように書いてあるので一応は従ってみる
```
pip3 install -r requirements.txt
```
- 本来、condaとpipは混ぜて使ってはいけないので注意
