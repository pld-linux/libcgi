Summary:	CGI applications in C library
Summary(pl.UTF-8):	Biblioteka C dla aplikacji CGI
Name:		libcgi
Version:	1.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libcgi/%{name}-%{version}.tar.gz
# Source0-md5:	110af367081d33c7ed6527a1a60fc274
URL:		http://libcgi.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LibCGI is a library written from scratch to easily make CGI
applications in C. There are a lot of functions like string
manipulation, session and cookie support, GET and POST methods
manipulation etc., to help you to quickly write powerful CGI programs.

%description -l pl.UTF-8
LibCGI to napisana od zera bibioteka do łatwego tworzenia aplikacji
CGI w C. Zawiera wiele funkcji do operacji na łańcuchach znaków,
obsługi sesji i ciasteczek, metod GET i POST itp.

%package devel
Summary:	Header files for libcgi library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libcgi
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libcgi library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libcgi.

%package static
Summary:	Static libcgi library
Summary(pl.UTF-8):	Statyczna biblioteka libcgi
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libcgi library.

%description static -l pl.UTF-8
Statyczna biblioteka libcgi.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make} \
	CC="%{__cc}" \
	FLAGS="%{rpmcflags} -Wall -fpic" \
	CFLAGS="%{rpmcflags} -Wall -fpic"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir},%{_mandir}/man3}

%{__make} install \
	LIBDIR=$RPM_BUILD_ROOT%{_libdir} \
	INCDIR=$RPM_BUILD_ROOT%{_includedir}

install doc/man/man3/libcgi*.3 $RPM_BUILD_ROOT%{_mandir}/man3

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog README THANKS TODO
%attr(755,root,root) %{_libdir}/libcgi.so

%files devel
%defattr(644,root,root,755)
%doc examples/*
%{_includedir}/cgi.h
%{_includedir}/session.h
%{_mandir}/man3/libcgi_*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libcgi.a
