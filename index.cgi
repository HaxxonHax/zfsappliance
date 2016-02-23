#!/usr/bin/perl
use Data::Dumper;

require 'zfsappliance-lib.pl';
# Creates the HTML header from the lang/en file
ui_print_header(undef, $text{'index_title'}, "", undef, 1, 1);

# Function calls from the zfsappliance-lib.pl file
$conf = get_zfsappliance_config();
@shares = get_shares();
#$dir = find($conf, "root");

# /usr/bin/svcs -H -o FMRI,STATE,NSTATE,STIME,DESC *dns*
# This is where the main output code goes.  Typical is an output table
@icons =  ( "images/storage.gif", "images/shares.gif",
            "images/naming.gif" );
@titles = ( $text{'storage_title'}, $text{'shares_title'},
            $text{'naming_title'} );
@links =  ( "manage_zpools.cgi", "manage_shares.cgi",
            "manage_naming.cgi" );
&icons_table(\@links, \@titles, \@icons, 5);

# Standard footer; link back to previous menu
ui_print_footer("/", $text{'index'});
