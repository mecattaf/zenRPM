# https://github.com/solopasha/hyprlandRPM/tree/master/nwg-look
# Generated by go2rpm 1.14.0
%bcond check 1
%bcond bootstrap 0

%if %{with bootstrap}
%global debug_package %{nil}
%endif

%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif

# https://github.com/nwg-piotr/nwg-look
%global goipath         github.com/nwg-piotr/nwg-look
Version:        0.2.7

%gometa -L -f

%global common_description %{expand:
GTK3 settings editor adapted to work in the wlroots environment.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           nwg-look
Release:        %autorelease
Summary:        GTK3 settings editor adapted to work in the wlroots environment

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

BuildRequires:  desktop-file-utils

Requires:       /usr/bin/gsettings
Requires:       xcur2png

%description %{common_description}


%prep
%goprep -A
%autopatch -p1

%if %{without bootstrap}
%generate_buildrequires
%go_generate_buildrequires
%endif

%if %{without bootstrap}
%build
%gobuild -o %{gobuilddir}/bin/nwg-look %{goipath}
%endif

%install
%if %{without bootstrap}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -Dpm0644 stuff/main.glade -t %{buildroot}%{_datadir}/nwg-look
install -Dpm0644 langs/* -t %{buildroot}%{_datadir}/nwg-look/langs
install -Dpm0644 stuff/nwg-look.desktop -t %{buildroot}%{_datadir}/applications
install -Dpm0644 stuff/nwg-look.svg -t %{buildroot}%{_datadir}/pixmaps
%endif

%if %{without bootstrap}
%if %{with check}
%check
%gocheck
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%endif
%endif

%if %{without bootstrap}
%files
%license LICENSE
%doc README.md
%{_bindir}/nwg-look
%{_datadir}/%{name}/
%{_datadir}/applications/nwg-look.desktop
%{_datadir}/pixmaps/nwg-look.svg
%endif

%changelog
%autochangelog

