#!/usr/bin/env python3

# parse.biosample.py
# '23-11-23-Thu.    Ver.0.1    # parse.BioSample.py
# '26-04-15-Wed.    Ver.0.2
# Nakazato T.

import argparse
import xml.etree.ElementTree as ET

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', type=str)
args = parser.parse_args()

file_in = args.file

tree = ET.parse(file_in)
root = tree.getroot()

for biosample in root:

    id_bs = ""
    taxid = ""
    taxon_name = ""
    strain = ""
    owner_name = ""
    title = ""
    pubdate_tmp = ""

#    <BioSample last_update="2022-04-05T17:24:38.000+09:00" publication_date="2014-04-07T00:00:00.000+09:00" access="public">
    pubdate_tmp = biosample.get('publication_date')
    pubdate_match = re.match(r"\d{4}-\d{2}-\d{2}", pubdate_tmp)
    pubdate = pubdate_match.group()
#    print(pubdate)
    
    for ele1 in biosample:

        if ele1.tag == "Ids":

            for each_id in ele1:
                id_attrib = each_id.attrib
                
                if id_attrib.get('namespace'):    # for DDBJ
                    db = id_attrib.get('namespace')
                elif id_attrib.get('db'):        # for NCBI
                    db = id_attrib.get('db')
                    
                if db == "BioSample":
                    id_bs = each_id.text
#                    print(id_bs)
                elif db != None:
                    #print("[db]\t" + db)
                    None
                else:
#                    print("[OtherID]\t" + id_attrib)
                    None
                    
        elif ele1.tag == "Description":
            for each_desc in ele1:
                #print("[tag]\t" + each_desc.tag)
                #print("[attrib]\t" + str(each_desc.attrib))
                #print("[text]\t" + str(each_desc.text))

                desc_tag = each_desc.tag

                if desc_tag == "Title":
                    title = each_desc.text
                    #print(title)
                elif desc_tag == "Organism":
                    desc_org = each_desc.attrib
                    taxid = desc_org.get('taxonomy_id')
                    if taxid == None:
                        taxid = "0"
                    taxon_name = desc_org.get('taxonomy_name')
                    if taxon_name == None:
                        for each_taxon in each_desc:
                            if each_taxon.tag == "OrganismName":
                                taxon_name = each_taxon.text
                        
                    #print("\t".join([taxid, taxon_name]))
                elif desc_tag == "SampleName":
                    None
                elif desc_tag == "Comment":
                    None
                else:
                    #print("[Other_desc]\t" + desc_tag)
                    None
                    
        elif ele1.tag == "Owner":
            for each_owner in ele1:
                owner_tag = each_owner.tag

                if owner_tag == "Name":
                    owner_name = each_owner.text
        elif ele1.tag == "Models":
            for each_model in ele1:
                model_tag = each_model.tag

                if model_tag == "Model":
                    model = each_model.text
#                    print(model)
                else:
                   # print("[Oter_model]\t" + model_tag)
                    None
        elif ele1.tag == "Package":
            None
            
        elif ele1.tag == "Attributes":
            for each_attr in ele1:
                attr_value = str(each_attr.text)
#                print("[text]\t" + attr_value)

                attr = each_attr.attrib.get("attribute_name")
#                print("[attr]\t" + attr)

                if attr == "sample_name":
                    sample_name = attr_value
                elif attr == "strain":
                    strain = attr_value
                
        elif ele1.tag == "Status":
            status_attr = ele1.attrib
            status = status_attr.get('status')
            status_date = status_attr.get('when')
#            print("\t".join([status, status_date]))
    out = [id_bs, taxid, taxon_name, strain, pubdate, owner_name, title]
    print("\t".join([str(x) if x is not None else "" for x in out]))

    
