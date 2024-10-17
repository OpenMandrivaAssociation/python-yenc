%define tag ee6b73a5b14f

Name:           python-yenc
Version:        0.4.0
Release:        2
Summary:        yEnc Module for Python
Group:          Development/Python
License:        GPLv2+
URL:            https://www.hellanzb.com/trac/
Source0:        https://bitbucket.org/dual75/yenc/get/0.4.0.tar.gz
BuildRequires:  python-devel
BuildRequires:  python-distribute

%description
python-yenc is a yEnc decoding library for Python. yEnc is a
binary-to-text encoding scheme for transferring binary files
in messages on Usenet or via e-mail.

%prep
%setup -q -n dual75-yenc-%{tag}


%build
CFLAGS="%{optflags}" %{__python} -c 'import setuptools; execfile("setup.py")' build


%install
%{__python} -c 'import setuptools; execfile("setup.py")' install -O1 --skip-build --root %{buildroot}
chmod g-w %{buildroot}/%{py_platsitedir}/_yenc.so


%check
PYTHONPATH="$PYTHONPATH:%{buildroot}/%{py_platsitedir}" %{__python} test/test.py


%clean


%files
%doc README TODO COPYING
%{py_platsitedir}/*

