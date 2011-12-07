Name: hunspell-et
Summary: Estonian hunspell dictionaries
%define upstreamid 20030606
Version: 0.%{upstreamid}
Release: 5.1%{?dist}
Source: http://www.meso.ee/~jjpp/speller/ispell-et_%{upstreamid}.tar.gz
Group: Applications/Text
URL: http://www.meso.ee/~jjpp/speller/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv2+ and LPPL
BuildArch: noarch

Requires: hunspell
Provides: hunspell-ee = 0.20030606-4
Obsoletes: hunspell-ee < 0.20030606-4

%description
Estonian hunspell dictionaries.

%package -n hyphen-et
Requires: hyphen
Summary: Estonian hyphenation rules
Group: Applications/Text

%description -n hyphen-et
Estonian hyphenation rules.

%prep
%setup -q -n ispell-et-%{upstreamid}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p latin-1/et_EE.* $RPM_BUILD_ROOT/%{_datadir}/myspell
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_et.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/hyph_et_EE.dic

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README COPYRIGHT
%{_datadir}/myspell/*

%files -n hyphen-et
%defattr(-,root,root,-)
%doc README COPYRIGHT
%{_datadir}/hyphen/*


%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20030606-5.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20030606-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 30 2009 Caolan McNamara <caolanm@redhat.com> - 0.20030606-4
- erroneously imported as hunspell-ee, rename as hunspell-et

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20030606-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Nov 23 2007 Caolan McNamara <caolanm@redhat.com> - 0.20030606-2
- package hyphenation rules

* Fri Nov 23 2007 Caolan McNamara <caolanm@redhat.com> - 0.20030606-1
- canonical upstream tarball

* Thu Aug 09 2007 Caolan McNamara <caolanm@redhat.com> - 0.20030602-2
- clarify license

* Thu Dec 07 2006 Caolan McNamara <caolanm@redhat.com> - 0.20030602-1
- initial version
