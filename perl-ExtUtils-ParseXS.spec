#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	ExtUtils
%define	pnam	ParseXS
Summary:	ExtUtils::ParseXS - converts Perl XS code into C code
Summary(pl.UTF-8):	ExtUtils::ParseXS - przekształcanie kodu Perl XS do C
Name:		perl-ExtUtils-ParseXS
Version:	2.22_06
%define	filever	2.2206
Release:	1
Epoch:		1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/ExtUtils/DAGOLDEN/%{pdir}-%{pnam}-%{filever}.tar.gz
# Source0-md5:	5a78d0c4654c6b50e7c87da8b671e8a6
URL:		http://search.cpan.org/dist/ExtUtils-ParseXS/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-ExtUtils-CBuilder
BuildRequires:	perl-Test-Simple >= 0.47
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ExtUtils::ParseXS will compile XS code into C code by embedding the
constructs necessary to let C functions manipulate Perl values and
creates the glue necessary to let Perl access those functions. The
compiler uses typemaps to determine how to map C function parameters
and variables to Perl values.

%description -l pl.UTF-8
ExtUtils::ParseXS kompiluje kod XS do kodu C osadzając konstrukcje
umożliwiające funkcjom w C operowanie na wartościach perlowych, a
także tworzy kod sklejający umożliwiający Perlowi dostęp do tych
funkcji. Kompilator wykorzystuje plik typemaps do określenia sposobu
odwzorowywania parametrów funkcji i zmiennych C na wartości perlowe.

%prep
%setup -q -n %{pdir}-%{pnam}-%{filever}

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
%doc Changes
%{perl_vendorlib}/ExtUtils/ParseXS.pm
%{perl_vendorlib}/ExtUtils/xsubpp
%{_mandir}/man3/ExtUtils::ParseXS.3pm*
