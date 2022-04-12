#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x70FE17F8A643E15B (lukasa@keybase.io)
#
Name     : pypi-certifi
Version  : 2021.10.8
Release  : 86
URL      : https://files.pythonhosted.org/packages/6c/ae/d26450834f0acc9e3d1f74508da6df1551ceab6c2ce0766a593362d6d57f/certifi-2021.10.8.tar.gz
Source0  : https://files.pythonhosted.org/packages/6c/ae/d26450834f0acc9e3d1f74508da6df1551ceab6c2ce0766a593362d6d57f/certifi-2021.10.8.tar.gz
Source1  : https://files.pythonhosted.org/packages/6c/ae/d26450834f0acc9e3d1f74508da6df1551ceab6c2ce0766a593362d6d57f/certifi-2021.10.8.tar.gz.asc
Summary  : Python package for providing Mozilla's CA Bundle.
Group    : Development/Tools
License  : MPL-2.0
Requires: pypi-certifi-python = %{version}-%{release}
Requires: pypi-certifi-python3 = %{version}-%{release}
Requires: ca-certs
BuildRequires : buildreq-distutils3
Patch1: 0001-Use-unified-trust-store.patch

%description
================================
        
        `Certifi`_ provides Mozilla's carefully curated collection of Root Certificates for
        validating the trustworthiness of SSL certificates while verifying the identity
        of TLS hosts. It has been extracted from the `Requests`_ project.
        
        Installation
        ------------

%package python
Summary: python components for the pypi-certifi package.
Group: Default
Requires: pypi-certifi-python3 = %{version}-%{release}

%description python
python components for the pypi-certifi package.


%package python3
Summary: python3 components for the pypi-certifi package.
Group: Default
Requires: python3-core
Provides: pypi(certifi)

%description python3
python3 components for the pypi-certifi package.


%prep
%setup -q -n certifi-2021.10.8
cd %{_builddir}/certifi-2021.10.8
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649725566
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
