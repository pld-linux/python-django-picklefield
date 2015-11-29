#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define 	module	django-picklefield
Summary:	Pickled object field for Django
Name:		python-%{module}
Version:	0.1.9
Release:	2
License:	MIT
Group:		Development/Languages
URL:		http://pypi.python.org/pypi/django-picklefield
Source0:	http://pypi.python.org/packages/source/d/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	4c2bad7ccbd6981ce3515d2e5e23058b
#BuildRequires:	python-coverage
#BuildRequires:	python-devel
#BuildRequires:	python-django
#BuildRequires:	python-nose
#BuildRequires:	python-pyflakes
#BuildRequires:	python-setuptools
#BuildRequires:	python-sqlite
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	sed >= 4.0
Requires:	python-django
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
django-picklefield provides an implementation of a pickled object
field. Such fields can contain any picklable objects.

%prep
%setup -q -n %{module}-%{version}
%{__sed} -i -e 's/^from ez_setup/#from ez_setup/' setup.py
%{__sed} -i -e 's/^use_setuptools()/#use_setuptools()/' setup.py

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install \
	--root $RPM_BUILD_ROOT

%py_postclean

rm -rf $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/tests
rm -rf $RPM_BUILD_ROOT%{py_sitescriptdir}/tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/picklefield
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/django_picklefield-%{version}-*.egg-info/
%endif
