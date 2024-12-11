# GTDB-Tk

## インストール
- まずはminiconda環境を整えること（+mambaも）
```
# gtdbtk仮想環境を作る
$ mamba create -n gtdbtk
$ mamba activate gtdbtk
(gtdbtk) $   ← 仮想環境の中
```
### 実際のインストール
```
(gtdbtk) $ mamba install -c bioconda gtdbtk    ← biocondaからパッケージを取ってくる
...
    GTDB-Tk v2.1.0 requires ~63G of external data which needs to be downloaded
    and extracted. This can be done automatically, or manually.

    Automatic:

        1. Run the command "download-db.sh" to automatically download and extract to:
            /home/tkr_nak/miniconda3/envs/gtdbtk/share/gtdbtk-2.1.0/db/

    Manual:

        1. Manually download the latest reference data:
            wget https://data.gtdb.ecogenomic.org/releases/release207/207.0/auxillary_files/gtdbtk_r207_v2_data.tar.gz

        2. Extract the archive to a target directory:
            tar -xvzf gtdbtk_r207_v2_data.tar.gz -c "/path/to/target/db" --strip 1 > /dev/null
            rm gtdbtk_r207_v2_data.tar.gz

        3. Set the GTDBTK_DATA_PATH environment variable by running:
            conda env config vars set GTDBTK_DATA_PATH="/path/to/target/db"
```
- 今回は、データを自分用のデータ置き場ディレクトリに格納したいのでManualで
```
$ wget https://data.gtdb.ecogenomic.org/releases/release207/207.0/auxillary_files/gtdbtk_r207_v2_data.tar.gz
$ mv gtdbtk_r207_v2_data.tar.gz /data/gtdbtk/
$ cd /data/gtdbtk/
$ tar xvzf gtdbtk_r207_v2_data.tar.gz --strip 1 > /dev/null  ← -c 入れたら怒られたので削った
```
```
/data/gtdbtk$ ls -alFh
合計 63G
drwxrwxr-x 13 tkr_nak tkr_nak 4.0K 12月 12 00:06 ./
drwxrwxrwx 12 root    root    4.0K 12月 10 23:34 ../
drwxrwxr-x  4 tkr_nak tkr_nak 4.0K  5月  9  2022 fastani/
-rw-rw-r--  1 tkr_nak tkr_nak  63G  5月 10  2022 gtdbtk_r207_v2_data.tar.gz
drwxrwxr-x  4 tkr_nak tkr_nak 4.0K  5月  9  2022 markers/
drwxrwxr-x  2 tkr_nak tkr_nak 4.0K  5月  9  2022 masks/
drwxrwxr-x  2 tkr_nak tkr_nak 4.0K  5月  9  2022 metadata/
drwxrwxr-x  2 tkr_nak tkr_nak 4.0K  5月  9  2022 mrca_red/
drwxrwxr-x  2 tkr_nak tkr_nak 4.0K  5月  9  2022 msa/
drwxrwxr-x  4 tkr_nak tkr_nak 4.0K  5月  9  2022 pplacer/
drwxrwxr-x  2 tkr_nak tkr_nak 4.0K  5月  9  2022 radii/
drwxrwxr-x  4 tkr_nak tkr_nak 4.0K  5月 10  2022 split/
drwxrwxr-x  2 tkr_nak tkr_nak 4.0K  5月  9  2022 taxonomy/
drwxrwxr-x  2 tkr_nak tkr_nak 4.0K  5月  9  2022 temp/
/data/gtdbtk$ du -sh *
62G     fastani
63G     gtdbtk_r207_v2_data.tar.gz
77M     markers
64K     masks
8.0K    metadata
4.8M    mrca_red
2.5G    msa
431M    pplacer
3.1M    radii
1.1G    split
18M     taxonomy
4.0K    temp
```
```
$ conda env config vars set GTDBTK_DATA_PATH="/dta/gtdbtk"
To make your changes take effect please reactivate your environment
(gtdbtk) $ mamba deactivate
$ mamba activate gtdbtk
(gtdbtk) $ 
```
