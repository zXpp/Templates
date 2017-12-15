#!/usr/bin/perl

$n = 0 ;
$s = 0;
$t = 0.0 ;
while (<>) {
   next if m/^;;/ ;
   chop;
   @p = split; 
   next if ( $p[2] =~ m/inter_segment_gap/ );

   $n++;
   $s +=  @p - 6 ;
   $t += $p[4] - $p[3];
}

printf("%d words %d segs %.2f hours => %.2f word per seg %.2f word per sec  \n" , $s , $n ,  $t/3600.0  , $s/$n , $s/$t );
