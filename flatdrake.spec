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

%changelog
*Tue Apr 25 2023 Astragalo <mauro.carbini@gmail.com> 1.0.0-mib1
-Modificato controllo uscita ora con btnclose non chiede conferma
-Correzioni tooltip

*Mon Apr 24 2023 Astragalo <mauro.carbini@gmail.com> 1.0.0-mib2
-Modificata la gestione dell'immagine

*Sun Apr 23 2023 Astragalo <mauro.carbini@gmail.com> 1.0.0-mib1
-Prima release pubblica
-Aggiunte tooltip
-Aggiunta creazione di file temporaneo per ricerca su dnfdrake
-Aggiunta funzione che deseleziona all da update se si seleziona un'app specifica da aggiornare

*Thu Apr 06 2023 Astragalo <mauro.carbini@gmail.com> 0.99.6-mib1
-Aggiunta funzione di ricerca su flathub
-Aggiunta spunta sul pulsante update di default aggiorna tutto
-Aggiunta funzione di conferma uscita
-Correzioni varie

*Sun Apr 02 2023 Astragalo <mauro.carbini@gmail.com> 0.99.5-mib1
-Aggiunta verifica app presente in repo rpm
-Correzioni varie

*Thu Mar 23 2023 Astragalo <mauro.carbini@gmail.com> 0.99.1-mib1
-Aggiunto caricamento flathub all'avvio
-Correzioni varie

*Tue Mar 21 2023 Astragalo <mauro.carbini@gmail.com> 0.99.0-mib1
-Initial Build for Rosa and OpenMandriva Rome (MIB)


