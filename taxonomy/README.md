# NCBI Taxonomy

## データの取得
- ftp://ftp.ncbi.nlm.nih.gov/pub/taxonomy/new_taxdump/new_taxdump.tar.gz を落として解凍する
- names.dmp と rankedlineage.dmp を使う
- nodes.dmpも?
- フォーマットが変態的

```
$ head -3 names.dmp                
1       |       all     |               |       synonym |
1       |       root    |               |       scientific name |
2       |       Bacteria        |       Bacteria <bacteria>     |       scientific name |
```
確認すると
```
$ head names.dmp| ruby -lane 'p $_'
"1\t|\tall\t|\t\t|\tsynonym\t|"
"1\t|\troot\t|\t\t|\tscientific name\t|"
"2\t|\tBacteria\t|\tBacteria <bacteria>\t|\tscientific name\t|"
```
| で区切られた上にデータの左右に \t 入れてスペースつくって見やすくしてるじゃねぇか。（メンドイ

普通のタブ区切りファイルにする

`./taxonomy.dmp2tab.pl names.dmp > names.tab`


## 名称 → TaxonID
- Scientific Name以外にSynonymがあってややこしい。
- Synonymはnames.dmpにしか出てこないようだ

```
$ grep "Bacillus endorhythmos" *.dmp
names.dmp:1396  |       Bacillus endorhythmos   |               |       synonym|
```

### names.dmp の中身
```
tax_id                                  -- the id of node associated wit
name_txt                                -- name itself
unique name                             -- the unique variant of this na
name class                              -- (synonym, common name, ...)
```

- unique name: Bacillus はbacteriaとナナフシで使われているので、どちらか、とか。

```
1386    Bacillus        Bacillus <firmicutes>   scientific name
55087   Bacillus        Bacillus <walking sticks>       scientific name
```

```
$ cut -f 4 names.tab | sort | uniq -c | sort -rn
2512652 scientific name
 675332 authority
 247536 synonym
  76045 includes
  57465 equivalent name
  30353 genbank common name
  14647 common name
   2082 acronym
    667 in-part
    230 blast name
     25 genbank acronym
```

### rankedlineage.dmp の中身
```
tax_id                                  -- node id
tax_name                                -- scientific name of the organism
species                                 -- name of a species (coincide with organism name for species-level nodes)
genus                                   -- genus name when available
family                                  -- family name when available
order                                   -- order name when available
class                                   -- class name when available
phylum                                  -- phylum name when available
kingdom                                 -- kingdom name when available
superkingdom                            -- superkingdom (domain) name when available
```
### nodes.dmp の中身
```
nodes.dmp
---------
This file represents taxonomy nodes. The description for each node includes 
the following fields:

        tax_id                                  -- node id in GenBank taxonomy database
        parent tax_id                           -- parent node id in GenBank taxonomy database
        rank                                    -- rank of this node (superkingdom, kingdom, ...) 
        embl code                               -- locus-name prefix; not unique
        division id                             -- see division.dmp file
        inherited div flag  (1 or 0)            -- 1 if node inherits division from parent
        genetic code id                         -- see gencode.dmp file
        inherited GC  flag  (1 or 0)            -- 1 if node inherits genetic code from parent
        mitochondrial genetic code id           -- see gencode.dmp file
        inherited MGC flag  (1 or 0)            -- 1 if node inherits mitochondrial gencode from parent
        GenBank hidden flag (1 or 0)            -- 1 if name is suppressed in GenBank entry lineage
        hidden subtree root flag (1 or 0)       -- 1 if this subtree has no sequence data yet
        comments                                -- free-text comments and citations
        plastid genetic code id                 -- see gencode.dmp file
        inherited PGC flag  (1 or 0)            -- 1 if node inherits plastid gencode from parent
        specified_species                       -- 1 if species in the node's lineage has formal name
        hydrogenosome genetic code id           -- see gencode.dmp file
        inherited HGC flag  (1 or 0)            -- 1 if node inherits hydrogenosome gencode from parent
```

### typematerial.dmp の中身
```
        tax_id                                  -- node id
        tax_name                                -- organism name type material is assigned to
        type                                    -- type material type (see typeoftype.dmp)
        identifier                              -- identifier in type material collection
```

```
$ cut -f 3 typematerial.tab | sort | uniq -c | sort -rn 
  87081 type strain
  34874 holotype
  16816 type material
  14423 culture from holotype
  12868 paratype
   3206 isotype
   2783 culture from type material
   1828 syntype
   1092 culture from epitype
   1071 lectotype
        ...
```


## 階層構造を得る
- 目、科、属など決まった階層に関してはrankedlineage.dmpに記載される
- 上のような決まった階層に挟まる階層も含めてについてはfullnamelineage.dmpに記載される

### fullnamelineage.dmpの中身
```
fullnamelineage.dmp
----------------
Full name lineage file fields:

        tax_id                                  -- node id
        tax_name                                -- scientific name of the organism
        lineage                                 -- sequence of sncestor names separated by semicolon ';' denoting nodes' ancestors starting from the most distant one and ending with the immediate one
```




