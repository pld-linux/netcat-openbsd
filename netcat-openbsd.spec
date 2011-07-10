Summary:	Versatile network test and debugging tool
Summary(es.UTF-8):	Herramienta de prueba e depuración para servicios de red
Summary(pl.UTF-8):	Proste narzędzie do testowania sieci
Summary(pt_BR.UTF-8):	Ferramenta de teste e depuração para serviços de rede
Name:		netcat-openbsd
Version:	1.89
Release:	2
License:	Public Domain
Group:		Networking/Utilities
Source0:	http://ftp.de.debian.org/debian/pool/main/n/%{name}/%{name}_%{version}.orig.tar.gz
# Source0-md5:	7238ce15aae43069e96ba7faf03f153e
# http://cdn.debian.net/debian/pool/main/n/%{name}/%{name}_%{version}-4.diff.gz
Patch0:		%{name}_%{version}-4.diff
URL:		http://packages.debian.org/sid/netcat-openbsd
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
%setup -q -n %{name}-%{version}.orig
%patch0 -p1

# taken from arch linux
for i in `cat debian/patches/series`
	do
		echo "** patch $i" 1>&2
		cat "debian/patches/$i"
	done | patch -p1

%build
%{__make} CFLAGS="%{rpmcflags} -DDEBIAN_VERSION=\"\""

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
