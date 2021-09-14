Name:      python3-warwick-observatory-lmount
Version:   20210914
Release:   0
License:   GPL3
Summary:   Common code for the L mount daemon
Url:       https://github.com/warwick-one-metre/lmountd
BuildArch: noarch
Requires:  python3, python3-warwick-observatory-common

%description

%prep

rsync -av --exclude=build .. .

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog