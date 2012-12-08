%define upstream_name    OLE-Storage_Lite
%define upstream_version 0.19

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Simple Class for OLE document interface
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/OLE/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

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
%__perl Makefile.PL INSTALLDIRS=vendor 
%make OPTIMIZE="%{optflags}"

%install
%makeinstall_std

%files
%doc Changes README sample
%{perl_vendorlib}/OLE
%{_mandir}/*/*


%changelog
* Fri Nov 27 2009 Jérôme Quelin <jquelin@mandriva.org> 0.190.0-1mdv2010.1
+ Revision: 470466
- update to 0.19

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.180.0-1mdv2010.0
+ Revision: 401996
- rebuild using %%perl_convert_version

* Sun Jan 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.18-1mdv2009.1
+ Revision: 324516
- update to new version 0.18

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.17-2mdv2009.0
+ Revision: 268633
- rebuild early 2009.0 package (before pixel changes)

* Tue May 13 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.17-1mdv2009.0
+ Revision: 206821
- update to new version 0.17

* Thu Feb 21 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.16-1mdv2008.1
+ Revision: 173558
- new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Dec 03 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.15-1mdv2008.1
+ Revision: 114650
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - fix summary-ended-with-dot


* Fri Feb 02 2007 Oden Eriksson <oeriksson@mandriva.com> 0.14-3mdv2007.0
+ Revision: 115947
- Import perl-OLE-Storage_Lite

* Sun Jan 08 2006 Oden Eriksson <oeriksson@mandriva.com> 0.14-2mdk
- rebuild

* Thu Dec 02 2004 Oden Eriksson <oden.eriksson@linux-mandrake.com> 0.14-1mdk
- initial mandrake package

