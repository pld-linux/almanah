Summary:	Almanah Diary - keep a personal diary
Summary(pl.UTF-8):	Almanah Diary - osobisty pamiętnik
Name:		almanah
Version:	0.11.1
Release:	3
License:	GPL v3+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/almanah/0.11/%{name}-%{version}.tar.xz
# Source0-md5:	6107d7becf94548170365f45f8d9dc69
URL:		https://wiki.gnome.org/Apps/Almanah_Diary
BuildRequires:	appstream-glib-devel
BuildRequires:	atk-devel
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.9
BuildRequires:	cairo-devel
BuildRequires:	evolution-data-server-devel >= 3.6
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	gpgme-devel >= 1.0.0
BuildRequires:	gtk+3-devel >= 3.5.6
BuildRequires:	gtkspell3-devel >= 3.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libcryptui-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
BuildRequires:	sqlite3-devel >= 3
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.28.0
Requires:	evolution-data-server >= 3.6
Requires:	glib2 >= 1:2.28.0
Requires:	gpgme >= 1.0.0
Requires:	gtk+3 >= 3.5.6
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
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%doc AUTHORS ChangeLog* MAINTAINERS NEWS README
%attr(755,root,root) %{_bindir}/almanah
%{_datadir}/GConf/gsettings/almanah.convert
%{_datadir}/almanah
%{_datadir}/appdata/almanah.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.almanah.gschema.xml
%{_desktopdir}/almanah.desktop
%{_iconsdir}/hicolor/*x*/apps/almanah.png
%{_iconsdir}/hicolor/scalable/actions/almanah-tags-symbolic.svg
