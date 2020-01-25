#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	DateTime
%define	pnam	Event-ICal
Summary:	DateTime::Event::ICal - Perl DateTime extension for computing rfc2445 recurrences
Summary(pl.UTF-8):	DateTime::Event::ICal - rozszerzenie DateTime o obliczanie rekurencji rfc2445
Name:		perl-DateTime-Event-ICal
Version:	0.13
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/F/FG/FGLOCK/DateTime-Event-ICal-%{version}.tar.gz
# Source0-md5:	cc7fc1f939c41c3c6e25b349917fbcdc
URL:		http://search.cpan.org/dist/DateTime-Event-ICal/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-DateTime
BuildRequires:	perl-DateTime-Event-Recurrence >= 0.11
%endif
Requires:	perl-DateTime >= 1:0.34-1.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides convenience methods that let you easily create
DateTime::Set objects for rfc2445 style recurrences.

%description -l pl.UTF-8
Ten moduł dostarcza wygodne metody pozwalające łatwo tworzyć obiekty
DateTime::Set dla rekurencji w stylu rfc2445.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/DateTime/Event/*.pm
%{_mandir}/man3/*
