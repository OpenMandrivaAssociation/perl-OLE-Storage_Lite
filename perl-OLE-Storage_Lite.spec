%define modname	OLE-Storage_Lite
%define modver	0.19

Summary:	Simple Class for OLE document interface
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	14
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://www.cpan.org/modules/by-module/OLE/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
OLE::Storage_Lite allows you to read and write an OLE structured file. Please
refer OLE::Storage by Martin Schwartz.

OLE::Storage_Lite::PPS is a class representing PPS.
OLE::Storage_Lite::PPS::Root, OLE::Storage_Lite::PPS::File and
OLE::Storage_Lite::PPS::Dir are subclasses of OLE::Storage_Lite::PPS.

%prep
%setup -qn %{modname}-%{modver}

# perl path hack
find . -type f | xargs perl -p -i -e "s|^#\!/usr/local/bin/perl|#\!/usr/bin/perl|g"

%build
%__perl Makefile.PL INSTALLDIRS=vendor 
%make OPTIMIZE="%{optflags}"

%install
%makeinstall_std

%files
%doc Changes README sample
%{perl_vendorlib}/OLE
%{_mandir}/man3/*

