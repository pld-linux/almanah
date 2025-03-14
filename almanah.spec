#
# Conditional build:
%bcond_without	evolution	# Evolution calendar integration
%bcond_without	gtkspell	# GtkSpell spell checking

Summary:	Almanah Diary - keep a personal diary
Summary(pl.UTF-8):	Almanah Diary - osobisty pamiętnik
Name:		almanah
Version:	0.12.4
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/almanah/0.12/%{name}-%{version}.tar.xz
# Source0-md5:	b5d0e39c4f45bf8adfb53bd44461871c
URL:		https://wiki.gnome.org/Apps/Almanah_Diary
BuildRequires:	AppStream
BuildRequires:	atk-devel
BuildRequires:	cairo-devel
%{?with_evolution:BuildRequires:	evolution-data-server-devel >= 3.33.2}
BuildRequires:	gettext-tools
BuildRequires:	gcr4-devel >= 4
BuildRequires:	glib2-devel >= 1:2.68
BuildRequires:	gpgme-devel >= 1.0.0
BuildRequires:	gtk+3-devel >= 3.15
BuildRequires:	gtksourceview4-devel >= 4.0
%{?with_gtkspell:BuildRequires:	gtkspell3-devel >= 3.0}
BuildRequires:	libcryptui-devel
BuildRequires:	meson >= 0.59
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	sqlite3-devel >= 3
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.68
%{?with_evolution:Requires:	evolution-data-server >= 3.33.2}
Requires:	glib2 >= 1:2.68
Requires:	gpgme >= 1.0.0
Requires:	gtk+3 >= 3.15
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Almanah is a small GTK+ application to allow you to keep a diary of
your life.

%description -l pl.UTF-8
Almanah to mała aplikacja GTK+ pozwalająca prowadzić własny
pamiętnik.

%prep
%setup -q

%build
%meson \
	%{!?with_evolution:-Devolution=disabled} \
	%{!?with_gtkspell:-Dspell_checking=disabled}

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS NEWS.md README.md
%attr(755,root,root) %{_bindir}/almanah
%{_datadir}/glib-2.0/schemas/org.gnome.almanah.gschema.xml
%{_datadir}/metainfo/org.gnome.Almanah.metainfo.xml
%{_desktopdir}/org.gnome.Almanah.desktop
%{_iconsdir}/hicolor/*x*/apps/org.gnome.Almanah.png
%{_iconsdir}/hicolor/scalable/actions/org.gnome.Almanah-tags-symbolic.svg
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Almanah-symbolic.svg
