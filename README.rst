========
zonediff
========

Library and commandline tool to create logical diffs of zonefiles

Installing
==========
python setup.py install

Usage
=====

You can use this tool as a python library or as a standalone tool.

Standalone
----------
``python -mzonediff [options] [versioncontrol] zonefile version1 [version2]``

zonediff can use plaintext files or version control checkouts. At the moment it
supports git, bzr and rcs, but support for other systems is easy to implement.
The two main modes of operations are:

* ``python -mzonediff foo-old.zone foo-new.zone``
* ``python -mzonediff --bzr foo.zone 45 46``

Output is either html or plain text.

See the output of ``python -mzonediff --help`` for complete usage info

As a library
------------

3 functions are available: ``diff_zones``, ``format_changes_plain`` and
``format_changes_html``. They do what their name suggests they do.

``diff_zones(zone1, zone2, ignore_ttl=False, ignore_soa=False) -> changes``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Compares two dns.zone.Zone objects and returns a list of all changes in the
format (name, oldnode, newnode).

If ignore_ttl is true, a node will not be added to this list if the only change
is its TTL.
    
If ignore_soa is true, a node will not be added to this list if the only
changes is a change in a SOA Rdata set.

The returned nodes do include all Rdata sets for all nodes with changes,
including unchanged Rdata sets.

dns.zone.Zone objects can be created from open filehandles as such:
``dns.zone.from_file(old, origin = '.', check_origin=False)``

``format_changes(oldfile, newfile, changes, ignore_ttl=False) -> str``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Given 2 filenames and a list of changes from diff_zones, produce diff-like
output. If ignore_ttl is True, TTL-only changes are not displayed


``format_changes(oldfile, newfile, changes, ignore_ttl=False) -> str``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Given 2 filenames and a list of changes from diff_zones, produce nice html
output. If ignore_ttl is True, TTL-only changes are not displayed
