#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	ExtUtils
%define	pnam	ParseXS
Summary:	ExtUtils::ParseXS - converts Perl XS code into C code
Summary(pl):	ExtUtils::ParseXS - przekszta³canie kodu Perl XS do C
Name:		perl-ExtUtils-ParseXS
Version:	2.17
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
#Source0:	http://www.cpan.org/modules/by-authors/id/K/KW/KWILLIAMS/ExtUtils-ParseXS-2.17.tar.gz
Source0:	http://www.cpan.org/modules/by-module/ExtUtils/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	36553d14f8cc424ed124130f8d8823f3
URL:		http://search.cpan.org/dist/ExtUtils-ParseXS/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-ExtUtils-CBuilder
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ExtUtils::ParseXS will compile XS code into C code by embedding the
constructs necessary to let C functions manipulate Perl values and
creates the glue necessary to let Perl access those functions. The
compiler uses typemaps to determine how to map C function parameters
and variables to Perl values.

%description -l pl
ExtUtils::ParseXS kompiluje kod XS do kodu C osadzaj±c konstrukcje
umo¿liwiaj±ce funkcjom w C operowanie na warto¶ciach perlowych, a
tak¿e tworzy kod sklejaj±cy umo¿liwiaj±cy Perlowi dostêp do tych
funkcji. Kompilator wykorzystuje plik typemaps do okre¶lenia sposobu
odwzorowywania parametrów funkcji i zmiennych C na warto¶ci perlowe.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/ExtUtils/ParseXS.pm
%{_mandir}/man3/ExtUtils::ParseXS.3*
