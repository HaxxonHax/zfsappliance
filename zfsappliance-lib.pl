=head1 zfsappliance-lib.pl
 
Functions for managing the ZfsAppliance Webmin configuration file.
 
  foreign_require("zfsappliance", "zfsappliance-lib.pl");
  @sites = zfsappliance::list_zfsappliance_websites()
 
=cut

BEGIN { push(@INC, ".."); };
use WebminCore;
use POSIX qw(strftime);
init_config();
foreign_require("mount", "mount-lib.pl");

=head2 get_zfsappliance_config()

Returns the ZfsAppliance Webmin configuration as a list of hash references with name and value keys.

=cut
sub get_zfsappliance_config
{
  my $lref = &read_file_lines($config{'zfsappliance_conf'});
  my @rv;
  my $lnum = 0;
  foreach my $line (@$lref) {
    my ($n, $v) = split(/\s+/, $line, 2);
    if ($n)
    {
      push(@rv, { 'name' => $n, 'value' => $v, 'line' => $lnum });
    }
    $lnum++;
  }
  return @rv;
}

=head2 get_shares()

Returns the ZFS Shares as a list of hash references with name and value keys.

=cut
sub get_shares
{
  my @sharelist;

  my @shareoutput = `/usr/sbin/share`;
  foreach my $line (@shareoutput) {
    my ($name, $path, $prot, $params, $desc) = split(/\t/,$line, 5);
    if ($name)
    {
      push(@sharelist, { 'name' => $name, 'path' => $path, 'protocol' => $prot, 'params' => $params, 'desc' => $desc });
    }
  }
  return @sharelist;
}

=head2 get_share_params()

Returns the ZFS Share Parameters as a list of hash references with name and value keys.

=cut
sub get_share_params
{
  my @paramlist;

  my @shareoutput = `/usr/sbin/share`;
  foreach my $line (@shareoutput) {
    my ($name, $path, $prot, $params, $desc) = split(/\t/,$line, 5);
    if ($name)
    {
      push(@paramlist, { 'name' => $name, 'path' => $path, 'protocol' => $prot, 'params' => $params, 'desc' => $desc });
    }
  }
  return @paramlist;
}

=head2 get_zfs_pools()

Returns the ZFS Pools as a list of hash references with name and value keys.

=cut
sub get_zfs_pools
{
  my @paramlist;
  my $capture = 0;

  my @zpool = `/usr/sbin/zpool list -H`;
  foreach my $line (@zpool) {
    my ($pool, $size, $alloc, $free, $cap, $dedup, $health, $altroot) = split(/\s+/,$line, 8);
    if ($pool)
    {
      push(@paramlist, { 'pool' => $pool, 'size' => $size, 'alloc' => $alloc, 'free' => $free, 'dedup' => $dedup, 'health' => $health, 'altroot' => $altroot });
    }
  }
  return @paramlist;
}

=head2 get_zfs_datasets()

Returns the ZFS Datasets as a list of hash references with name and value keys.

=cut
sub get_zfs_dataset
{
  my @paramlist;
  my @args = @_;

  my @zfsoutput = `/usr/sbin/zfs list -Hr $args[0]`;
  foreach my $line (@zfsoutput) {
    my ($name, $used, $avail, $refer, $mountpoint) = split(/\t/,$line, 5);
    if ($name)
    {
      push(@paramlist, { 'name' => $name, 'used' => $used, 'avail' => $avail, 'refer' => $refer, 'mountpoint' => $mountpoint });
    }
  }
  return @paramlist;
}


=head2 get_filelist(directory)

Returns the File Listing of a directory as a list of hash references with name and value keys.

=cut
sub get_filelist
{
  my @paramlist;
  my @args = @_;

  my @lsoutput = `/usr/bin/ls -ail $args[0]`;

  foreach my $line (@lsoutput) {
    my ($whitespace, $inode, $perms, $nfiles, $owner, $group, $bytes, $month, $day, $time, $filename) = split(/\s+/,$line, 11);
    if ($filename)
    {
      push(@paramlist, { 'inode' => $inode,
                         'perms' => $perms,
                         'nfiles' => $nfiles,
                         'owner' => $owner,
                         'group' => $group,
                         'bytes' => $bytes,
                         'month' => $month,
                         'day' => $day,
                         'time' => $time,
                         'filename' => $filename
                        });
    }
  }
  return @paramlist;
}

# nfs_export_chooser_button(serverinput, exportinput, [form])
sub nfs_export_chooser_button
{
local($form);
$form = @_ > 2 ? $_[2] : 0;
if ($access{'browse'}) {
        return "<input type=button onClick='if (document.forms[$form].$_[0].value != \"\") { ifield = document.forms[$form].$_[1]; nfs_export = window.open(\"../$module_name/nfs_export.cgi?server=\"+document.forms[$form].$_[0].value, \"nfs_export\", \"toolbar=no,menubar=no,scrollbars=yes,width=500,height=200\"); nfs_export.ifield = ifield; window.ifield = ifield }' value=\"...\">\n";
        }
return undef;
}

