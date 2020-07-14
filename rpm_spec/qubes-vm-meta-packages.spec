%if 0%{?suse_version}
%define local_dist_name opensuse
%else
%define local_dist_name fedora
%endif

Name:		qubes-vm-meta-packages
Version:	%(cat version)
Release:	1%{?dist}
Summary:	Meta packages for Qubes-specific components
BuildArch:	noarch

Group:		System Environment/Base
License:	GPLv2+
URL:		https://www.qubes-os.org/

%if 0%{?qubes_builder}
%define _builddir %(pwd)
%endif

%package -n qubes-vm-dependencies
Summary:    Meta package with packages required in Qubes VM
Requires:   qubes-core-vm
Requires:   qubes-core-vm-systemd
Requires:   qubes-gui-vm

%description -n qubes-vm-dependencies
This package depends on packages required to be installed in Qubes VM.

%package -n qubes-vm-recommended
Summary:    Meta package with packages recommended in Qubes VM
Requires:   qubes-core-vm-doc
Requires:   mate-notification-daemon
Requires:   qubes-gpg-split
Requires:   qubes-img-converter
Requires:   qubes-input-proxy-sender
Requires:   qubes-mgmt-salt-vm-connector
Requires:   qubes-pdf-converter
Requires:   qubes-usb-proxy
Requires:   thunderbird-qubes

%description -n qubes-vm-recommended
Installing this package is recommended to have full functionality available in
Qubes VM.

%description
Meta packages for easy maintenance of installed Qubes OS specific packages.

%package -n qubes-repo-contrib
Summary:	Repository definition for packages contributed to Qubes OS

%description -n qubes-repo-contrib
Contrib repository contains packages written/adopted specifically for Qubes,
not available in upstream repositories.

%prep
%if 0%{?qubes_builder}
# we operate on the current directory, so no need to unpack anything
# symlink is to generate useful debuginfo packages
rm -f %{name}-%{version}
ln -sf . %{name}-%{version}
%setup -T -D
%else
%setup -q
%endif

%build

%install
make -C repos install-vm-%{local_dist_name} DESTDIR=$RPM_BUILD_ROOT

%files -n qubes-repo-contrib
%config(noreplace) /etc/yum.repos.d/qubes-contrib-vm-r3.2.repo
%if 0%{?suse_version}
/etc/pki/rpm-gpg/RPM-GPG-KEY-qubes-3.2-contrib-%{local_dist_name}
/etc/pki/rpm-gpg/RPM-GPG-KEY-qubes-3-contrib-%{local_dist_name}
%else
/etc/pki/rpm-gpg/RPM-GPG-KEY-qubes-3.2-contrib
/etc/pki/rpm-gpg/RPM-GPG-KEY-qubes-3-contrib
%endif

%files -n qubes-vm-dependencies

%files -n qubes-vm-recommended

%changelog

