%define __noautoreq /bin/ksh

Name:		mstone
Version:	4.9.4
Release:	5
Summary:	Mail protocols benchmark framework
License:	GPL
Group:		Networking/Other
URL:		http://mstone.sourceforge.net/
Source:     http://downloads.sourceforge.net/mstone/mstone+docs-%{version}.tar.gz
BuildRequires: cmake

%description
Mstone is a multi-protocol stress and performance measurement tool. Mstone can
test multiple protocols (e.g. POP and SMTP) simultaneously and measures the
performance of every transaction. The performance can be graphed throughout the
duration of the test. 

%prep
%setup -q
find . -type f -exec chmod a+r {} \;

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

%files
%doc INSTALL.txt LICENSE  LICENSE.npl NEWS.txt README.txt doc/*
%{_bindir}/mailclient
%{_bindir}/getdist
%{_datadir}/mstone
%config(noreplace) %{_sysconfdir}/mstone



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 4.9.4-4mdv2011.0
+ Revision: 620412
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 4.9.4-3mdv2010.0
+ Revision: 430109
- rebuild

* Thu Sep 18 2008 Guillaume Rousse <guillomovitch@mandriva.org> 4.9.4-2mdv2009.0
+ Revision: 285751
- skip ksh dependencies

* Thu Sep 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 4.9.4-1mdv2009.0
+ Revision: 283928
- import mstone


* Thu Sep 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 4.9.4-1mdv2009.0
- first mdv release

* Fri Dec 14 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.2-0.%%{rc}.1mdv2008.1
- first mdv release
