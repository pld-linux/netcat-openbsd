Summary:	Versatile network test and debugging tool
Summary(es.UTF-8):	Herramienta de prueba e depuración para servicios de red
Summary(pl.UTF-8):	Proste narzędzie do testowania sieci
Summary(pt_BR.UTF-8):	Ferramenta de teste e depuração para serviços de rede
Name:		netcat-openbsd
Version:	1.234
Release:	1
License:	ISC
Group:		Networking/Utilities
Source0:	https://deb.debian.org/debian/pool/main/n/%{name}/%{name}_%{version}.orig.tar.gz
# Source0-md5:	c3906f02d5a070afd8ac23ec983fc746
# Patches from Debian netcat-openbsd 1.234-2
Patch0:		port-to-linux-with-libbsd.patch
Patch1:		build-without-TLS-support.patch
Patch2:		connect-timeout.patch
Patch3:		get-sev-by-name.patch
Patch4:		send-crlf.patch
Patch5:		quit-timer.patch
Patch6:		udp-scan-timeout.patch
Patch7:		dccp-support.patch
Patch8:		broadcast-support.patch
Patch9:		serialized-handling-multiple-clients.patch
Patch10:	set-TCP-MD5SIG-correctly-for-client-connections.patch
Patch11:	destination-port-list.patch
Patch12:	use-flags-to-specify-listen-address.patch
Patch13:	make-getnameinfo-errors-nonfatal-in-report_sock.patch
Patch14:	abstract-unix-domain-socket.patch
Patch15:	misc-failures-and-features.patch
URL:		https://packages.debian.org/sid/netcat-openbsd
BuildRequires:	libbsd-devel
BuildRequires:	pkgconfig
Provides:	nc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Netcat is a simple Unix utility which reads and writes data across
network connections, using TCP or UDP protocol. It is designed to be a
reliable "back-end" tool that can be used directly or easily driven by
other programs and scripts. At the same time, it is a feature-rich
network debugging and exploration tool, since it can create almost any
kind of connection you would need and has several interesting built-in
capabilities. Netcat, or "nc" as the actual program is named, should
have been supplied long ago as another one of those cryptic but
standard Unix tools.

%description -l es.UTF-8
NetCat es un cliente de red mínimo. Puede ser usado para crear
conexiones TCP a puertos arbitrarios y puede simular conexiones sobre
UDP. También puede oír puertos.

%description -l pl.UTF-8
Netcat to proste uniksowe narzędzie, które odbiera i wysyła dane
poprzez połączenia sieciowe protokołami TCP lub UDP. Jest
zaprojektowane jako wiarygodny "back-end", który może być używany
bezpośrednio albo sterowany przez inne programy i skrypty.
Jednocześnie może pomóc w wykrywaniu usterek w sieci albo poznawaniu
jej od środka, ponieważ może stworzyć prawie dowolny rodzaj
połączenia, jaki może być potrzebny, i ma wbudowanych kilka ciekawych
funkcji. Netcat - albo "nc", jak się nazywa właściwy program, powinien
był być dostarczany już dawno temu jako kolejne tajemnicze, ale
standardowe uniksowe narzędzie.

%description -l pt_BR.UTF-8
O NetCat é um cliente de rede mínimo. Pode ser usado para criar
conexões TCP para portas arbitrárias e pode simular conexões sobre
UDP. Também pode receber conexões.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1
%patch -P9 -p1
%patch -P10 -p1
%patch -P11 -p1
%patch -P12 -p1
%patch -P13 -p1
%patch -P14 -p1
%patch -P15 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags}" \
	LDFLAGS="%{rpmldflags}" \
	LIBS="-lbsd -lresolv"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install nc $RPM_BUILD_ROOT%{_bindir}/nc
install nc.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nc
%{_mandir}/man1/*
