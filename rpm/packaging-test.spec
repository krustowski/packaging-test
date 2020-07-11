%global debug_package %{nil}
%define build_dir /home/krusty/rpmbuild/BUILD

Name:           packaging-test
Version:        0.2
Release:        2%{?dist}
Summary:        RPM testing package

License:        GPLv3+
URL:            https://github.com/krustowski/%{name}
Source0:        https://gitlab.labs.nic.cz/knot/%{name}/-/archive/v0.2/%{name}-v%{version}.tar.gz
#Patch1:		greet.sh.patch

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
cp ~/pckg/packaging-test/debian/packaging-test.service ./
cp ~/pckg/packaging-test/service_start.sh ./
patch < greet.sh.patch
#%patch1 -p1

%build
make
%make_install


%install
#rm -rf $RPM_BUILD_ROOT

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_usr}/share/%{name}
mkdir -p %{buildroot}%{_unitdir}

install -p -m 0755 -D demo_libuv %{buildroot}%{_bindir}
install -p -m 0755 -D greet.sh %{buildroot}%{_bindir}

install -p -m 0744 -D service_start.sh %{buildroot}%{_usr}/share/%{name}/service_start.sh
install -p -m 0644 -D packaging-test.service %{buildroot}%{_unitdir}/packaging-test.service
#%make_install


%preun
%systemd_preun packaging-test.service


%postun
%systemd_postun_with_restart packaging-test.service


%files
%license LICENSE
%config %{name}.service
%{_bindir}/demo_libuv
%{_bindir}/greet.sh
%{_usr}/share/%{name}/service_start.sh
%{_unitdir}/packaging-test.service


%changelog
* Sat Jul 11 2020 Krystof Sara <k@n0p.cz>
- greet.sh patching and systemd service integration

* Fri Jul 10 2020 Krystof Sara <k@n0p.cz>
- Fedora RPM package testing 
