#!/usr/bin/perl
#

if ( @ARGV != 3 )
{
    print "usage: $0 <infile> <dimension> <outfile>\n";
    exit(0);
}

( $infile , $ndim, $outfile ) = @ARGV;


open(IN,$infile);
open(OUT,">$outfile");

while ($data=<IN>)
{
    chomp($data);
    print OUT "$data\n";
    if($data=~/\<sigmoid\> 13 13/)
    {
       print "**$data**\n";
       last;
    }
}
close(IN);
close(OUT);

