Name:                swt-chart
Version:             0.10.0
Release:             1
Summary:             SWTChart Feature

License:             EPL-1.0
URL:                 https://github.com/eclipse/swtchart
Source0:             http://sourceforge.net/code-snapshots/svn/s/sw/swt-chart/code/swt-chart-code-r312-tags-%{version}.zip

BuildArch:           noarch

BuildRequires:       tycho >= 0.14.0
Requires:            eclipse-platform >= 3.4.0

%description
SWTChart is a light-weight charting component for SWT.

%package        javadoc
Summary:             Javadoc for %{name}

%description    javadoc
%{summary}.

%prep
%setup -q -n %{name}-code-r312-tags-%{version}
# Create the poms
xmvn -o org.eclipse.tycho:tycho-pomgenerator-plugin:generate-poms -DgroupId=org.swtchart
%mvn_package "::pom::" __noinstall
%mvn_package :org.swtchart.example* __noinstall

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Aug 17 2020 wangxiao <wangxiao65@huawei.com> - 0.10.0-1
- package init
