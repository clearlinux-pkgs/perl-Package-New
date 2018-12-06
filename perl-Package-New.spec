#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Package-New
Version  : 0.07
Release  : 4
URL      : https://cpan.metacpan.org/authors/id/M/MR/MRDVT/Package-New-0.07.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MR/MRDVT/Package-New-0.07.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libp/libpackage-new-perl/libpackage-new-perl_0.07-2.debian.tar.xz
Summary  : Simple base package from which to inherit
Group    : Development/Tools
License  : BSD-3-Clause
Requires: perl-Package-New-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
The Package::New object provides a consistent object constructor for
objects.

%package dev
Summary: dev components for the perl-Package-New package.
Group: Development
Provides: perl-Package-New-devel = %{version}-%{release}

%description dev
dev components for the perl-Package-New package.


%package license
Summary: license components for the perl-Package-New package.
Group: Default

%description license
license components for the perl-Package-New package.


%prep
%setup -q -n Package-New-0.07
cd ..
%setup -q -T -D -n Package-New-0.07 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Package-New-0.07/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Package-New
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Package-New/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Package-New/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1Package/New.pm
/usr/lib/perl5/vendor_perl/5.28.1Package/New/Dump.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Package::New.3
/usr/share/man/man3/Package::New::Dump.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Package-New/LICENSE
/usr/share/package-licenses/perl-Package-New/deblicense_copyright
