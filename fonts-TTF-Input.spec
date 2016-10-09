Summary:	Fonts for Code, from Font Bureau
Name:		fonts-TTF-Input
Version:	1.2
Release:	1
License:	Custom
Group:		Fonts
Source0:	Input-Font-%{version}.zip
# NoSource0-md5:	e137f760dd6f3b25b73ef3aa3a7a7fd9
NoSource:	0
URL:		http://input.fontbureau.com/
BuildRequires:	unzip
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/TTF
Requires:	fontconfig >= 1:2.10.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ttffontsdir	%{_fontsdir}/TTF

%description
Fonts for Code, from Font Bureau.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_ttffontsdir}

cp -a Input_Fonts/*/*/*.ttf $RPM_BUILD_ROOT%{_ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc ChangeLog.txt INSTALL.txt LICENSE.txt README.txt
%{_ttffontsdir}/InputMono-*.ttf
%{_ttffontsdir}/InputMonoCompressed-*.ttf
%{_ttffontsdir}/InputMonoCondensed-*.ttf
%{_ttffontsdir}/InputMonoNarrow-*.ttf
%{_ttffontsdir}/InputSans-*.ttf
%{_ttffontsdir}/InputSansCompressed-*.ttf
%{_ttffontsdir}/InputSansCondensed-*.ttf
%{_ttffontsdir}/InputSansNarrow-*.ttf
%{_ttffontsdir}/InputSerif-*.ttf
%{_ttffontsdir}/InputSerifCompressed-*.ttf
%{_ttffontsdir}/InputSerifCondensed-*.ttf
%{_ttffontsdir}/InputSerifNarrow-*.ttf
