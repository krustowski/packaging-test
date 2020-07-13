#!/bin/bash

# build.sh
# A universal script for automatic package building on Debian & Fedora environments
# by Krystof Sara / 13. 7. 2020

function die {
	printf "$1\n\n"
	exit 1
}

#[[ $EUID -eq 0 ]] || die "Must be run as root..."

uname -a | grep -qw "Linux" || die "Must be run on a Linux machine..."

# Distro extraction
DISTRO=""
DISTRO_FULL=$(cat /etc/os-release | grep PRETTY_NAME= | cut -d'=' -f2)

# Debian or Fedora
echo $DISTRO_FULL | grep -qw "Debian" && DISTRO="Debian"
echo $DISTRO_FULL | grep -qw "Fedora" && DISTRO="Fedora"

[[ ! $DISTRO ]] && die "Unknown Linux distribution..."

# Prepare the environment and build the package
PCKG_NAME="packaging-test"
PCKG_VERSION="0.2"

cd "$(dirname $0)"

case $DISTRO in
	"Debian")
		echo "Installing the prereqs (with sudo)..."
		sudo apt install gcc make libuv1 libuv1-dev debhelper devscripts build-essential -yy \
		       && printf "Ok.\n\n" \
		       || die "Error occured during the installation..."

		echo "Downloading the upstream tarball..."
		wget -O "../packaging-test_0.2.orig.tar.gz" "https://gitlab.labs.nic.cz/knot/$PCKG_NAME/-/archive/v0.2/$PCKG_NAME-v$PCKG_VERSION.tar.gz" \
			&& printf "Ok.\n\n" \
			|| die "Error occured during the upstream tarball downloading..."

		echo "Building the DEB package..."
		sleep 3
		debuild -uc -us -ui -i \
			&& printf "\nOk. Package is located in the upper directory ($PWD/../).\n\n" \
			|| die "Error occured during the package building..."
		;;

	"Fedora")
		echo "Installing the prereqs (with sudo)..."
		sudo dnf install gcc make rpm-build rpm-devel rpmlint coreutils diffutils patch rpmdevtools -yy \
			&& printf "Ok.\n\n" \
			|| die "Error occured during the installation..."

		echo "Setting the rpm tree structure..."
		rpmdev-setuptree \
			&& printf "Ok.\n\n" \
			|| die "The tree cannot be set..."

		echo "Building the RPM package..."
		sleep 3
		rpmbuild -bb rpm/packaging-test.spec \
			&& printf "\nOk. Package is located in '$HOME/rpmbuild/RPMS' directory.\n\n" \
			|| die "Error occured during the package building..."
		;;
esac
