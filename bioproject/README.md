# BioProject
## データの入手先
### DDBJから
```
https://ddbj.nig.ac.jp/public/ddbj_database/bioproject/
 	bioproject.xml	2026-04-12 18:21	3.6G
 	ddbj_core_bioproject.xml	2026-04-13 02:00	33M
 	ddbj_summary.txt	2026-04-13 02:00	1.9M
 	schema/	2015-10-14 09:39	-
```

- これもDDBJとNCBIで形式が違ったりするような予感もする（未確認）

## データの一例
```
        <Package>
                <Project>
                        <Project>
                                <ProjectID>
                                        <ArchiveID accession="PRJDB503" archive="DDBJ" />
                                </ProjectID>
                                <ProjectDescr>
                                        <Title>Genome projects for evolutional studies of the family Acetobacteraceae</Title>
                                        <Description>We are pursuing a research project to comprehend the evolutional status of the family Acetobacteraceae based on genome analyses.  First 18 bacterial genomes were projected to read the genome DNA sequences.  We will provide data of more bacterial genome and moreover transcriptome by mRNA sequencing.</Description>
                                        <Grant GrantId="">
                                                <Title>Industrial utilization and molecular comprehension of the thermo-tolerance of thermostable fermentation microbes</Title>
                                                <Agency abbr="PROBRAIN">he Program for Promotion of Basic Research Activities for Innovative Biosciences</Agency>
                                        </Grant>
                                        <Grant GrantId="2251022">
                                                <Title>Applied studies for biomass utilization based on genome analyses of acetic acid bacteria exhibiting specific metabolic traits.</Title>
                                                <Agency abbr="KAKEN-HI">Scientific Research from the Ministry of Education, Culture, Sports, Science and Technology of Japan</Agency>
                                        </Grant>
                                        <Grant GrantId="">
                                                <Title>Fermentational approaches for low CO2 exhausting from genome engineering and evolutional adaptation of thermo-tolerant microbes.</Title>
                                                <Agency abbr="ALCA">Advanced Low Carbon Technology Research and Development Program  Abbreviation :   ALCA</Agency>
                                        </Grant>
                                        <ProjectReleaseDate>2012-09-10T18:17:52.600+09:00</ProjectReleaseDate>
                                </ProjectDescr>
                                <ProjectType>
                                        <ProjectTypeTopAdmin subtype="eOther">
                                                <Organism taxID="433">
                                                        <OrganismName>Acetobacteraceae</OrganismName>
                                                </Organism>
                                        </ProjectTypeTopAdmin>
                                </ProjectType>
                        </Project>
                </Project>
        </Package>
```

