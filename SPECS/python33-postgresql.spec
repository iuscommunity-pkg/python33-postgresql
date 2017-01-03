%global __python33 /usr/bin/python3.3
%{!?python33_sitearch: %global python33_sitearch %(%{__python33} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}

Name:           python33-postgresql
Version:        1.2.1
Release:        2.ius%{?dist}
Summary:        Connect to PostgreSQL with Python 3

Group:          Applications/Databases
License:        BSD
URL:            http://python.projects.postgresql.org/
Source0:        https://pypi.io/packages/source/p/py-postgresql/py-postgresql-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  python33-devel

%description
py-postgresql is a Python 3 package providing modules to work with PostgreSQL.
This includes a high-level driver, and many other tools that support a
developer working with PostgreSQL databases.

%prep
%setup -q -n py-postgresql-%{version}


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python33} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python33} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS LICENSE README
%{python33_sitearch}/*


%changelog
* Tue Jan 03 2017 Ben Harper <ben.harper@rackspace.com> - 1.2.1-2.ius
- update python33_sitearch macro

* Thu Dec 29 2016 Ben Harper <ben.harper@rackspace.com> - 1.2.1-1.ius
- Latest upstream
- update Source0 URL

* Tue Oct 16 2012 Ben Harper <ben.harper@rackspace.com> - 1.1.0-1.ius
- Porting from python32-postgresql

* Tue Jul 31 2012 Jeffrey Ness <jeffrey.ness@rackspace.com> - 1.0.4-1.ius
- New package for python32
