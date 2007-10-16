Name: x11-driver-video-sunleo
Version: 1.1.0
Release: %mkrel 3
Summary: The X.org driver for sun leo Cards
Group: Development/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-sunleo-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-server < 7.0

%description
The X.org driver for sun leo Cards

%prep
%setup -q -n xf86-video-sunleo-%{version}

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/xorg/modules/drivers/sunleo_drv.la
%{_libdir}/xorg/modules/drivers/sunleo_drv.so
%{_mandir}/man4/sunleo.*
