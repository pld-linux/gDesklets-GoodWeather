
%define		pname	GoodWeather

Summary:	A sensor and display for displaying the current and forecasting weather information
Summary(pl):	Czujnik i wy¶wietlacz do pokazywania aktualnej informacji pogodowej oraz jej prognozowania
Name:		gDesklets-GoodWeather
Version:	0.4
Release:	3
License:	GPL v2
Group:		X11/Applications
Source0:	http://gdesklets.gnomedesktop.org/files/%{pname}-%{version}.tar.bz2
# Source0-md5:	ad7851fed9de6f8adc35d522d5b08cdb
Patch0:		%{name}-metatag.patch
URL:		http://gdesklets.gnomedesktop.org/categories.php?func=gd_show_app&gd_app_id=93
BuildRequires:	python >= 1:2.3
BuildRequires:	python-pygtk-gtk >= 1.99.14
Requires:	gDesklets
%pyrequires_eq	python-libs
Provides:	gDesklets-display
Provides:	gDesklets-sensor
#Conflicts:	gDesklets-StarterKit
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sensorsdir	%{_datadir}/gdesklets/Sensors
%define		_displaysdir	%{_datadir}/gdesklets/Displays

%description
This desklet (sensor/display) shows the current temperature, humidity,
sky, windchill temperature and a forecast of the next four days on
your desktop.

%description -l pl
Czujnik i wy¶wietlacz do pokazywania aktualnych informacji dotycz±cych
temperatury, wilgotno¶ci, zachmurzenia oraz si³y wiatru. Wy¶wietla
równie¿ informacje na temat pogody na najbli¿sze cztery dni.

%prep
%setup -q -n %{pname}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sensorsdir},%{_displaysdir}/%{pname}}

./Install_%{pname}_Sensor.bin --nomsg \
	$RPM_BUILD_ROOT%{_sensorsdir}

cp -R gfx *.display $RPM_BUILD_ROOT%{_displaysdir}/%{pname}

%py_comp $RPM_BUILD_ROOT%{_sensorsdir}
%py_ocomp $RPM_BUILD_ROOT%{_sensorsdir}

rm -f $RPM_BUILD_ROOT%{_sensorsdir}/*/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{_sensorsdir}/%{pname}
%{_sensorsdir}/%{pname}/*.py*
%{_sensorsdir}/%{pname}/liquid
%{_sensorsdir}/%{pname}/weather.com
%{_sensorsdir}/%{pname}/um
%{_displaysdir}/*
