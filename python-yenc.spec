Name:           python-yenc
Version:        0.3
Release:        %mkrel 2
Summary:        yEnc Module for Python
Group:          Development/Python
License:        GPLv2+
URL:            http://www.hellanzb.com/trac/
Source0:        http://www.hellanzb.com/hellanzb-content/yenc-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  python-devel
BuildRequires:  python-setuptools

%description
python-yenc is a yEnc decoding library for Python. yEnc is a
binary-to-text encoding scheme for transferring binary files
in messages on Usenet or via e-mail.

%prep
%setup -q -n yenc-%{version}


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} -c 'import setuptools; execfile("setup.py")' build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} -c 'import setuptools; execfile("setup.py")' install -O1 --skip-build --root $RPM_BUILD_ROOT
chmod g-w $RPM_BUILD_ROOT/%{python_sitearch}/_yenc.so


%check
PYTHONPATH="$PYTHONPATH:$RPM_BUILD_ROOT/%{python_sitearch}" %{__python} test/test.py


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README TODO COPYING
%{py_platsitedir}/*
