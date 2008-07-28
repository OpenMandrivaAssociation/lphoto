%define name lphoto
%define ver 1.0.69
%define rel %mkrel 3
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

Summary: 	Lphoto photo album
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
BuildRequires:  ImageMagick
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
