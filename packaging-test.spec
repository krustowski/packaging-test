Name: 		packaging-test
Version:	0.2
Release:	1
Summary:	RPM testing package
License:	GPL-3.0-or-later
#Source0:	https://gitlab.labs.nic.cz/knot/packaging-test/-/archive/v0.2/packaging-test-v0.2.tar.gz

%description
A testing RPM package for package-testing tarball.

%prep
# not yet

%build
# make

%install
mkdir -p %{buildroot}/usr/bin/
#install -m 755 demo_libuv %{buildroot}/usr/bin/demo_libuv
#install -m 755 greet.sh %{buildroot}/usr/bin/greet.sh

%files
#/usr/bin/demo_libuv
#/usr/bin/greet.sh

%changelog
# skip
