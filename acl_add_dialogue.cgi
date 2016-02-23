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


# Attributes
#     read_data (r)
#     list_directory (r)
#     write_data (w)
#     add_file (w)
#     append_data (p)
#     add_subdirectory (p)
#     read_xattr (R)
#     write_xattr (W)
#     execute (x)
#     read_attributes (a)
#     write_attributes (A)
#     delete (d)
#     delete_child (D)
#     read_acl (c)
#     write_acl (C)
#     write_owner (o)
#     synchronize (s) Currently, this permission is not supported.
#     full_set All permissions.
#     modify_set All permissions except write_acl and write_owner.
#     read_set read_data, read_acl, read_attributes, and read_xattr.
#     write_set write_data,    append_data,    write_attributes,     and write_xattr
# Inheritance
#     file_inherit (f) Inherit to all newly created files.
#     dir_inherit (d) Inherit to all newly created directories.
#     inherit_only (i) When placed on a directory, do not apply to  the  directory,  only to newly created files and directories. This flag  requires   that   either   file_inherit   and   or dir_inherit is also specified.
#     no_propagate (n) Indicates  that  ACL  entries  should  be  inherited  to objects  in  a  directory,  but  inheritance should stop after descending one level. This flag is dependent  upon either file_inherit and or dir_inherit also being specified.

print ui_columns_start([  
  $text{'text_read_data'},
  $text{'text_list_directory'},
  $text{'text_write_data'},
  $text{'text_add_file'}
]);
print ui_columns_row([
  $text{'text_append_data'},
  $text{'text_add_subdirectory'},
  $text{'text_read_xattr'},
  $text{'text_write_xattr'}
]);
print ui_columns_row([
  $text{'text_execute'},
  $text{'text_read_attributes'},
  $text{'text_write_attributes'},
  $text{'text_delete'}
]);
print ui_columns_row([
  $text{'text_delete_child'},
  $text{'text_read_acl'},
  $text{'text_write_acl'},
  $text{'text_write_owner'}
]);

print ui_columns_end();
#popup_window_link('add_file_attr.cgi, $text{'link_acl_add}, width, height, scrollbar, &field-mappings);
popup_window_link('add_file_attr.cgi', 'link_acl_add', 200, 200, 1);

# Standard footer; link back to previous menu
&ui_print_footer("", $text{'index_return'});

