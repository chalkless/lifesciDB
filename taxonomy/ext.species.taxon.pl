#!/usr/bin/perl

# ext.species.taxon.pl
# Nakazato T.
# '20-08-12-Thu.    Ver. 0.1

$debug = 1;

$file_node = "nodes.tab";
$file_taxon = shift @ARGV;

open (NODE, $file_node) or die $!;
while (defined ($line_node = <NODE>)) {
    $line_node =~ s/[\r\n]//g;

    my @ele = split(/\t/, $line_node);
    my $tax_id = $ele[0];
    my $rank   = $ele[2];

    $taxid2rank{$tax_id} = $rank;
}
close (NODE);

open (TAXON, $file_taxon) or die $!;
while (defined ($line_taxon = <TAXON>)) {
    $line_taxon =~ s/[\r\n]//;

    my @ele = split(/\t/, $line_taxon);
    my $tax_id = $ele[0];
    my $name   = $ele[1];
    my $rank   = $taxid2rank{$tax_id};

    print join("\t", $tax_id, $rank, $name)."\n";
}
close (TAXON);




