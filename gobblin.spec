%define debug_package %{nil}

Name:		gobblin
Version:	%{__version}
Release:	%{__release}%{?dist}
Summary:	Universal data ingestion framework for Hadoop.

Group:		Applications
License:	Apache
URL:		https://github.com/linkedin/gobblin
Source0:	gobblin-dist.tar.gz

BuildRequires:	java-1.7.0-openjdk
Requires:	java-1.7.0-openjdk

%description
Gobblin is a universal data ingestion framework for extracting, transforming,
and loading large volume of data from a variety of data sources, e.g.,
databases, rest APIs, FTP/SFTP servers, filers, etc., onto Hadoop. Gobblin
handles the common routine tasks required for all data ingestion ETLs, including
job/task scheduling, task partitioning, error handling, state management, data
quality checking, data publishing, etc. Gobblin ingests data from different data
sources in the same execution framework, and manages metadata of different
sources all in one place. This, combined with other features such as auto
scalability, fault tolerance, data quality assurance, extensibility, and the
ability of handling data model evolution, makes Gobblin an easy-to-use,
self-serving, and efficient data ingestion framework.


%prep
%setup -qc


%build


%install
rm -rf $RPM_BUILD_ROOT

%{__mkdir_p} $RPM_BUILD_ROOT/opt
%{__mv} gobblin-dist $RPM_BUILD_ROOT/opt/%{name}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/opt/%{name}
%config(noreplace) /opt/%{name}/conf/*


%changelog
* Wed Oct 21 2015 Eduard Iskandarov <edikexp@gmail.com> b642afff27574c34f8dd75de3729a8d72760197e
- Update to git commit b642afff27574c34f8dd75de3729a8d72760197e
- No replace configuration files

* Tue Oct 20 2015 Eduard Iskandarov <edikexp@gmail.com> 0.5.0
- Initial RPM release
