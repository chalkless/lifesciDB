MeSHとTaxonomyをつないでみる

```
$ ./extOrgMesh.py d2023.bin > mesh2taxon.2023.tab
$ head mesh2taxon.2023.tab
D000011 Abelson murine leukemia virus   B04.613.807.375.525.020,B04.820.650.375.525.020 11788
D000045 Acacia  B01.875.800.575.912.250.401.025 3808
D000048 Acanthamoeba    B01.046.500.100.075.080 5754
D000049 Acanthocephala  B01.050.500.500.132     10232
...
```

```
$ /share/bin/bio/taxonomy.dmp2tab.pl rankedlineage.dmp > /work/230626_taxonomy/rankedlineage.tab
$ head -7 /work/230626_taxonomy/rankedlineage.tab
1       root
131567  cellular organisms
2157    Archaea
1935183 Asgard group                                                           Archaea
2798909 Candidatus Baldrarchaeota                                              Archaea
2798916 Candidatus Baldrarchaeia                                               Candidatus Baldrarchaeota                Archaea
2798922 Candidatus Baldrarchaeales                                      Candidatus Baldrarchaeia        Candidatus Baldrarchaeota               Archaea
```

```
$ python3 /share/bin/bio/merge.mesh2taxon.py -t ../230626_taxonomy/rankedlineage.tab -m mesh2taxon.2023.tab 
```
とりあえずやるとエラーが出る。→　Taxonomy IDが変更になったため。最近はウイルスも2名法に変わってなおのこと増えた。
ので、merge2taxon.pyを書き換えた

```
$ python3 /share/bin/bio/merge.mesh2taxon.py -m mesh2taxon.2023.tab -t ../230626_taxonomy/rankedlineage.tab -o ../230626_taxonomy/outdated.tab > /work/mesh2taxon/mesh2taxon.2023.arranged.tab
```
