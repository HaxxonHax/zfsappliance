#!/usr/bin/perl
use Data::Dumper;

require 'zfsappliance-lib.pl';
# Creates the HTML header from the lang/en file
ui_print_header(undef, $text{'index_zpools_title'}, "", undef, 1, 1);

# Function calls from the zfsappliance-lib.pl file
$conf = get_zfsappliance_config();
@zfspools = get_zfs_pools();
#@zfsdatasets = get_zfs_datasets();

# Build links
@links = ( );
push(@links,&ui_link("create_zpool.cgi",$text{'index_zpool_create'}));
push(@links,&ui_link("modify_zpool.cgi",$text{'index_zpool_change'}));
push(@links,&ui_link("mirror_zpool.cgi",$text{'index_zpool_mirror'}));
push(@links,&ui_link("destroy_zpool.cgi",$text{'index_zpool_destroy'}));

# This is where the main output code goes.  Typical is an output table
print ui_columns_start([ '', $text{'index_pool'}, $text{'index_size'}, $text{'index_alloc'}, $text{'index_free'}, $text{'index_dedup'}, $text{'index_health'}, $text{'index_altroot'} ]);
foreach $u (@zfspools) {
    print ui_checked_columns_row([
        "<a href='edit_zpool.cgi?zpool=$u->{'pool'}'>$u->{'pool'}</a>",
        $u->{'size'},
        $u->{'alloc'},
        $u->{'free'},
        $u->{'dedup'},
        $u->{'health'},
        $u->{'altroot'},
      ]);
    }
print ui_columns_end();
print &ui_links_row(\@links);

# Standard footer; link back to previous menu
&ui_print_footer("", $text{'index_return'});
