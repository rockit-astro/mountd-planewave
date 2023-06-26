Name:      halfmetre-lmount-server
Version:   20230626
Release:   0
Url:       https://github.com/warwick-one-metre/lmountd
Summary:   Mount daemon for the half metre telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3 python3-astropy python3-Pyro4 python3-requests
Requires:  python3-warwick-observatory-common python3-warwick-observatory-lmount
Requires:  pwi4

%description

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_udevrulesdir}
mkdir -p %{buildroot}%{_sysconfdir}/lmountd/

%{__install} %{_sourcedir}/lmountd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/lmountd@.service %{buildroot}%{_unitdir}
%{__install} %{_sourcedir}/10-planewave-lmount.rules %{buildroot}%{_udevrulesdir}
%{__install} %{_sourcedir}/halfmetre.json %{buildroot}%{_sysconfdir}/lmountd/

%files
%defattr(0755,root,root,-)
%{_bindir}/lmountd
%defattr(0644,root,root,-)
%{_unitdir}/lmountd@.service
%{_udevrulesdir}/10-planewave-lmount.rules
%{_sysconfdir}/lmountd/halfmetre.json

%changelog
