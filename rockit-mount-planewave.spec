Name:      rockit-mount-planewave
Version:   %{_version}
Release:   1
Summary:   Planewave L mount control
Url:       https://github.com/rockit-astro/mountd-planewave
License:   GPL-3.0
BuildArch: noarch

%description


%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}/etc/bash_completion.d
mkdir -p %{buildroot}%{_sysconfdir}/mountd/
mkdir -p %{buildroot}%{_udevrulesdir}

%{__install} %{_sourcedir}/tel %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/planewave_mountd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/planewave_mountd@.service %{buildroot}%{_unitdir}
%{__install} %{_sourcedir}/completion/tel %{buildroot}/etc/bash_completion.d/tel
%{__install} %{_sourcedir}/config/10-planewave-lmount.rules %{buildroot}%{_udevrulesdir}

%{__install} %{_sourcedir}/config/clasp.json %{buildroot}%{_sysconfdir}/mountd/
%{__install} %{_sourcedir}/config/halfmetre.json %{buildroot}%{_sysconfdir}/mountd/
%{__install} %{_sourcedir}/config/superwasp.json %{buildroot}%{_sysconfdir}/mountd/

%package server
Summary:  L mount server
Group:    Unspecified
Requires: python3-rockit-mount-planewave python3-astropy python3-requests pwi4
%description server

%files server
%defattr(0755,root,root,-)
%{_bindir}/planewave_mountd
%defattr(0644,root,root,-)
%{_unitdir}/planewave_mountd@.service
%{_udevrulesdir}/10-planewave-lmount.rules

%package client
Summary:  L mount client
Group:    Unspecified
Requires: python3-rockit-mount-planewave python3-astropy
%description client

%files client
%defattr(0755,root,root,-)
%{_bindir}/tel
/etc/bash_completion.d/tel

%package data-clasp
Summary: L mount configuration for the CLASP telescope
Group:   Unspecified
%description data-clasp

%files data-clasp
%defattr(0644,root,root,-)
%{_sysconfdir}/mountd/clasp.json

%package data-halfmetre
Summary: L mount configuration for the half metre telescope
Group:   Unspecified
%description data-halfmetre

%files data-halfmetre
%defattr(0644,root,root,-)
%{_sysconfdir}/mountd/halfmetre.json

%package data-superwasp
Summary: L mount configuration for the SuperWASP telescope
Group:   Unspecified
%description data-superwasp

%files data-superwasp
%defattr(0644,root,root,-)
%{_sysconfdir}/mountd/superwasp.json

%changelog