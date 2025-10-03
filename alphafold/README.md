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
- aria2を入れろ、とのこと
```
conda install aria2
```
