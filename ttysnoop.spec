Summary:	Program to snoop on a TTY through another
Summary(pl):	Program s³u¿acy do snoopowania jednej konsoli za pomoc± drugiej
Name:		ttysnoop 
Version:	0.12c 
Release:	6
Source:		ftp://sunsite.unc.edu:/pub/Linux/utils/terminal/%{name}-%{version}.tar.gz
Patch:		%{name}-%{version}-glibc.patch
Copyright:	distributable
Group:		Utilities/Terminal
Group(pl):	U¿ytki/Terminal
BuildRoot:	/tmp/%{name}-%{version}-root


%description
The package allows you to snoop on login tty's through another tty-device       
or pseudo-tty. The snoop-tty becomes a 'clone' of the original tty,             
redirecting both input and output from/to it.

%prep
%setup -q
%patch -p1

%build
make "RPM_OPTS=$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc,sbin,usr/share/man/man8}

install -s ttysnoop{,s} $RPM_BUILD_ROOT/sbin
install ttysnoop.8 $RPM_BUILD_ROOT/usr/share/man/man8
install snooptab.dist $RPM_BUILD_ROOT/etc/snooptab

gzip -9nf   $RPM_BUILD_ROOT/usr/share/man/man8/*
gzip -9nf   README

%files
%defattr(644,root,root,755)

%config /etc/snooptab
%doc README.gz 

%attr(755,root,root) /sbin/ttysnoop
%attr(755,root,root) /sbin/ttysnoops
/usr/share/man/man8/ttysnoop.8.gz
