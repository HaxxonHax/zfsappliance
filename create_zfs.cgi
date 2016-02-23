#!/usr/bin/perl
use Data::Dumper;

require 'zfsappliance-lib.pl';
# Creates the HTML header from the lang/en file
ui_print_header(undef, $text{'index_zpools_title'}, "", undef, 1, 1);

# Function calls from the zfsappliance-lib.pl file
$conf = get_zfsappliance_config();
#@disks = get_spare_disks();

do 'forms-lib.pl';
#$ntable = new Webmin::Table([ $text{'edit_zpoolname'},
#                             ]);

# This is where the main output code goes.  Typical is an output table

# Standard footer; link back to previous menu
&ui_print_footer("", $text{'index_return'});
