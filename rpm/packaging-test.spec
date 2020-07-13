%global debug_package %{nil}

Name:           packaging-test
Version:        0.2
Release:        3%{?dist}
Summary:        RPM testing package

License:        GPLv3+
URL:            https://github.com/krustowski/%{name}
Source0:        https://gitlab.labs.nic.cz/knot/%{name}/-/archive/v0.2/%{name}-v%{version}.tar.gz
Source1:	https://raw.githubusercontent.com/krustowski/%{name}/master/Makefile
Source2:	https://raw.githubusercontent.com/krustowski/%{name}/master/rpm/%{name}.service
Source3:	https://raw.githubusercontent.com/krustowski/%{name}/master/service_start.sh
Patch0:		https://raw.githubusercontent.com/krustowski/%{name}/master/rpm/greet.sh.patch

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
patch < %{_sourcedir}/greet.sh.patch
cp %{_sourcedir}/Makefile ./
cp %{_sourcedir}/%{name}.service ./
cp %{_sourcedir}/service_start.sh ./

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
install -p -m 0644 -D %{name}.service %{buildroot}%{_unitdir}/%{name}.service
#%make_install

%post
%systemd_post packaging-test.service
systemctl start packaging-test.service

%preun
%systemd_preun packaging-test.service

%postun
%systemd_postun packaging-test.service

%files
%license LICENSE
%{_bindir}/demo_libuv
%{_bindir}/greet.sh
%{_usr}/share/%{name}/service_start.sh
%{_unitdir}/%{name}.service

%changelog
* Sun Jul 12 2020 Krystof Sara <k@n0p.cz>
- Remote sources and patches added
- Systemd service installation fix

* Sat Jul 11 2020 Krystof Sara <k@n0p.cz>
- greet.sh patching and systemd service integration

* Fri Jul 10 2020 Krystof Sara <k@n0p.cz>
- Fedora RPM package testing 
