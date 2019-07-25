
%define name	pxsup2dast
%define version	20090809
%define rel	2
%define release %mkrel %rel

Summary:	Project X sup to dvdauthor subtitle xml converter
Name:		%name
Version:	20120704
Release:	1
Group:		Video
License:	GPLv2
URL:		http://www.guru-group.fi/~too/sw/m2vmp2cut/
Source:		http://www.guru-group.fi/~too/sw/m2vmp2cut/pxsup2dast.c
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	zlib-devel

%description
Converts Project X sup files to dvdauthor subtitle xml files.

%prep
%setup -q -c -T
cp -a %SOURCE0 .

%build
# and points go to the author for his imaginative build system :)
export CC="%__cc %optflags"
sh pxsup2dast.c

%install
rm -rf %{buildroot}
install -d -m755 %{buildroot}%{_bindir}
install -m755 %{name} %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{name}



%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 20090809-2mdv2011.0
+ Revision: 614628
- the mass rebuild of 2010.1 packages

* Sat Feb 06 2010 Anssi Hannula <anssi@mandriva.org> 20090809-1mdv2010.1
+ Revision: 501458
- new version
- update license tag

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 20070305-1mdv2009.0
+ Revision: 136445
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Apr 17 2007 Anssi Hannula <anssi@mandriva.org> 20070305-1mdv2008.0
+ Revision: 13949
- new version


* Sun Aug 06 2006 Anssi Hannula <anssi@mnadriva.org> 20050814-2mdv2007.0
- fix buildrequires

* Mon Jul 17 2006 Anssi Hannula <anssi@mandriva.org> 20050814-1mdv2007.0
- initial Mandriva release

