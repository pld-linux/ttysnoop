Summary:	Program to snoop on a TTY through another
Summary(pl):	Program s³u¿±cy do kontrolowania jednej konsoli za pomoc± innej
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

%description -l pl
Pakiet ten pozwala na podgl±danie i kontrolowanie loginowych tty
poprzez inne urz±dzenie tego typu lub pseudo-tty. Urz±dzenie
kontroluj±ce stajê siê klonem pierwotnego tty, przekierowuj±c strumieñ
wej¶cia/wyj¶cia do niej.

%prep
%setup -q
%patch -p1

%build
%{__make} OPT="%{rpmcflags}"

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
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/snooptab
%attr(755,root,root) %{_sbindir}/*
%attr(700,root,root) %dir %{_var}/spool/%{name}
%{_mandir}/man8/*
