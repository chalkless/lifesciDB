# GTDB-tk

## インストール
- まずはminiconda環境を整えること（+mambaも）
```
# gtdbtk仮想環境を作る
$ mamba create -n gtdbtk
$ mamba activate gtdbtk
(gtdbtk) $   ← 仮想環境の中
```
- 実際のインストール
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
