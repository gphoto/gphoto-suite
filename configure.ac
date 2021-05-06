AC_PREREQ(2.69)
dnl Use a short version and package name here, or "make dist" will fail
dnl packaging [...]/libgphoto2_port/gphoto2-port-portability.h
dnl because tar only handles 99 chars per file path. Oh, and GNU tar 1.13
dnl even used to fail silently before automake got the filename-length-max=99
dnl parameter.
dnl
dnl If we want to use a package name like "gphoto-suite-2.2.4", then we have to
dnl remove libgphoto2_port from libgphoto2 and give it its own subdirectory:
dnl   src/libgphoto2_port/libgphoto2_port/gphoto2/gphoto2-port-portability.h
dnl   src/libgphoto2/libgphoto2/...
dnl   src/libgphoto2/camlibs/...
dnl   src/gphoto2/...
dnl That would change the standard module people check out to "gphoto-suite".
dnl
dnl "/src/libgphoto2/libgphoto2_port/libgphoto2_port/gphoto2/gphoto2-port-portability.h"
dnl is 82 characters, which leaves 17 characters for the distdir name.
dnl "gphoto-suite-2.3.0" whould be 18 characters - one too many: 82+18=100 > 99 :-(
dnl
dnl However, "/src/libgphoto2/libgphoto2_port/gphoto2/gphoto2-port-portability.h"
dnl is 66 characters, which leaves 33 characters for the distdir name.
dnl "gphoto-suite-2.3.0" whould be 18 characters - bingo!
AC_INIT([gphoto suite],
        [2.5.23.1],
        [https://github.com/gphoto/gphoto-suite/issues],
        [gphoto-suite],
        [https://github.com/gphoto/gphoto-suite])
AC_CONFIG_SRCDIR([README.md])
AC_CONFIG_HEADERS([config.h])
AC_CONFIG_MACRO_DIR([auto-m4])
AC_CONFIG_AUX_DIR([auto-aux])
AM_INIT_AUTOMAKE([
  -Wall
  -Werror
  foreign
  1.15
  no-dist-gzip
  dist-xz
  check-news
  filename-length-max=99
])

m4_pattern_forbid([^GP_])

GP_CHECK_SHELL_ENVIRONMENT
GP_CONFIG_MSG([Build])
GP_CONFIG_MSG([Source code location],[${srcdir}])


dnl ---------------------------------------------------------------------------
dnl compiler stuff
dnl ---------------------------------------------------------------------------

LT_INIT([
  dlopen
  win32-dll
  disable-static
])

AC_PROG_CC
AC_PROG_CXX

AM_CFLAGS="$CFLAGS"
AM_LDFLAGS="$LDFLAGS"
AM_CPPFLAGS="$CPPFLAGS"

GP_CONFIG_MSG([Compiler],[${CC}])


GP_CONFIG_MSG([Features])


PKG_CHECK_MODULES([PKGMODULECHECK], [pkgmodulecheck], [:], [:])



# ---------------------------------------------------------------------------
# Warnings: If we have GCC, be paranoid.
# ---------------------------------------------------------------------------
AS_VAR_IF([GCC], [yes], [dnl
    AM_CPPFLAGS="$AM_CPPFLAGS -Wall -Wextra -Wchar-subscripts -Wmissing-declarations -Wmissing-prototypes -Wnested-externs -Wpointer-arith"
    AM_LDFLAGS="$AM_LDFLAGS -g -Wall"
])

AC_SUBST([AM_CPPFLAGS])
AC_SUBST([AM_LDFLAGS])


# Configure subdirs.

dnl Absolute directories work with multiple levels of
dnl AC_CONFIG_SUBDIRS recursion, relative directories do not.
gp_top_builddir="$(pwd)/"
gp_top_srcdir="$(cd "${srcdir}" && pwd)/"

GP_SUBPACKAGE([gphoto2_manual])
AS_IF(["$enable_subpackage_gphoto2_manual" && test -f "${srcdir}/src/gphoto2-manual/configure.ac"], [dnl
   AC_CONFIG_SUBDIRS([src/gphoto2-manual])
   # let pkg-config find *-uninstalled.pc
   PKG_CONFIG_PATH="${gp_top_builddir}src/gphoto2-manual${PKG_CONFIG_PATH+:}${PKG_CONFIG_PATH}"
   export PKG_CONFIG_PATH
])

GP_SUBPACKAGE([libexif])
AS_IF(["$enable_subpackage_libexif" && test -f "${srcdir}/src/libexif/configure.ac"], [dnl
   AC_CONFIG_SUBDIRS([src/libexif])
   # let pkg-config find *-uninstalled.pc
   PKG_CONFIG_PATH="${gp_top_builddir}src/libexif${PKG_CONFIG_PATH+:}${PKG_CONFIG_PATH}"
   export PKG_CONFIG_PATH
])

GP_SUBPACKAGE([exif])
AS_IF(["$enable_subpackage_exif" && test -f "${srcdir}/src/exif/configure.ac"], [dnl
   AC_CONFIG_SUBDIRS([src/exif])
])

GP_SUBPACKAGE([libexif_gtk])
AS_IF(["$enable_subpackage_libexif_gtk" && test -f "${srcdir}/src/libexif-gtk/configure.ac"], [dnl
   AC_CONFIG_SUBDIRS([src/libexif-gtk])
   # let pkg-config find *-uninstalled.pc
   PKG_CONFIG_PATH="${gp_top_builddir}src/libexif-gtk${PKG_CONFIG_PATH+:}${PKG_CONFIG_PATH}"
   export PKG_CONFIG_PATH
])

GP_SUBPACKAGE([gexif])
AS_IF(["$enable_subpackage_gexif" && test -f "${srcdir}/src/gexif/configure.ac"], [dnl
   AC_CONFIG_SUBDIRS([src/gexif])
])

GP_SUBPACKAGE([libgphoto2])
AS_IF(["$enable_subpackage_libgphoto2" && test -f "${srcdir}/src/libgphoto2/configure.ac"], [dnl
   AC_CONFIG_SUBDIRS([src/libgphoto2])
   # let pkg-config find *-uninstalled.pc
   PKG_CONFIG_PATH="${gp_top_builddir}src/libgphoto2/libgphoto2_port${PKG_CONFIG_PATH+:}${PKG_CONFIG_PATH}"
   PKG_CONFIG_PATH="${gp_top_builddir}src/libgphoto2${PKG_CONFIG_PATH+:}${PKG_CONFIG_PATH}"
   # PKG_CONFIG_PATH="src/libgphoto2/libgphoto2_port${PKG_CONFIG_PATH+:}${PKG_CONFIG_PATH}"
   # PKG_CONFIG_PATH="src/libgphoto2${PKG_CONFIG_PATH+:}${PKG_CONFIG_PATH}"
   export PKG_CONFIG_PATH
])

GP_SUBPACKAGE([gphoto2])
AS_IF(["$enable_subpackage_gphoto2" && test -f "${srcdir}/src/gphoto2/configure.ac"], [dnl
   AC_CONFIG_SUBDIRS([src/gphoto2])
])

GP_SUBPACKAGE([gphotofs])
AS_IF(["$enable_subpackage_gphotofs" && test -f "${srcdir}/src/gphotofs/configure.ac"], [dnl
   AC_CONFIG_SUBDIRS([src/gphotofs])
])

GP_SUBPACKAGE([libgphoto2_sharp])
AS_IF(["$enable_subpackage_libgphoto2_sharp" && test -f "${srcdir}/src/libgphoto2-sharp/configure.ac"], [dnl
   AC_CONFIG_SUBDIRS([src/libgphoto2-sharp])
])

GP_SUBPACKAGE([libgphoto2_python])
AS_IF(["$enable_subpackage_libgphoto2_python" && test -f "${srcdir}/src/libgphoto2-python/configure.ac"], [dnl
   AC_CONFIG_SUBDIRS([src/libgphoto2-python])
])

GP_SUBPACKAGE([gtkam])
AS_IF(["$enable_subpackage_gtkam" && test -f "${srcdir}/src/gtkam/configure.ac"], [dnl
   AC_CONFIG_SUBDIRS([src/gtkam])
])


dnl ---------------------------------------------------------------------------
dnl Output files
dnl ---------------------------------------------------------------------------
AC_CONFIG_FILES([Makefile])
AC_OUTPUT

GP_CONFIG_OUTPUT
