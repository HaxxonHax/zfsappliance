#!/usr/bin/perl
use Data::Dumper;

require 'zfsappliance-lib.pl';
# Creates the HTML header from the lang/en file
ui_print_header(undef, $text{'index_title'}, "", undef, 1, 1);

# Read in all of the POST variables.
&ReadParse();

# get zpool
if (defined($in{'zpool'})) {
        $zpool = $in{'zpool'};
} else {
        &error("No zpool selected!");
        }

# Build links
@links = ( );
push(@links,&ui_link("create_zfs.cgi",$text{'index_zfs_create'}));
push(@links,&ui_link("destroy_zfs.cgi",$text{'index_zfs_destroy'}));
push(@links,&ui_link("modify_zfs.cgi",$text{'index_zfs_change'}));

# Function calls from the zfsappliance-lib.pl file
$conf = get_zfsappliance_config();
@zfsdatasets = get_zfs_dataset($zpool);

print ui_columns_start([ '', $text{'index_name'}, $text{'index_used'}, $text{'index_avail'}, $text{'index_refer'}, $text{'index_mountpoint'} ]);
foreach $u (@zfsdatasets) {
    print ui_checked_columns_row([
        "<a href='edit_zpool.cgi?share=$u->{'name'}'>$u->{'name'}</a>",
        $u->{'used'},
        $u->{'avail'},
        $u->{'refer'},
        $u->{'mountpoint'},
      ]);
    }
print ui_columns_end();
print &ui_links_row(\@links);

# Standard footer; link back to previous menu
&ui_print_footer("manage_zpools.cgi", $text{'index_return_zpool'});
