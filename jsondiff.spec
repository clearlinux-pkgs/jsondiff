#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jsondiff
Version  : 1.1.2
Release  : 3
URL      : https://files.pythonhosted.org/packages/33/0c/ddb17571e061c655871ccbf76cdada55a31569327d21517de779d4887241/jsondiff-1.1.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/33/0c/ddb17571e061c655871ccbf76cdada55a31569327d21517de779d4887241/jsondiff-1.1.2.tar.gz
Summary  : Diff JSON and JSON-like structures in Python
Group    : Development/Tools
License  : MIT
Requires: jsondiff-bin = %{version}-%{release}
Requires: jsondiff-license = %{version}-%{release}
Requires: jsondiff-python = %{version}-%{release}
Requires: jsondiff-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
jsondiff
========
Diff JSON and JSON-like structures in Python.
Installation
------------

%package bin
Summary: bin components for the jsondiff package.
Group: Binaries
Requires: jsondiff-license = %{version}-%{release}

%description bin
bin components for the jsondiff package.


%package license
Summary: license components for the jsondiff package.
Group: Default

%description license
license components for the jsondiff package.


%package python
Summary: python components for the jsondiff package.
Group: Default
Requires: jsondiff-python3 = %{version}-%{release}

%description python
python components for the jsondiff package.


%package python3
Summary: python3 components for the jsondiff package.
Group: Default
Requires: python3-core

%description python3
python3 components for the jsondiff package.


%prep
%setup -q -n jsondiff-1.1.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1547490787
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/jsondiff
cp LICENSE %{buildroot}/usr/share/package-licenses/jsondiff/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jsondiff

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/jsondiff/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
