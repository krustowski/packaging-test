%global debug_package %{nil}
%define build_dir /home/krusty/rpmbuild/BUILD

Name:           packaging-test
Version:        0.2
Release:        1%{?dist}
Summary:        RPM testing package

License:        GPLv3+
URL:            https://github.com/krustowski/%{name}
Source0:        https://gitlab.labs.nic.cz/knot/%{name}/-/archive/v0.2/%{name}-v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make 
BuildRequires:  libuv 
BuildRequires:  libuv-devel
BuildRequires:	systemd-rpm-macros
Requires:       bash
Requires:	systemd

%description
Fedora packaging test, %{name} is a test package for CZ.NIC job application.

%prep
%setup -n packaging-test-v0.2
cp ~/pckg/packaging-test/Makefile ./
cp ~/pckg/packaging-test/rpm/greet.sh.patch ./
patch < greet.sh.patch

%build
make
#%make_install


%install
#rm -rf $RPM_BUILD_ROOT
#cd /home/krusty/rpmbuild/BUILD/packaging-test-0.2

mkdir -p %{buildroot}/%{_bindir}
install -m 0755 demo_libuv %{buildroot}/%{_bindir}
install -m 0755 greet.sh %{buildroot}/%{_bindir}
#%make_install


%files
%license LICENSE
%{_bindir}/demo_libuv
%{_bindir}/greet.sh


%changelog
* Fri Jul 10 2020 Krystof Sara <k@n0p.cz>
- Fedora RPM package testing 
