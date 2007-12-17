%define name    cvsutils
%define version 0.2.3
%define release %mkrel 1

%define Summary Collection of useful CVS scripts

Summary:        %Summary
Name:           %name
Version:        %version
Release:        %release
License:        GPL
Group:          Development/Other
URL:            http://www.red-bean.com/cvsutils/
Source0:        http://www.red-bean.com/cvsutils/releases/%name-%version.tar.bz2
BuildArch:      noarch

%description
CVS Utilities is a collection of scripts, mostly in the Perl language,
that allow you to manage the files in the CVS working directory.
You can tell which files are under version control and which are
not without even being online. You can erase or move away all derived
files in seconds.


%prep
%setup -q


%build
%configure
%make


%install
rm -rf %buildroot
%makeinstall


%clean
rm -rf %buildroot


%files
%defattr(0755,root,root,0755)
%_bindir/*
%defattr(0644,root,root,0755)
%_mandir/man1/%name.1*
%doc AUTHORS TODO COPYING ChangeLog NEWS README THANKS
