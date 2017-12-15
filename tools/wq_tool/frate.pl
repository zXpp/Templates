#!/usr/bin/perl
# ===========================================================================
# CONFUSION MATRIX COMPUTATION BASED ON FRAME RATES
# ===========================================================================
# (c) 2004, Thomas Hain

# commanbd line 
while ( @ARGV > 0 ) {
    if ( $ARGV[0] eq "-tgt" ) {
        push @TARGETS, $ARGV[1];
        shift @ARGV;
    }
    elsif ( $ARGV[0] eq "-o" ) {
        $OUTPUTMLF = $ARGV[1];
        shift @ARGV;
    }
    else {
        last;
    }
    shift @ARGV;
}

if ( @ARGV != 2 ) {
    print "usage: $0 [OPTIONS] <REF> <TST>\n";
      exit(1);
}

( $ref , $tst ) = @ARGV;

# --------------------------------
open(IN,$ref);
while (<IN>) {
    chop;
    next if (m/#!MLF!#/);
    if ( m/\"(.*)[.]lab\"/) {
        @p = split(/\//,$1);
        $seg = ( $p[0] eq "*" ) ? $p[$#p] : $1 ;
    }
    elsif (m/^.$/) {
    }
    else {
        @p = split;
        push @{$SEGS{$seg}} , [  @p[0..2] , ""  ];
        $REFSYMB{$p[2]}++;
    }
}
close(IN);

# --------------------------------
open(IN,$tst);
while (<IN>) {
    chop;
    next if (m/#!MLF!#/);
    if ( m/\"(.*)[.]rec\"/ || m/\"(.*)[.]lab\"/) {
        @p = split(/\//,$1);
        $seg = ( $p[0] eq "*" ) ? $p[$#p] : $1 ;

        die "no ref" if (!defined($SEGS{$seg}));

        $curseg = $SEGS{$seg};
        $idx = 0;

#	print "$seg\n";
    }
    elsif (m/^.$/) {
        $curseg = 0;
    }
    else {
        die "???" if ($curseg == 0);

        @p = split;
        $TSTSYMB{$p[2]}++;

        while ( $idx < @{$curseg} ) {

#            print "@p ======= ($idx/" . @{$curseg} . ") @{$curseg->[$idx]}\n";

            # check we are overlapping
           # die "???: $p[0] != $curseg->[$idx]->[0] " if ( $p[0] != $curseg->[$idx]->[0] );
           # next if ( $p[0] > $curseg->[$idx]->[1] );

            # the starts have to be ident !
            if ( $p[1] > $curseg->[$idx]->[1] ) { # seg longer than ref
                $curseg->[$idx]->[3] = $p[2];
                $p[0] = $curseg->[$idx]->[1];
            }
            elsif ( $p[1] == $curseg->[$idx]->[1] ) {
                $curseg->[$idx]->[3] = $p[2];
                $idx++;
                last;
            }
            else { # seg shorter than ref
                splice @{$curseg},$idx,0, [ $p[0] , $p[1] , $curseg->[$idx]->[2] , $p[2] ];
                $idx++;
                # the current seg remains
                $curseg->[$idx]->[0] = $p[1];
                last; 
            }
            $idx++;
        }
    }
}
close(IN);
ConfusionMatrix();

if ( defined($OUTPUTMLF) ) {
    PrintMLF( $OUTPUTMLF );
}

sub ConfusionMatrix
{
    $FMTPERC = "%8.2f";

    # collect
    foreach $seg ( keys %SEGS ) {
        foreach $s ( @{$SEGS{$seg}} ) {
            $d = $s->[1] - $s->[0];
            $CONF{$s->[2]}{$s->[3]} += $d;
            $RLEN{$s->[2]} += $d;
            $TLEN +=$d;
        }
    }
    # print
    @TKEYS = sort keys %TSTSYMB;

    printf("CONFUSION MATRIX\n");
    printf("%-15s   ","TEST --->");
    foreach $t ( @TKEYS ){
        printf("%8s ",$t);
    }
    $totalCF = 0;         ######## SA:Check total of the whole confusion matrix
    print "\n" . "-" x (@TKEYS * 9 + 18) . "\n";
    foreach $r ( sort keys %CONF ) {
        printf("%-15s : ",$r);
        foreach $t ( @TKEYS ){
            printf($FMTPERC . " ",  100 * $CONF{$r}{$t} / $TLEN );
            $totalCF += 100 * $CONF{$r}{$t} / $TLEN;  ######## SA:Check total of the whole confusion matrix
        }
        print "\n";
    }

  
    print "-" x (@TKEYS * 9 + 18) . "\n";
    printf ("Total of confusion matrix : " . $FMTPERC . "\n",  $totalCF ); ######## SA:Check total of the whole confusion matrix
	
    # ===========================================================================
    # PERCENT CORRECT
    # ===========================================================================
    $CORR=0;
    foreach $t ( @TKEYS ){
        $CORR += $CONF{$t}{$t};
    }
    printf("%-15s : " . $FMTPERC . "\n","%CORRECT", 100 * $CORR / $TLEN );

    # ===========================================================================
    # FALSE ALARN AND FALSE REJECT
    # ===========================================================================
    if ( @TARGETS > 0 ) {

        # FALSE REJECT :          REF = tgt  && TST != tgt     / REF = tgt
        $fr = 0; $frden = 0;
        foreach $r ( @TARGETS ) {
            $frden += $RLEN{$r};
            foreach $t ( @TKEYS ) {
                if (! ($r eq $t)) {
                    $fr += $CONF{$r}{$t};
                }
            }
        }

        # FALSE ALArM :           REF != tgt && TST = tgt      / REF != tgt
        $fa = 0 ;
        foreach $r ( keys %REFSYMB ) {
            $found=0;
            foreach $t ( @TARGETS ) {
                $found = 1 if ($r eq $t);
            }
            next if $found;
            foreach $t ( @TARGETS ) {
                $fa += $CONF{$r}{$t};
            }
        }
        $faden = $TLEN - $frden;
        printf("%-15s : " . $FMTPERC . "\n","%FALSE ALARM", 100 * $fa / $faden );
        printf("%-15s : " . $FMTPERC . "\n","%FALSE REJECT", 100 * $fr / $frden )    
    }

    # ===========================================================================
    # CONF MATRIX NORMALISED BY REFERENCE DURATION
    # ===========================================================================
    printf("\nNORMALISATION BY REFERENCE\n");
    printf("%-15s   ","TEST --->");
    foreach $t ( @TKEYS ){
        printf("%8s ",$t);
    }
    print "\n" . "-" x (@TKEYS * 9 + 18) . "\n";
    foreach $r ( sort keys %CONF ) {
        printf("%-15s : ",$r);
        foreach $t ( @TKEYS ){
            printf($FMTPERC . " ", 100 * $CONF{$r}{$t} / $RLEN{$r} );
        }
        print "\n";
    }
    print "-" x (@TKEYS * 9 + 18) . "\n";
}

sub PrintMLF{
    my ( $file ) = @_;

    open(OUT,">$file");
    print OUT "#!MLF!#\n";
    foreach $seg ( keys %SEGS ) {
        print OUT "\"$seg.lab\"\n";
        foreach $s ( @{$SEGS{$seg}} ) {
            print OUT "@{$s}\n";
        }
        print OUT ".\n";
    }
    close(OUT);
}
