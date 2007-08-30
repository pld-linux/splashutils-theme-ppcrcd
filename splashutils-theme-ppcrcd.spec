#
# Conditional build:
%bcond_with	scaler	# build for splashutils with scale capabilities

%define		theme	ppcrcd
Summary:	Splashutils - ppcrcd theme
Summary(pl.UTF-8):	Splashutils - motyw ppcrcd
Name:		splashutils-theme-%{theme}
Version:	2.1
Release:	1
License:	GPL v2
Group:		Themes
Source0:	http://ppcrcd.pld-linux.org/fbsplash/fbsplash-theme-%{theme}-%{version}.tar.bz2
# Source0-md5:	101ce1bca5f8e146df81c767ed906f59
URL:		http://ppcrcd.pld-linux.org/fbsplash/
%{!?with_scaler:BuildRequires: /usr/bin/convert}
Provides:	fbsplash-theme
Requires:	splashutils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/splash

%description
PPCRCD theme for splashutils.

%description -l pl.UTF-8
Motyw PPCRCD do splashutils.

%prep
%setup -q -n fbsplash-theme-%{theme}-%{version}

%build
%if %{with scaler}
./calc_splash_configs.pl ppcrcd.jpg
%else
./calc_splash_configs.pl ppcrcd.png 1 -- -verbose -quality 90
%endif

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sysconfdir}/
cp -a ppcrcd $RPM_BUILD_ROOT%{_sysconfdir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/%{theme}
