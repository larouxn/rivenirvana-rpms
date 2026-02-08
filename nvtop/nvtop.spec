%global commit 76890233d759199f50ad3bdb57a0c0988e96fc44
%global shortc %(c=%{commit}; echo ${c:0:7})

Name:           nvtop
Version:        3.3.2
Release:        1.g%{shortc}%{?dist}
Summary:        GPU & Accelerator process monitoring for AMD, Apple, Huawei, Intel, NVIDIA and Qualcomm

License:        GPLv3
URL:            https://github.com/Syllo/nvtop

Source:         %{url}/archive/%{commit}/%{commit}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(ncursesw)

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib


%description
NVTOP stands for Neat Videocard TOP, a (h)top like task monitor for GPUs and
accelerators. It can handle multiple GPUs and print information about them in
a htop-familiar way.

%prep
%autosetup -p1 -n %{name}-%{commit}

%build
%cmake -DNVIDIA_SUPPORT=ON -DAMDGPU_SUPPORT=ON -DINTEL_SUPPORT=ON
%cmake_build

%install
%cmake_install


%files
%license COPYING
%doc README.markdown
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man1/%{name}.1*
%{_metainfodir}/io.github.syllo.nvtop.metainfo.xml

%changelog
%autochangelog
