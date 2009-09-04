
%define name	pxsup2dast
%define version	20070305
%define rel	2
%define release %mkrel %rel

Summary:	Project X sup to dvdauthor subtitle xml converter
Name:		%name
Version:	%version
Release:	%release
Group:		Video
License:	GPL
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

