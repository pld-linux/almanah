#
# Conditional build:
%bcond_without	evolution	# Evolution calendar integration
%bcond_without	gtkspell	# GtkSpell spell checking

Summary:	Almanah Diary - keep a personal diary
Summary(pl.UTF-8):	Almanah Diary - osobisty pamiętnik
Name:		almanah
Version:	0.12.3
Release:	2
License:	GPL v3+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/almanah/0.12/%{name}-%{version}.tar.xz
# Source0-md5:	b4d6023342f49e23435e06fd54d7fa4c
URL:		https://wiki.gnome.org/Apps/Almanah_Diary
BuildRequires:	appstream-glib
BuildRequires:	atk-devel
BuildRequires:	cairo-devel
%{?with_evolution:BuildRequires:	evolution-data-server-devel >= 3.33.2}
BuildRequires:	gettext-tools
BuildRequires:	gcr-devel >= 3
BuildRequires:	glib2-devel >= 1:2.32
BuildRequires:	gpgme-devel >= 1.0.0
BuildRequires:	gtk+3-devel >= 3.15
BuildRequires:	gtksourceview3-devel >= 3.0
%{?with_gtkspell:BuildRequires:	gtkspell3-devel >= 3.0}
BuildRequires:	libcryptui-devel
BuildRequires:	meson >= 0.51
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	sqlite3-devel >= 3
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.32
%{?with_evolution:Requires:	evolution-data-server >= 3.33.2}
Requires:	glib2 >= 1:2.32
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
%meson build \
	%{!?with_evolution:-Devolution=false} \
	%{!?with_gtkspell:-Dspell_checking=false}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

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
%doc AUTHORS MAINTAINERS NEWS README.md
%attr(755,root,root) %{_bindir}/almanah
%{_datadir}/GConf/gsettings/almanah.convert
%{_datadir}/glib-2.0/schemas/org.gnome.almanah.gschema.xml
%{_datadir}/metainfo/almanah.appdata.xml
%{_desktopdir}/almanah.desktop
%{_iconsdir}/hicolor/*x*/apps/almanah.png
%{_iconsdir}/hicolor/scalable/actions/almanah-tags-symbolic.svg
%{_iconsdir}/hicolor/scalable/apps/almanah-symbolic.svg
