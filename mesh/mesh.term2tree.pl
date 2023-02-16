#!/usr/bin/perl

# mesh.term2tree.pl
# Nakazato T.
# '23-02-16-Thu.    Ver. 0.1

$debug = 1;

my ($file_in) = shift @ARGV;        # dYYYY.bin
open(IN, $file_in) or die $!;
while (defined ($line_in = <IN>)) {
    $line_in =~ s/[\r\n]//;

    if ($line_in =~ /^MH = (.*)/) {
	$mterm = $1;
    }
    elsif ($line_in =~ /^MN = (.*)/) {
	push @tree, $1;
    }
    elsif ($line_in =~ /^UI = (.*)/) {
	$mid = $1;

	$treeid = join("|", @tree);
	undef @tree;
	
	print join("\t", $mid, $mterm, $treeid)."\n";
    }
}
close($file_in);




