#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Package-New
Version  : 0.09
Release  : 19
URL      : https://cpan.metacpan.org/authors/id/M/MR/MRDVT/Package-New-0.09.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MR/MRDVT/Package-New-0.09.tar.gz
Summary  : 'Simple base package from which to inherit'
Group    : Development/Tools
License  : BSD-3-Clause
Requires: perl-Package-New-license = %{version}-%{release}
Requires: perl-Package-New-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Devel::Hide)

%description
The Package::New object provides a consistent object constructor for
objects.

%package dev
Summary: dev components for the perl-Package-New package.
Group: Development
Provides: perl-Package-New-devel = %{version}-%{release}
Requires: perl-Package-New = %{version}-%{release}

%description dev
dev components for the perl-Package-New package.


%package license
Summary: license components for the perl-Package-New package.
Group: Default

%description license
license components for the perl-Package-New package.


%package perl
Summary: perl components for the perl-Package-New package.
Group: Default
Requires: perl-Package-New = %{version}-%{release}

%description perl
perl components for the perl-Package-New package.


%prep
%setup -q -n Package-New-0.09
cd %{_builddir}/Package-New-0.09

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Package-New
cp %{_builddir}/Package-New-0.09/LICENSE %{buildroot}/usr/share/package-licenses/perl-Package-New/571205fab3219483856ac156c78539db74834e7e
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Package::New.3
/usr/share/man/man3/Package::New::Dump.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Package-New/571205fab3219483856ac156c78539db74834e7e

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Package/New.pm
/usr/lib/perl5/vendor_perl/5.34.0/Package/New/Dump.pm
