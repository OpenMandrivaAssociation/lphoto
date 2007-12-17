%define name lphoto
%define ver 1.0.13
%define rel %mkrel 3
%define extraver -0.0.0.45.lindows0.1
%define pyver %(python -V 2>&1 | cut -f2 -d" " | cut -f1,2 -d".")

%define have_pre %(echo %ver|awk '{p=0} /[a-z,A-Z][a-z,A-Z]/ {p=1} {print p}')
%if %have_pre
%define version %(perl -e '$name="%ver"; print ($name =~ /(.*?)[a-z]/);')
%define release %mkrel 3
%else
%define version %ver
%define release %mkrel 3
%endif

Summary: 	Lphoto photo album
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
# http://www.linspire.com/lindows_products_details.php?id=12424&pg=specs
Source0: 	http://software.lindows.com/emptypool//lindowsos/pool/main/l/lphoto/%{name}_%{ver}%{extraver}.tar.bz2
License:	GPL
Group: 		Graphics
Prefix: 	%{_prefix}
Url: 		http://www.linspire.com/lphoto
BuildRequires:	python-devel 
BuildRequires:  ImageMagick
BuildRequires:  PyQt
Requires:	PyQt

%description
LPhoto Photo Album

%prep
%setup -q -n %{name}-%ver

%build

%install
python install.py -i %{buildroot} -b %{_bindir}

mkdir -p %{buildroot}/{%{_menudir},%{_miconsdir},%{_liconsdir}}
convert -resize 16x16 %{name}.png %{buildroot}/%{_miconsdir}/%{name}.png
convert -resize 32x32 %{name}.png %{buildroot}/%{_iconsdir}/%{name}.png
install %{name}.png %{buildroot}/%{_liconsdir}/%{name}.png
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat > %{buildroot}/%{_menudir}/%{name} << EOF
?package(%{name}):\
command="%{_bindir}/%{name}" \
needs="x11" \
icon="%{name}.png" \
section="Multimedia/Graphics" \
title="LPhoto" \
longtitle="LPhoto photo album"
EOF

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_libdir}/python%{pyver}/site-packages/*
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_menudir}/%{name}
%doc LICENSE.GPL

