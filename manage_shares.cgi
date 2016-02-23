#!/usr/bin/perl
use Data::Dumper;

require 'zfsappliance-lib.pl';
# Creates the HTML header from the lang/en file
ui_print_header(undef, $text{'index_title'}, "", undef, 1, 1);

# Function calls from the zfsappliance-lib.pl file
$conf = get_zfsappliance_config();
@shares = get_shares();

# /usr/bin/svcs -H -o FMRI,STATE,NSTATE,STIME,DESC *dns*
# This is where the main output code goes.  Typical is an output table
print ui_columns_start([ '', $text{'index_name'}, $text{'index_path'}, $text{'index_protocol'}, $text{'index_params'}, $text{'index_description'} ]);
foreach $u (@shares) {
    print ui_checked_columns_row([
        "<a href='share_edit.cgi?share=$u->{'name'}'>$u->{'name'}</a>",
        "<a href='path_edit.cgi?path=$u->{'path'}&chroot=$u->{'path'}'>$u->{'path'}",
        $u->{'protocol'},
        $u->{'params'},
        $u->{'desc'},
      ]);
    }
print ui_columns_end();

# Print out string using webmin's 'text' function from Webmin API
print &text('index_root', "/"), "<p>\n";

# Standard footer; link back to previous menu
&ui_print_footer("", $text{'index_return'});

