%define real_name OLE-Storage_Lite

Summary:	OLE::Storage_Lite - Simple Class for OLE document interface.
Name:		perl-%{real_name}
Version:	0.14
Release:	%mkrel 3
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://www.cpan.org
Source0:	%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
OLE::Storage_Lite - Simple Class for OLE document interface.

%prep

%setup -q -n %{real_name}-%{version}

# perl path hack
find . -type f | xargs perl -p -i -e "s|^#\!/usr/local/bin/perl|#\!/usr/bin/perl|g"

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor 

%make OPTIMIZE="%{optflags}"

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%makeinstall_std

%clean 
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README sample
%{perl_vendorlib}/OLE
%{_mandir}/*/*


