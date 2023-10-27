%define	major 0
%define	libname		%mklibname %{name} %{major}
%define	develname	%mklibname %{name} -d

Summary:	A library for Gtk+ which provides a spread sheet widget
Name:		spread-sheet-widget
Version:	0.10
Release:	1
License:	GPLv3+
URL:		https://www.gnu.org/software/ssw/
Source0:	https://alpha.gnu.org/gnu/ssw/%{name}-%{version}.tar.gz
Source1:	https://alpha.gnu.org/gnu/ssw/%{name}-%{version}.tar.gz.sig
Patch1:		spread-sheet-widget-0001-No-need-to-specify-gtk3-lib-in-pc-file.patch
Patch2:		spread-sheet-widget-0002-Use-more-standard-macros-in-pc-file.patch

BuildRequires:	texinfo
BuildRequires:	pkgconfig(glib-2.0) >= 2.44
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.18.0

%description
GNU Spread Sheet Widget is a library for Gtk+ which provides a widget for
viewing and manipulating 2 dimensional tabular data in a manner similar to many
popular spread sheet programs.

The design follows the model-view-controller paradigm and is of complexity O(1)
in both time and space. This means that it is efficient and fast even for very
large data.

Features commonly found in graphical user interfaces such as cut and paste,
drag and drop and row/column labelling are also included.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	A library for Gtk+ which provides a spread sheet widget
Group:		System/Libraries

%description -n %{libname}
GNU Spread Sheet Widget is a library for Gtk+ which provides a widget for
viewing and manipulating 2 dimensional tabular data in a manner similar to many
popular spread sheet programs.

The design follows the model-view-controller paradigm and is of complexity O(1)
in both time and space. This means that it is efficient and fast even for very
large data.

Features commonly found in graphical user interfaces such as cut and paste,
drag and drop and row/column labelling are also included.

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{develname}
Summary:	The development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}

%description -n %{develname}
Additional header files for development with %{name}.

%files -n %{develname}
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%{_includedir}/ssw-axis-model.h
%{_includedir}/ssw-sheet-axis.h
%{_includedir}/ssw-sheet.h
%{_includedir}/ssw-virtual-model.h
%{_infodir}/%{name}.info*
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

