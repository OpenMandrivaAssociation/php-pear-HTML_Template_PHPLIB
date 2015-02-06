%define		_class		HTML
%define		_subclass	Template
%define		upstream_name	%{_class}_%{_subclass}_PHPLIB

Name:		php-pear-%{upstream_name}
Version:	1.5.0
Release:	7
Summary:	Preg_* based template system
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/HTML_Template_PHPLIB/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
The popular Template system from PHPLIB ported to PEAR.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/examples
%{_bindir}/html_template_phplibtool
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.5.0-5mdv2012.0
+ Revision: 742005
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.5.0-4
+ Revision: 679356
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.5.0-3mdv2011.0
+ Revision: 613682
- the mass rebuild of 2010.1 packages

* Sat Dec 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.5.0-2mdv2010.1
+ Revision: 477888
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Mon Sep 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.5.0-1mdv2010.0
+ Revision: 446477
- update to new version 1.5.0

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.4.0-3mdv2010.0
+ Revision: 441181
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.4.0-2mdv2009.1
+ Revision: 322123
- rebuild

* Sun Oct 12 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.4.0-1mdv2009.1
+ Revision: 292881
- update to new version 1.4.0

* Tue Sep 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.3-1mdv2009.0
+ Revision: 278921
- update to new version 1.3.3

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.3.2-2mdv2009.0
+ Revision: 236882
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Apr 28 2007 Oden Eriksson <oeriksson@mandriva.com> 1.3.2-1mdv2008.0
+ Revision: 18950
- fix build
- remove unneded P0
- 1.3.2


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.3.1-9mdv2007.0
+ Revision: 81696
- Import php-pear-HTML_Template_PHPLIB

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.3.1-9mdk
- new group (Development/PHP)

* Mon Nov 07 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.3.1-8mdk
- Fix BuildRequires

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3.1-7mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3.1-6mdk
- rebuilt to use new pear auto deps/reqs from pld

* Thu Aug 04 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3.1-5mdk
- fix a xml formatting error

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3.1-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3.1-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3.1-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3.1-1mdk
- initial Mandriva package (PLD import)

