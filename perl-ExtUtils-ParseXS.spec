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
Version:	3.30
Release:	1
Epoch:		1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/ExtUtils/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	db1d2dffcf538c9b49701d8aa2aea7fa
URL:		http://search.cpan.org/dist/ExtUtils-ParseXS/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.46
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

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/ExtUtils/ParseXS.pod
# in perl-devel-tools
%{__rm} $RPM_BUILD_ROOT%{_bindir}/xsubpp \
	$RPM_BUILD_ROOT%{_mandir}/man1/xsubpp.1p

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/ExtUtils/ParseXS.pm
%{perl_vendorlib}/ExtUtils/ParseXS
%{perl_vendorlib}/ExtUtils/Typemaps.pm
%{perl_vendorlib}/ExtUtils/Typemaps
%{perl_vendorlib}/ExtUtils/xsubpp
%{_mandir}/man3/ExtUtils::ParseXS*.3pm*
%{_mandir}/man3/ExtUtils::Typemaps*.3pm*
