Summary:	Program to snoop on a TTY through another
Summary(pl):	Program s³u¿acy do kontrolowania jednej konsoli za pomoc± innej
Name:		ttysnoop 
Version:	0.12c 
Release:	7
Source:		ftp://sunsite.unc.edu/pub/Linux/utils/terminal/%{name}-%{version}.tar.gz
Patch:		%{name}-%{version}-glibc.patch
Copyright:	distributable
Group:		Utilities/Terminal
Group(pl):	U¿ytki/Terminal
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_sbindir	/sbin
%define		_sysconfidir	/etc

%description
The package allows you to snoop on login tty's through another tty-device or
pseudo-tty. The snoop-tty becomes a 'clone' of the original tty, redirecting
both input and output from/to it.

%description -l pl
Pakiet ten pozwala na podgl±danie i kontrolowanie loginowych tty poprzez inne
urz±dzenie tego typu lub pseudo-tty. Urz±dzenie kontroluj±ce stajê siê klonem
pierwotnego tty, przekierowuj±c strumieñ wej¶cia/wyj¶cia do niej. 

%prep
%setup -q
%patch -p1

%build
make OPT="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_sysconfidir}
install -d $RPM_BUILD_ROOT/%{_sbindir}
install -d $RPM_BUILD_ROOT/%{_mandir}/man8
install -d $RPM_BUILD_ROOT/%{_var}/spool/%{name}

install -s ttysnoop{,s}	$RPM_BUILD_ROOT%{_sbindir}
install ttysnoop.8	$RPM_BUILD_ROOT%{_mandir}/man8
echo ".so ttysnoop.8" > $RPM_BUILD_ROOT%{_mandir}/man8/ttysnoops.8
install snooptab.dist	$RPM_BUILD_ROOT%{_sysconfidir}/snooptab

gzip -9nf  $RPM_BUILD_ROOT%{_mandir}/man8/* \
	README

%files
%defattr(644,root,root,755)
%doc README.gz 
%attr(640,root,root) %config(noreplace) %{_sysconfidir}/snooptab
%attr(755,root,root) %{_sbindir}/*
%attr(700,root,root) %dir %{_var}/spool/%{name}
%{_mandir}/man8/*
