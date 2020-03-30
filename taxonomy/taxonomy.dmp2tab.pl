#!/usr/bin/perl

# taxonomy.dmp2tab.pl
# '20-03-30-Mon.    Ver. 0
# Nakazato T.

$debug = 1;

# NCBI taxonomy のデータ（names.dmp, rankedlineage.dmp など）をタブ区切りに変換
# 元ファイルは | で区切られている上にデータがタブで囲まれている（謎）
# $ head names.dmp | ruby -lane 'p $_'
# "1\t|\tall\t|\t\t|\tsynonym\t|"
# "1\t|\troot\t|\t\t|\tscientific name\t|"
# "2\t|\tBacteria\t|\tBacteria <bacteria>\t|\tscientific name\t|"

$file_in = shift @ARGV;

open (IN, $file_in) or die $!;
while (defined ($line_in = <IN>)) {
    $line_in =~ s/[\r\n]//g;

    @ele = split(/\|/, $line_in);

    @out = map { $_ =~ s/^[\t\s]*(.*)/$1/g;
		 $_ =~ s/([^\s\t]*)[\t\s]*/$1/g;
		 $_ } @ele;
    print join("\t", @out)."\n";
}
close(IN);
