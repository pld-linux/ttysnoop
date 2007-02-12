Summary:	Program to snoop on a TTY through another
Summary(pl.UTF-8):	Program służący do kontrolowania jednej konsoli za pomocą innej
Name:		ttysnoop
Version:	0.12c
Release:	11
License:	distributable
Group:		Applications/Terminal
Source0:	ftp://sunsite.unc.edu/pub/Linux/utils/terminal/%{name}-%{version}.tar.gz
# Source0-md5:	85ba8fcac7b1a3a103fe632eef26a92d
Patch0:		%{name}-%{version}-glibc.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
The package allows you to snoop on login tty's through another
tty-device or pseudo-tty. The snoop-tty becomes a 'clone' of the
original tty, redirecting both input and output from/to it.

%description -l pl.UTF-8
Pakiet ten pozwala na podglądanie i kontrolowanie loginowych tty
poprzez inne urządzenie tego typu lub pseudo-tty. Urządzenie
kontrolujące staje się klonem pierwotnego tty, przekierowując strumień
wejścia/wyjścia do niego.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_sbindir},%{_mandir}/man8} \
	$RPM_BUILD_ROOT%{_var}/spool/%{name}

install ttysnoop{,s}	$RPM_BUILD_ROOT%{_sbindir}
install ttysnoop.8	$RPM_BUILD_ROOT%{_mandir}/man8
echo ".so ttysnoop.8" > $RPM_BUILD_ROOT%{_mandir}/man8/ttysnoops.8
install snooptab.dist	$RPM_BUILD_ROOT%{_sysconfdir}/snooptab

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/snooptab
%attr(755,root,root) %{_sbindir}/*
%attr(700,root,root) %dir %{_var}/spool/%{name}
%{_mandir}/man8/*
