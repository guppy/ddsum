Name:      ddsum
Summary:   checksum tool
Version:   3
Release:   1
License:   BSD
Group:     System Environment/Base
URL:       http://ddsum.com
Source0:   http://ddsum.com/download/ddsum-%{version}.tar.gz
Requires:  python
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
ddsum is a checksum tool inspired by dd5sum.

%prep
%setup -q

%{__rm} -rf %{buildroot}


%install
mkdir -p %{buildroot}/%{_bindir}
cp -f ddsum  %{buildroot}/%{_bindir}/

%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root)
%{_bindir}/ddsum


%changelog
* Wed Feb 16 2011 Jeff Fisher <guppy@ddsum.com> - 3-1
- Added support for versions of python without hashlib
- Cleaned up error output

* Tue Feb 15 2011 Jeff Fisher <guppy@ddsum.com> - 2-1
- Added a spec file 
