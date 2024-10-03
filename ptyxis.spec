# TODO: use gtk4-update-icon-cache
Summary:	Ptyxis - a container oriented terminal
Summary(pl.UTF-8):	Ptyxis - terminal zorientowany na kontenery
Name:		ptyxis
Version:	47.1
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/ptyxis/47/%{name}-%{version}.tar.xz
# Source0-md5:	13b3d2160c35c36b7168285f061e090a
URL:		https://gitlab.gnome.org/chergert/ptyxis
BuildRequires:	glib2-devel >= 1:2.80
BuildRequires:	gtk4-devel >= 4.14
BuildRequires:	json-glib-devel >= 1.6
BuildRequires:	libadwaita-devel >= 1.6
BuildRequires:	libportal-gtk4-devel
BuildRequires:	meson >= 0.64.0
BuildRequires:	ninja >= 1.5
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	vte-gtk4-devel >= 0.77
BuildRequires:	xz
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib2 >= 1:2.80
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.80
Requires:	gtk4 >= 4.14
Requires:	hicolor-icon-theme
Requires:	json-glib >= 1.6
Requires:	libadwaita >= 1.6
Requires:	vte-gtk4 >= 0.77
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ptyxis is a terminal which attempts to simplify what it means to be a
terminal in the age of operating systems which are themselves
containers.

%description -l pl.UTF-8
Ptyxis to terminal, który próbuje uprościć znaczenie terminala w erze
systemów operacyjnych będących kontenerami.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database
%update_icon_cache hicolor
%glib_compile_schemas

%postun
%update_desktop_database
%update_icon_cache hicolor
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_bindir}/ptyxis
%attr(755,root,root) %{_libexecdir}/ptyxis-agent
%{_datadir}/dbus-1/services/org.gnome.Ptyxis.service
%{_datadir}/glib-2.0/schemas/org.gnome.Ptyxis.gschema.xml
%{_datadir}/metainfo/org.gnome.Ptyxis.metainfo.xml
%{_desktopdir}/org.gnome.Ptyxis.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Ptyxis.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Ptyxis-symbolic.svg
%{_mandir}/man1/ptyxis.1*
