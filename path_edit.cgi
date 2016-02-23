#!/usr/bin/perl
use Data::Dumper;

require 'zfsappliance-lib.pl';
# Creates the HTML header from the lang/en file
ui_print_header(undef, $text{'index_title'}, "", undef, 1, 1);

# Function calls from the zfsappliance-lib.pl file
$conf = get_zfsappliance_config();

# Get the POST data
&ReadParse();

# Ensure we weren't contacted without any parameters
if (defined($in{'path'})) {
        $path = $in{'path'};
} else {
        &error("No directory selected!");
}
if (defined($in{'chroot'})) {
        $chroot = $in{'chroot'};
} else {
        $chroot = '/';
}

@filelist = get_filelist($path);

# /usr/bin/svcs -H -o FMRI,STATE,NSTATE,STIME,DESC *dns*
# This is where the main output code goes.  Typical is an output table

# First, we get a list of all the files in the directory, with the attributes
# Then, we create a selection table so that we can edit the ACLs.

print ui_columns_start([ '', 
                         $text{'index_inode'},
                         $text{'index_perms'},
                         $text{'index_nfiles'},
                         $text{'index_owner'},
                         $text{'index_group'},
                         $text{'index_bytes'},
                         $text{'index_month'},
                         $text{'index_day'},
                         $text{'index_time'},
                         $text{'index_filename'} ]);
foreach $u (@filelist) {
    if ( $u->{'perms'} =~ m/^d/ && $u->{'filename'} !~ m/^\.\.$/ && $u->{'filename'} !~ m/^\.$/ ) {
      print ui_checked_columns_row([
          $u->{'inode'},
          $u->{'perms'},
          $u->{'nfiles'},
          $u->{'owner'},
          $u->{'group'},
          $u->{'bytes'},
          $u->{'month'},
          $u->{'day'},
          $u->{'time'},
          "<a href='path_edit.cgi?path=$path/$u->{'filename'}&chroot=$chroot'>$u->{'filename'}</a>"
        ]);
    } elsif ( $u->{'perms'} =~ m/^d/ && $u->{'filename'} =~ m/^\.\.$/ ) {
      my @str = split(/\/([^\/]+)$/, $path);
      my $oldpwd = $str[0];
      if ( $oldpwd == "" || $oldpwd == $chroot )
      {
        $oldpwd = $chroot;
      }
      print ui_columns_row([
          '',
          $u->{'inode'},
          $u->{'perms'},
          $u->{'nfiles'},
          $u->{'owner'},
          $u->{'group'},
          $u->{'bytes'},
          $u->{'month'},
          $u->{'day'},
          $u->{'time'},
          "<a href='path_edit.cgi?path=$oldpwd&chroot=$chroot'>$u->{'filename'}</a>"
        ]);
    } elsif ( $u->{'perms'} =~ m/^d/ && $u->{'filename'} =~ m/^\.$/ ) {
      my @str = split(/\/([^\/]+)$/, $path);
      my $oldpwd = $str[0];
      if ( $oldpwd == "" || $oldpwd == $chroot )
      {
        $oldpwd = $chroot;
      }
      print ui_columns_row([
          '',
          $u->{'inode'},
          $u->{'perms'},
          $u->{'nfiles'},
          $u->{'owner'},
          $u->{'group'},
          $u->{'bytes'},
          $u->{'month'},
          $u->{'day'},
          $u->{'time'},
          "<a href='path_edit.cgi?path=$oldpwd&chroot=$chroot'>$u->{'filename'}</a>"
        ]);
    } else {
      print ui_checked_columns_row([
          $u->{'inode'},
          $u->{'perms'},
          $u->{'nfiles'},
          $u->{'owner'},
          $u->{'group'},
          $u->{'bytes'},
          $u->{'month'},
          $u->{'day'},
          $u->{'time'},
          $u->{'filename'},
        ]);
      }
    }
print ui_columns_end();
#popup_window_link('add_file_attr.cgi, $text{'link_acl_add}, width, height, scrollbar, &field-mappings);
popup_window_link('add_file_attr.cgi', 'link_acl_add', 200, 200, 1);

# Standard footer; link back to previous menu
&ui_print_footer("", $text{'index_return'});

