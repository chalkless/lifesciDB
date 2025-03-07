#!/usr/bin/perl

# restrict.mesh.pl
# Nakazato T.
# '23-02-16-Thu.    Ver. 0.1
# '25-03-07-Fri.    Ver. 0.11

use Getopt::Long 'GetOptions';

$debug = 1;

GetOptions(
    'field_column=s' => \$column,      # column number
    'category=s'     => \$category,
    'table_index=s'  => \$file_idx,
    'in=s'           => \$file_target
    );

open(IDX, $file_idx) or die $!;
while( defined( $line_idx = <IDX> )) {
    $line_idx =~ s/[\r\n]//g;

    my ($mid, $mterm, $mtree) = split(/\t/, $line_idx);

    $m_term2tree{lc($mterm)} = $mtree;
}
close(IDX);

open(IN, $file_target) or die $!;
while (defined ($line_in = <IN>)) {
    $line_in =~ s/[\r\n]//;

    @ele = split(/\t/, $line_in);

    $mterm_tgt = $ele[$column];
    $mtree_tgt = $m_term2tree{lc($mterm_tgt)};

    print $line_in."\n" if ($mtree_tgt =~ /$category/);
}
