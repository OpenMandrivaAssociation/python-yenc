Name:           python-yenc
Version:        0.4.0
Release:        1
Summary:        yEnc Module for Python
Group:          Development/Python
License:        GPLv2+
URL:            http://www.hellanzb.com/trac/
Source0:        https://bitbucket.org/dual75/yenc/get/0.4.0.tar.gz
BuildRequires:  python-devel
BuildRequires:  python-setuptools

%description
python-yenc is a yEnc decoding library for Python. yEnc is a
binary-to-text encoding scheme for transferring binary files
in messages on Usenet or via e-mail.

%prep
%setup -q -n yenc-%{version}


%build
CFLAGS="%{optflags}" %{__python} -c 'import setuptools; execfile("setup.py")' build


%install
%{__python} -c 'import setuptools; execfile("setup.py")' install -O1 --skip-build --root %{buildroot}
chmod g-w %{buildroot}/%{py_platsitedir}/_yenc.so


%check
PYTHONPATH="$PYTHONPATH:%{buildroot}/%{py_platsitedir}" %{__python} test/test.py


%clean


%files
%defattr(-,root,root,-)
%doc README TODO COPYING
%{py_platsitedir}/*


%changelog
* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.3-2mdv2010.0
+ Revision: 442550
- rebuild

* Thu Mar 05 2009 Jérôme Soyer <saispo@mandriva.org> 0.3-1mdv2009.1
+ Revision: 348964
- import python-yenc



