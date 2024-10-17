%define	name	cvsutils
%define	version	0.2.5
%define release	3
%define	Summary	Collection of useful CVS scripts

Summary:	%Summary
Name:		%name
Version:	0.2.6
Release:	1%release
License:	GPLv2+
Group:		Development/Other
URL:		https://www.red-bean.com/cvsutils/
Source0:	http://www.red-bean.com/cvsutils/releases/%name-%version.tar.gz
BuildRoot:	%_tmppath/%name-buildroot
BuildArch:	noarch

%description
CVS Utilities is a collection of scripts, mostly in the Perl language,
that allow you to manage the files in the CVS working directory.
You can tell which files are under version control and which are
not without even being online. You can erase or move away all derived
files in seconds.


%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(0755,root,root,0755)
%_bindir/*
%defattr(0644,root,root,0755)
%_mandir/man1/%name.1*
%doc AUTHORS COPYING ChangeLog NEWS README THANKS


%changelog
* Sun Aug 22 2010 Funda Wang <fwang@mandriva.org> 0.2.5-2mdv2011.0
+ Revision: 571885
- use configure2_5x

  + Sandro Cazzaniga <kharec@mandriva.org>
    - just clean spec and fix rpmlints warning on spec

* Tue Jun 09 2009 Jérôme Brenier <incubusss@mandriva.org> 0.2.5-2mdv2010.0
+ Revision: 384557
- fix license (GPLv2+)

* Sat Sep 06 2008 Emmanuel Andry <eandry@mandriva.org> 0.2.5-1mdv2009.0
+ Revision: 281912
- New version
- fix license

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.2.3-3mdv2009.0
+ Revision: 243840
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.2.3-1mdv2008.1
+ Revision: 140717
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 16 2007 Pascal Terjan <pterjan@mandriva.org> 0.2.3-1mdv2008.0
+ Revision: 64233
- Import cvsutils



* Wed Aug 17 2005 Nicolas L�cureuil <neoclust@mandriva.org> 0.2.3-1mdk
- New release 0.2.3

* Mon Nov 08 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.2.1-1mdk
- 0.2.1

* Sat Sep 27 2003 Han Boetes <han@linux-mandrake.com> 0.2.0-1mdk
- Initial Mandrake release; I actually copied the OpenBSD port, thanks
  Anil Madhavapeddy <avsm@openbsd.org>
