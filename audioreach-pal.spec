%global debug_package %{nil}
%global _lto_cflags %{nil}

Name:           audioreach-pal
Version:        1.0.0
Release:        1%{?dist}
Summary:        AudioReach Platform Adaptation Layer library
License:        BSD-3-Clause-Clear
URL:            https://github.com/AudioReach/audioreach-pal
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

ExclusiveArch:  aarch64

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  expat-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(agm)
BuildRequires:  pkgconfig(spf)
BuildRequires:  pkgconfig(kvh2xml)
BuildRequires:  pkgconfig(audioroute)
BuildRequires:  pkgconfig(tinyalsa)
BuildRequires:  tinycompress-devel

%description
AudioReach Platform Adaptation Layer (PAL) for Qualcomm platforms.
PAL provides a unified audio API for use cases including playback,
capture, compressed offload, and voice. It sits above the AudioReach
Graph Manager (AGM) and provides configuration for QCS6490, QCS9075,
QCS8300, and other supported Qualcomm IoT platforms.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers and pkg-config files for building applications that use
the AudioReach Platform Adaptation Layer.

%prep
%autosetup -n %{name}-%{version}

%build
autoreconf -fi
%configure \
    --with-glib \
    --with-syslog

%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete

%files
%license LICENSE
%{_libdir}/lib*.so*
%config(noreplace) %{_sysconfdir}/usecaseKvManager.xml
%config(noreplace) %{_sysconfdir}/plugin_manager.xml
%config(noreplace) %{_sysconfdir}/mixer_paths_*.xml
%config(noreplace) %{_sysconfdir}/resourcemanager_*.xml

%files devel
%{_includedir}/pal/
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libplugin_manager.a
%{_libdir}/libsession_utils_config.a

%changelog
* Fri Aug 14 2026 Qualcomm Linux <quic_linux@quicinc.com> - 1.0.0-1
- Initial RPM packaging of audioreach-pal version 1.0.0
