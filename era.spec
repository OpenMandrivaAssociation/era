#define snapshot 20220107
%define git 20231019

Name:		era
Version:	0.5.1
Release:	%{?snapshot:0.%{snapshot}.}%{git}.0
Summary:	Maui Clock app
URL:    	https://mauikit.org
Source0:	https://invent.kde.org/maui/era/-/archive/%{?snapshot:master}%{!?snapshot:%{version}}/%{name}-%{?snapshot:master}%{!?snapshot:%{version}}.tar.bz2%{?snapshot:#/%{name}-%{snapshot}.tar.bz2}
License:	GPLv3
Group:		Development/Tools
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(MauiKit3)
BuildRequires:  cmake(MauiKitFileBrowsing3)
BuildRequires:  cmake(MauiKitCalendar3)
BuildRequires:	gettext
BuildRequires:	cmake(Qt5QuickCompiler)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5QmlModels)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Widgets)

%description
Maui Clock app

%prep
%autosetup -p1 -n %{name}-%{?snapshot:master}%{!?snapshot:%{version}}
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/era
%{_datadir}/applications/org.kde.era.desktop
%{_datadir}/metainfo/org.kde.era.appdata.xml
%{_iconsdir}/hicolor/scalable/apps/era.svg
