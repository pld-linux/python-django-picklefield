#
# Conditional build:
%bcond_with	tests	# unit tests (not included in sdist)

%define 	module	django-picklefield
Summary:	Pickled object field for Django
Summary(pl.UTF-8):	Serializowalne przez pickle pole obiektowe dla Django
Name:		python-%{module}
# keep 2.x here for python2/Django 1.11 support
Version:	2.1.1
Release:	1
License:	MIT
Group:		Development/Languages/Python
Source0:	https://files.pythonhosted.org/packages/source/d/django-picklefield/%{module}-%{version}.tar.gz
# Source0-md5:	cbebe7750ba7b5744c8e1a6875a3ee7c
URL:		https://pypi.org/project/django-picklefield/
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-django >= 1.11
%endif
BuildRequires:	rpmbuild(macros) >= 1.714
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
django-picklefield provides an implementation of a pickled object
field. Such fields can contain any picklable objects.

%description -l pl.UTF-8
django-picklefield dostarcza implementację pola obiektowego
serializowalnego przez pickle. Pola takie mogą zawierać dowolne
serializowalne obiekty.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/picklefield
%{py_sitescriptdir}/django_picklefield-%{version}-*.egg-info
