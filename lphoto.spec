%define name lphoto
%define ver 1.0.69
%define rel 6
%define extraver -0.0.0.50.linspire2.1
%define pyver %(python -V 2>&1 | cut -f2 -d" " | cut -f1,2 -d".")

%define have_pre %(echo %ver|awk '{p=0} /[a-z,A-Z][a-z,A-Z]/ {p=1} {print p}')
%if %have_pre
%define version %(perl -e '$name="%ver"; print ($name =~ /(.*?)[a-z]/);')
%define release %mkrel %rel
%else
%define version %ver
%define release %mkrel %rel
%endif

Summary: 	Photo album
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
# http://www.linspire.com/lindows_products_details.php?id=12424&pg=specs
Source0: 	http://software.linspire.com/pool-src/l/lphoto/%{name}_%{ver}%{extraver}.tar.gz
License:	GPLv2+
Group: 		Graphics
BuildRoot: 	%{_tmppath}/%{name}-buildroot
Prefix: 	%{_prefix}
Url: 		http://www.linspire.com/lphoto
BuildRequires:	python-devel 
BuildRequires:  imagemagick
BuildRequires:  PyQt
BuildRequires:	desktop-file-utils
Requires:	PyQt

%description
LPhoto Photo Album

%prep
%setup -q -n marlin_build-freespire_lphoto-1.0

%build

%install
python install.py -i %{buildroot} -b %{_bindir}

mkdir -p %{buildroot}/{%{_menudir},%{_miconsdir},%{_liconsdir}}
convert -resize 16x16 %{name}.png %{buildroot}/%{_miconsdir}/%{name}.png
convert -resize 32x32 %{name}.png %{buildroot}/%{_iconsdir}/%{name}.png
install %{name}.png %{buildroot}/%{_liconsdir}/%{name}.png

desktop-file-install --vendor='' \
	--dir %buildroot%_datadir/applications \
	--add-category='Qt' \
	lphoto.desktop

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%python_sitelib/Lphoto
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_datadir}/applications/%{name}.desktop


%changelog
* Sat Nov 13 2010 Bogdano Arendartchuk <bogdano@mandriva.com> 1.0.69-6mdv2011.0
+ Revision: 597040
- rebuild for python 2.7

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.0.69-5mdv2010.0
+ Revision: 439608
- rebuild

* Mon Jan 05 2009 Funda Wang <fwang@mandriva.org> 1.0.69-4mdv2009.1
+ Revision: 324927
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Mon Jul 28 2008 Thierry Vignaud <tv@mandriva.org> 1.0.69-3mdv2009.0mdv2009.0
+ Revision: 251424
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sun Jan 06 2008 Funda Wang <fwang@mandriva.org> 1.0.69-1mdv2008.1mdv2008.1
+ Revision: 145957
- BR desktop-file-utils
- fix libdir
- switch to xdg menu entry
- New version 1.0.69

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import lphoto


* Fri Nov 04 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.0.13-3mdk
- Fix BuildRequires
- %%mkrel

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 1.0.13-2mdk
- Rebuild for new python

* Thu Jun 10 2004 Buchan Milne <bgmilne@linux-mandrake.com> 1.0.13-1mdk
-1.0.13

* Tue Apr 11 2004 Buchan Milne <bgmilne@linux-mandrake.com> 0.11-1mdk
- First Mandrake package
