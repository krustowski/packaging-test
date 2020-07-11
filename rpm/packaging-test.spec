Name:           packaging-test
Version:        0.2
Release:        1%{?dist}
Summary:        RPM testing package

License:        GPLv3+
URL:            https://github.com/krustowski/%{name}
Source0:        https://gitlab.labs.nic.cz/knot/%{name}/-/archive/v0.2/%{name}-v0.2.tar.gz

BuildRequires:  gcc make libuv libuv-devel
Requires:       systemd bash

%description
Fedora packaging test, %{name} is a test package for CZ.NIC job application.

%prep
%autosetup
mv %{_build}/%{name}-v%{version} %{name}-%{version}


%build
make
#%make_install


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}
%make_install


%files
%license LICENSE
%{_bindir}/%{name}


%changelog
* Fri Jul 10 2020 Krystof Sara <k@n0p.cz>
- Fedora RPM package testing 
