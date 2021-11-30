Name:           risi-tweaks
Version:        1.1.6
Release:        1%{?dist}
Summary:        risiOS's Tweak Tool

License:        GPL v3
URL:            https://github.com/risiOS/webapp-manager
Source0:        %{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:  python
Requires:       python
Requires:	python3-gobject
Requires:	python3-beautifulsoup4
Requires:	python3-configobj
Requires:	python3-pillow
Requires:	python3-setproctitle
Requires:	python3-tldextract
Requires:	xapps

%description
A fork of the Linux Mint web app manager with a store for web apps.

%prep
%autosetup

%build
%install

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_datadir}

cp -a usr/bin %{buildroot}%{_bindir}
cp -a usr/lib/webapp-manager %{buildroot}%{_libdir}
cp -a usr/share %{buildroot}%{_datadir}
cp -a etc %{_sysconfdir}

%files
# %license add-license-file-here
# %doc add-docs-here

%changelog
* Tue Jul 13 2021 PizzaLovingNerd
- First spec file
