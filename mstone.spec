%define name	mstone
%define version 4.9.4
%define release %mkrel 4

%define _requires_exceptions /bin/ksh

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Mail protocols benchmark framework
License:	GPL
Group:		Networking/Other
URL:		http://mstone.sourceforge.net/
Source:     http://downloads.sourceforge.net/mstone/mstone+docs-%{version}.tar.gz
BuildRequires: cmake
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Mstone is a multi-protocol stress and performance measurement tool. Mstone can
test multiple protocols (e.g. POP and SMTP) simultaneously and measures the
performance of every transaction. The performance can be graphed throughout the
duration of the test. 

%prep
%setup -q

%build
%cmake 
%make

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_sysconfdir}/%{name}
install -d -m 755 %{buildroot}%{_datadir}/%{name}/{bin,data}

install -m 755 build/src/mailclient %{buildroot}%{_bindir}
install -m 755 build/src/getdist %{buildroot}%{_bindir}
install -m 755 process mstone %{buildroot}%{_datadir}/%{name}
install -m 755 bin/* %{buildroot}%{_datadir}/%{name}/bin
install -m 644 data/* %{buildroot}%{_datadir}/%{name}/data
install -m 644 conf/* %{buildroot}%{_sysconfdir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc INSTALL.txt LICENSE  LICENSE.npl NEWS.txt README.txt doc/*
%{_bindir}/mailclient
%{_bindir}/getdist
%{_datadir}/mstone
%config(noreplace) %{_sysconfdir}/mstone

