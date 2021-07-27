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
- Synonymはnames.dmpにしか出てこないようだ（以下はtab変換されたファイルで処理している）
```
$ cut -f 4 names.tab| sort | uniq -c | sort -rn
2224096 scientificname
470951 authority
186520 synonym
50379 includes
29457 genbankcommonname
26646 equivalentname
14471 commonname
1164 acronym
1105 genbanksynonym
 534 in-part
 480 genbankacronym
 291 anamorph
 227 blastname
 169 teleomorph
```

### names.dmp の中身
```
tax_id                                  -- the id of node associated wit
name_txt                                -- name itself
unique name                             -- the unique variant of this na
name class                              -- (synonym, common name, ...)
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



