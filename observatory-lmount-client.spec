Name:      observatory-lmount-client
Version:   20210912
Release:   0
Url:       https://github.com/warwick-one-metre/lmountd
Summary:   L mount client
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3, python3-Pyro4, python3-warwick-observatory-common, python3-warwick-observatory-lmount

%description

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}/etc/bash_completion.d
%{__install} %{_sourcedir}/lmount %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/completion/lmount %{buildroot}/etc/bash_completion.d/lmount

%files
%defattr(0755,root,root,-)
%{_bindir}/lmount
/etc/bash_completion.d/lmount

%changelog
