Name:       tup
Version:    0.7.8.20.g1d2fd514
Release:    1%{?dist}
Summary:    A file-based build system
License:    GPLv2
URL:        http://gittup.org/tup
Packager:   js+tup@alien8.de

Source0: https://github.com/gittup/tup/archive/1d2fd51418cc8dd7d1a526fff55e65329b02b13e.tar.gz
Patch0: tup-without-git.patch

BuildRequires: fuse-devel, pcre-devel, gcc
Requires: fuse, pcre

%description

Tup is a file-based build system for Linux, OSX, and Windows. It inputs a list
of file changes and a directed acyclic graph (DAG), then processes the DAG to
execute the appropriate commands required to update dependent files. Updates are
performed with very little overhead since tup implements powerful build
algorithms to avoid doing unnecessary work. This means you can stay focused on
your project rather than on your build system.

%prep
%setup -q -n "tup-1d2fd51418cc8dd7d1a526fff55e65329b02b13e"

%patch0

%build
TUP_BUILD_VERSION=v%{version} ./bootstrap-nofuse.sh

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 tup %{buildroot}/%{_bindir}/tup

mkdir -p %{buildroot}/%{_mandir}/man1
install -m 0644 tup.1 %{buildroot}/%{_mandir}/man1/tup.1

%files
%{_bindir}/tup
%{_mandir}/man1/tup.1.*

%doc COPYING README.md CONTRIBUTING.md


%changelog

