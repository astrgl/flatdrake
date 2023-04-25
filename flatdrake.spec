Name: flatdrake
Version: 1.0.0
Release: 1
Packager: Astragalo
License: GPL
Group: Graphical desktop/KDE
Summary: FlatDrake  is a frontend for FlatPak
Url: https://mib.pianetalinux.org/
Source: %{name}-%{version}.tar.gz

Requires: flatpak
Requires: gambas3-runtime
Requires: gambas3-gb-form
Requires: gambas3-gb-image
Requires: gambas3-gb-gui
Requires: gambas3-gb-qt5
Requires: gambas3-gb-gtk3
Requires: gambas3-gb-dbus
Requires: gambas3-gb-form-stock
Requires: hicolor-icon-theme
Requires: lsb-release
Requires: xrandr
BuildArch: noarch

Conflicts:  gambas3-runtime  > 3.18.1

%description
FlatDrake  is a frontend for FlatPak
Powerful like a terminal and simple like a GUI!

%prep
%autosetup -n flatdrake

%install

install -Dm 755 flatdrake.gambas -t %{buildroot}/%{_bindir}/
install -Dm 755 flatdrake.desktop -t %buildroot/%_datadir/applications/
install -Dm 644 license -t %{buildroot}/%{_datadir}/flatdrake/
install -Dm 644 flatdrake-* -t %{buildroot}/%{_datadir}/flatdrake/
install -Dm 644 *.png -t %{buildroot}/%{_datadir}/flatdrake/
install -Dm 644 flatdrake.svg  -t %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/

%files
%{_bindir}/flatdrake.gambas
%{_datadir}/applications/flatdrake.desktop
%{_datadir}/icons/hicolor/32x32/apps/flatdrake.svg
%{_datadir}/flatdrake/license
%{_datadir}/flatdrake/flatdrake-*
%{_datadir}/flatdrake/*.png
