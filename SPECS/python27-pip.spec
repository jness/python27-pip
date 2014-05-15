%define __python /usr/bin/python%{pybasever}
# sitelib for noarch packages
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%define pyver 27
%define pybasever 2.7

Name:           python%{pyver}-pip
Version:        1.5.5
Release:        1.ius%{?dist}
Summary:        A tool for installing and managing Python packages.

Group:          Development/Languages
License:        MIT
URL:            http://pypi.python.org/pypi/pip
Source0:        http://pypi.python.org/packages/source/p/pip/pip-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python%{pyver}-devel, python%{pyver}-setuptools
Requires:       python%{pyver}-setuptools, python%{pyver}-devel

%description
A tool for installing and managing Python packages.

%prep
%setup -q -n pip-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc docs/*rst PKG-INFO AUTHORS.txt LICENSE.txt
%{python_sitelib}/*
%attr(755,root,root) %{_bindir}/pip*


%changelog
* Thu May 15 2014 Jeffrey Ness <jeffrey.ness@rackspace.com> - 1.5.5-1
- First build
