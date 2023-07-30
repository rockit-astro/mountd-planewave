Name:      rockit-lmount
Version:   %{_version}
Release:   1
Summary:   Planewave L mount control
Url:       https://github.com/rockit-astro/lmountd
License:   GPL-3.0
BuildArch: noarch

%description


%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}/etc/bash_completion.d
mkdir -p %{buildroot}%{_sysconfdir}/lmountd/
mkdir -p %{buildroot}%{_udevrulesdir}

%{__install} %{_sourcedir}/tel %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/lmountd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/lmountd@.service %{buildroot}%{_unitdir}
%{__install} %{_sourcedir}/completion/tel %{buildroot}/etc/bash_completion.d/tel
%{__install} %{_sourcedir}/config/10-planewave-lmount.rules %{buildroot}%{_udevrulesdir}

%{__install} %{_sourcedir}/config/clasp.json %{buildroot}%{_sysconfdir}/lmountd/
%{__install} %{_sourcedir}/config/halfmetre.json %{buildroot}%{_sysconfdir}/lmountd/
%{__install} %{_sourcedir}/config/superwasp.json %{buildroot}%{_sysconfdir}/lmountd/

%package server
Summary:  L mount server
Group:    Unspecified
Requires: python3-rockit-lmount python3-astropy python3-requests pwi4
%description server

%files server
%defattr(0755,root,root,-)
%{_bindir}/lmountd
%defattr(0644,root,root,-)
%{_unitdir}/lmountd@.service
%{_udevrulesdir}/10-planewave-lmount.rules

%package client
Summary:  L mount client
Group:    Unspecified
Requires: python3-rockit-lmount python3-astropy
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
%{_sysconfdir}/lmountd/clasp.json

%package data-halfmetre
Summary: L mount configuration for the half metre telescope
Group:   Unspecified
%description data-halfmetre

%files data-halfmetre
%defattr(0644,root,root,-)
%{_sysconfdir}/lmountd/halfmetre.json

%package data-superwasp
Summary: L mount configuration for the SuperWASP telescope
Group:   Unspecified
%description data-superwasp

%files data-superwasp
%defattr(0644,root,root,-)
%{_sysconfdir}/lmountd/superwasp.json

%changelog
