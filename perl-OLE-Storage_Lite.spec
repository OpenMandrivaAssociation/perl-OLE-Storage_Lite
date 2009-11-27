%define upstream_name    OLE-Storage_Lite
%define upstream_version 0.19

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	Simple Class for OLE document interface
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/OLE/%{upstream_name}-%{upstream_version}.tar.gz

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
OLE::Storage_Lite allows you to read and write an OLE structured file. Please
refer OLE::Storage by Martin Schwartz.

OLE::Storage_Lite::PPS is a class representing PPS.
OLE::Storage_Lite::PPS::Root, OLE::Storage_Lite::PPS::File and
OLE::Storage_Lite::PPS::Dir are subclasses of OLE::Storage_Lite::PPS.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

# perl path hack
find . -type f | xargs perl -p -i -e "s|^#\!/usr/local/bin/perl|#\!/usr/bin/perl|g"

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor 
%make OPTIMIZE="%{optflags}"

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README sample
%{perl_vendorlib}/OLE
%{_mandir}/*/*
