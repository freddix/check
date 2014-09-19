Summary:	Check - unit testing framework for C
Name:		check
Version:	0.9.14
Release:	1
License:	LGPL v2.1+
Group:		Development/Libraries
Source0:	http://download.sourceforge.net/check/%{name}-%{version}.tar.gz
# Source0-md5:	38263d115d784c17aa3b959ce94be8b8
Patch0:		%{name}-am.patch
URL:		http://check.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Check is a unit test framework for C. It features a simple interface
for defining unit tests, putting little in the way of the developer.
Tests are run in a separate address space, so Check can catch both
assertion failures and code errors that cause segmentation faults or
other signals. The output from unit tests can be used within source
code editors and IDEs.

%package devel
Summary:        Development files for check
Group:          Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for check.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__automake}
%{__autoconf}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/doc/check
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog* NEWS README
%attr(755,root,root) %{_bindir}/checkmk
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_mandir}/man1/checkmk.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_aclocaldir}/check.m4
%{_includedir}/*.h
%{_pkgconfigdir}/check.pc

