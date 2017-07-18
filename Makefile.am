SUBDIRS  =
# @subdirs@ are the configured subproject directories
SUBDIRS += @subdirs@
SUBDIRS += .

CLEANFILES =
TESTS =
check_SCRIPTS =

EXTRA_DIST = COPYING.LIB

EXTRA_DIST += README.md

ACLOCAL_AMFLAGS = -I auto-m4 -I gphoto-m4

# The gphoto2 testsuite (in src/gphoto2/tests/testsuite) requires
# CAMLIBS and IOLIBS to be set properly. Otherwise, the "make check"
# part of "make distcheck" of gphoto-suite will fail in src/gphoto2
# when that testsuite runs test based on the 'directory' camlib.
#
# The libgphoto2{,_port}-uninstalled.pc files with their `driverdir`
# variables are built too late to be of any help to us.
CAMLIBS = $(PWD)/src/libgphoto2/camlibs
IOLIBS = $(PWD)/src/libgphoto2/libgphoto2_port
export CAMLIBS
export IOLIBS

# Avoid rebuilding of gphoto-m4/Makefile.in as gphoto-m4 now supports
# single Makefile.am builds with Makefile includes.
include gphoto-m4/Makefile-files
include tools/Makefile-files
include tests/Makefile-files


#######################################################################
# Help for the maintainer
#

.PHONY: update-manpages
update-manpages:
	if test -d "$(top_builddir)/src/gphoto2-manual"; then \
		cp "$(top_builddir)/src/gphoto2-manual/src/man/libgphoto2.3" \
			"$(top_builddir)/src/libgphoto2/doc/"; \
		cp "$(top_builddir)/src/gphoto2-manual/src/man/libgphoto2_port.3" \
			"$(top_builddir)/src/libgphoto2/doc/"; \
		cp "$(top_builddir)/src/gphoto2-manual/src/man/gphoto2.1" \
			"$(top_builddir)/src/gphoto2/doc/"; \
	fi; exit 0

# End of Makefile.am.
