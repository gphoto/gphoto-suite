gphoto-suite
============

gphoto-suite is a kind of umbrella package which contains required
(sub)packages related to `libgphoto2` in one convenient package.

`gphoto-suite` makes compiling and installing from scratch easier for

  - people without much compilation experience
  - people who use cross compilation environments
  - people who run test builds and runtime tests
  - people who build integrated binary packages of `libgphoto2` and
    `gphoto2`


Legal stuff:
------------

`gphoto-suite` includes multiple packages which are mostly licensed
under GPL or LGPL. See the respective packages in `src/*` for details.


Quick Start:
------------

This part is still to be written for the new `git` based setup which
replaces the old `svn` based one.


Getting the source code via git
-------------------------------

Sources:

    git@github.com:gphoto/gphoto-suite.git
    https://github.com/gphoto/gphoto-suite.git

Get the sources:

    git clone --recursive git@github.com:gphoto/gphoto-suite.git

If you forgot the `--recursive` argument to `git clone`:

    git clone git@github.com:gphoto/gphoto-suite.git
    git submodule update --init --recursive

For `git amb`, clone and install `ndim-git-utils` from the following
place, and then use `git amb`:

    git clone https://github.com/ndim/ndim-git-utils.git

    cd gphoto-suite
    git amb make distcheck
	ls -l _build/master/*.tar.*

If you have to make changes to src/gphoto-m4, src/gphoto2,
src/libgphoto2 and push those upstream, change to the respective
directory and make sure that you actually have a git HEAD (not a
detached head).


Make sure required (or optional) dependencies are installed:
------------------------------------------------------------

Highest importance:
    pkgconfig
    libusb-dev libexif-dev libjpeg-dev
    libpopt-dev libltdl-dev

Recommended:
    libreadline-dev

Less important:
    doxygen

Optional:
    libaa-dev


Configure the build system:
---------------------------

This step is required regardless of the method you used to get
gphoto-suite.

Run

    ./configure --help=recursive

to get help on all the parameters for subprojects.

Note that some subproject options will be automatically set by
`gphoto-suite`. This mostly concerns the `*_CFLAGS` and `*_LIBS`
for the libraries `gphoto-suite` provides by itself.

Then run (for an in-tree build)

    ./configure

with your favourite configure parameters. Or, for an out-of-tree build:

    mkdir ../gphoto-suite-build
    cd ../gphoto-suite-build
    ../gphoto-suite/configure ...

with your favourite configure parameters.

If need be, you can even build the included subprojects by themselves:

    mkdir ../libgphoto2-build
    cd ../libgphoto2-build
    ../gphoto-suite/src/libgphoto2/configure ...


Compilation:
------------

Use the standard commands:

    make
    make install

The latter may be given a DESTDIR= parameter or run as root.


Cross-compilation:
------------------

This is an example using `i586-mingw32msvc` as the system for which
you want to compile (i.e. `i586-mingw32msvc-gcc` will be the compiler).
The build system for this example is `i686-pc-linux` (you can run
`config.guess` to determine the build system).

Note that you may want *not* to use

    ../configure --prefix=/foo/bar/usr ...
    make all
    make install

but

    ../configure --prefix=/usr ...
    make all
    make DESTDIR=/foo/bar install

if you have the "root" (`/`) directory of the system the stuff is
supposed to run on mapped into `/foo/bar`. It depends on your setup.

You can build `gphoto-suite` for that platform by running:

    mkdir _win32 && cd _win32
    ../configure --prefix=/tmp/lt-win32-inst \
        --host=i586-mingw32msvc --build=i686-pc-linux
    make all
    make install

If you have an emulator properly installed for the binaries, even
`make check` will give results. Yes, you can compile and test Windows
binaries on a Linux system!


Run the tests:
--------------

Run

    make check

and examine the output.


Check the distribution mechanism:
---------------------------------

Run

    make distcheck

and see whether it finishes without errors.


Reduced driver build
--------------------

For a quick `make distcheck`, it can be advantageous to not build all
camlibs and iolibs:

    make BUILD_THESE_CAMLIBS="directory.la" IOLIB_LTLIST="disk.la" distcheck

Adding a `-j3` or similar might also speed up things.
