Name:           perl-Devel-Symdump
Version:        2.10
Release:        3%{?dist}
Epoch:          1
Summary:        A Perl module for inspecting Perl's symbol table
Group:          Development/Libraries
License:        GPL+ or Artistic
Url:            http://search.cpan.org/dist/Devel-Symdump/
Source0:        http://www.cpan.org/authors/id/A/AN/ANDK/Devel-Symdump-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(Carp)
BuildRequires:  perl(English)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
# File::Spec is optional and not really needed on Unices
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
# Test::Pod::Coverage -> Pod::Coverage -> Devel::Symdump
%if 0%{!?perl_bootstrap:1}
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
%endif
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
The perl module Devel::Symdump provides a convenient way to inspect
perl's symbol table and the class hierarchy within a running program.

%prep
%setup -q -n Devel-Symdump-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
%{_fixperms} %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Devel/
%{_mandir}/man3/Devel::Symdump.3pm*

%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1:2.10-2
- Perl 5.18 rebuild

* Wed Mar 27 2013 Petr Šabata <contyk@redhat.com> - 1:2.10-1
- 2.10 bump
- Minor cleanup

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.08-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 19 2012 Marcela Mašláňová <mmaslano@redhat.com> - 1:2.08-13
- Change Exporter to BR, add lib dependency.

* Mon Nov  5 2012 Marcela Mašláňová <mmaslano@redhat.com> - 1:2.08-12
- Add missing requirement - Exporter

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.08-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Petr Pisar <ppisar@redhat.com> - 1:2.08-10
- Perl 5.16 re-rebuild of bootstrapped packages

* Sun Jun 10 2012 Petr Pisar <ppisar@redhat.com> - 1:2.08-9
- Perl 5.16 rebuild

* Wed Jan 11 2012 Paul Howarth <paul@city-fan.org> - 1:2.08-8
- Spec clean-up:
  - Use DESTDIR rather than PERL_INSTALL_ROOT
  - BR: perl(Carp)
  - BR: perl(Test::Pod) and perl(Test::Pod::Coverage) if not bootstrapping
  - Use %%{_fixperms} macro instead of our own chmod incantation
  - Make %%files list more explicit

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1:2.08-7
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.08-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 1:2.08-5
- Rebuild to fix problems with vendorarch/lib (#661697)

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 1:2.08-4
- Mass rebuild with perl-5.12.0

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1:2.08-3
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1:2.08-2
- rebuild against perl 5.10.1

* Mon Oct  5 2009 Stepan Kasal <skasal@redhat.com> - 1:2.08-1
- new upstream version

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.07-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.07-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1:2.07-5
- Rebuild for perl 5.10 (again)

* Thu Jan 10 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1:2.07-4
- rebuild for new perl

* Wed Aug 29 2007 Robin Norwood <rnorwood@redhat.com> - 1:2.07-3
- Add missing BuildRequires

* Mon Aug 27 2007 Robin Norwood <rnorwood@redhat.com> - 1:2.07-2
- Fix license tag
- Fix broken changelog entry

* Sat Feb  3 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1:2.07-1
- Update to 2.07.
- Minor corrections/cleanings.

* Sat Dec 02 2006 Robin Norwood <rnorwood@redhat.com> - 2.0604-1
- Upgrade to latest CPAN version: 2.0604

* Mon Jun 05 2006 Jason Vas Dias <jvdias@redhat.com> - 2.0601-1
- Upgrade to 2.0601

* Fri Feb 03 2006 Jason Vas Dias <jvdias@redhat.com> - 2.06-1
- Upgrade to 2.0.6
- rebuild for new perl-5.8.8

* Tue Jan 10 2006 Jason Vas Dias <jvdias@redhat.com> - 2.05-1
- fix bug 176718: Upgrade to 2.05

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcc

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcj

* Wed Apr 20 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.03-20
- (#155463)
- BuildArch correction (noarch).
- Bring up to date with current Fedora.Extras perl spec template.

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue May 11 2004 Chip Turner <cturner@redhat.com> 2.03-18
- fix typo, bugzilla 122905

* Thu Jun 05 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Aug  6 2002 Chip Turner <cturner@redhat.com>
- automated release bump and build

* Tue Jun  4 2002 Chip Turner <cturner@redhat.com>
- properly claim directories owned by package so they are removed when package is removed

* Sat Jan 26 2002 Tim Powers <timp@redhat.com>
- added provides

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Apr 30 2001 Chip Turner <cturner@redhat.com>
- Spec file was autogenerated. 
