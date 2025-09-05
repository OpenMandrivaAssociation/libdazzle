%define api	1.0
%define major	0
%define libname %mklibname dazzle %{api} %{major}
%define girname %mklibname dazzle-gir %{api}
%define devname %mklibname -d dazzle

%define url_ver %(echo %{version} | cut -d. -f1,2)

Name:           libdazzle
Version:	3.44.0
Release:	9
Summary:        Experimental new features for GTK+ and GLib
Group:		System/Libraries

License:        GPLv3+
URL:            https://git.gnome.org/browse/libdazzle/
Source0:        https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)

%description
libdazzle is a collection of fancy features for GLib and Gtk+ that aren't quite
ready or generic enough for use inside those libraries. This is often a proving
ground for new widget prototypes. Applications such as Builder tend to drive
development of this project.

%package        -n %libname
Summary:        Experimental new features for GTK+ and GLib
Group:		System/Libraries
Obsoletes:	%{_lib}dazzle0 < 3.26.0-4

%description    -n %libname
libdazzle is a collection of fancy features for GLib and Gtk+ that aren't quite
ready or generic enough for use inside those libraries. This is often a proving
ground for new widget prototypes. Applications such as Builder tend to drive
development of this project.

%package	-n %{girname}
Summary:	GObject Introspection interface description for Dazzle
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}
Conflicts:	%{_lib}dazzle0 < 3.26.0-4

%description	-n %{girname}
GObject Introspection interface description for Dazzle.

%package        -n %devname
Summary:        Development files for %{name}
Group:		Development/C
Requires:       %{libname} = %{version}-%{release}
Requires:       %{girname} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}%{api}-devel = %{version}-%{release}

%description    -n %devname
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang libdazzle-%{api}

%files -n %libname -f libdazzle-%{api}.lang
%license COPYING
%doc AUTHORS NEWS README.md
%{_bindir}/dazzle-list-counters
%{_libdir}/libdazzle-%{api}.so.%{major}

%files -n %{girname}
%{_libdir}/girepository-1.0/Dazzle-%{api}.typelib

%files -n %devname
%doc CONTRIBUTING.md examples
%{_datadir}/gir-1.0/Dazzle-%{api}.gir
%{_datadir}/vala/vapi/libdazzle-%{api}.*
%{_includedir}/libdazzle-%{api}/
%{_libdir}/libdazzle-%{api}.so
%{_libdir}/pkgconfig/libdazzle-%{api}.pc
