#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	Plagger - Pluggable RSS/Atom Aggregator
#Summary(pl.UTF-8):	
Name:		Plagger
Version:	0.7.17
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/M/MI/MIYAGAWA/%{name}-%{version}.tar.gz
# Source0-md5:	bb78c8c141e030f70efaccd9206a48d9
URL:		http://plagger.org/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plagger is a pluggable RSS/Atom feed aggregator and remixer platform.

Everything is implemented as a small plugin just like qpsmtpd, blosxom
and perlbal. All you have to do is write a flow of aggregation,
filters, syndication, publishing and notification plugins in config
YAML file.

See http://plagger.org/ for cookbook examples, quickstart document,
development community (Mailing List and IRC), subversion repository
and bug tracking.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q

%build
%{__perl} Makefile.PL \
	--skipdeps \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS Changes
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/*.pm
%{perl_vendorlib}/Plagger/
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
