# Packaging Test

## git repository

- Clone this git repository and commit all the changes you make.
- After you're done, push your git repository somewhere publicly accessible (e.g. gitlab.com, github.com).

## Shell scripting

Make the following changes to the greet.sh script:
- Include the user's username in the greeting.
- Include the current weekday in the greeting.
- Handle an *optional* argument in the script. The argument is a number indicating
  how many times the user should be greeted. When omitted, the script behaviour
  remains the same (user is greeted once).

## Packaging

Create a debian or rpm (or both!) package for the that installs `demo_libuv` executable compiled from `demo_libuv.c` file from this repository.

Use the following upstream tarball for your packaging:
https://gitlab.labs.nic.cz/knot/packaging-test/-/archive/v0.2/packaging-test-v0.2.tar.gz

Create all the source packaging files needed to create the package and put them
in `debian/` or `rpm/` directory.

If you're not sure where to start, check out the resources about debian or rpm
packaging in the links section below, or use a search engine. A good place to
start is also to take a look at some of the existing packages which are
similar. An example of a fairly simple package is lua-basexx.

### Systemd integration

Create a systemd unit file that can be used to run `demo_libuv` as a oneshot
service. Include it in the package as a downstream file.

## Resources

- Debian packaging: https://wiki.debian.org/Packaging
- Debian repository with packages: https://salsa.debian.org
- Debian Policy Manual: https://www.debian.org/doc/debian-policy/
- RPM packaging guide: https://rpm-packaging-guide.github.io
- Fedora repository with packages: https://src.fedoraproject.org/
- Fedora Packaging Guidelines: https://docs.fedoraproject.org/en-US/packaging-guidelines/
