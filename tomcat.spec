# TODO
# - %files
# - review %install section: which jar libs should we link to $TOMCATDIR/lib?
# - packages for *.renametojar files (-cgi and -ssi in server/lib)
# Conditional build:
%bcond_without	javadoc		# skip building javadocs
%bcond_with	jta		# put jta jar into tomcat lib dir.
%bcond_without	java_sun	# build with gcj (does not work)
#
Summary:	Apache Servlet/JSP Engine, RI for Servlet 2.5/JSP 2.1 API
Summary(pl.UTF-8):	Silnik Servlet/JSP Apache będący wzorcową implementacją API Servlet 2.5/JSP 2.1
Name:		tomcat
Version:	6.0.20
Release:	0.1
License:	Apache v2.0
Group:		Networking/Daemons/Java
Source0:	http://www.apache.org/dist/tomcat/tomcat-6/v%{version}/src/apache-%{name}-%{version}-src.tar.gz
# Source0-md5:	44f49e7e14028b6a53c3c346bd18c72f
Source1:	apache-%{name}.init
Source2:	apache-%{name}.sysconfig
Source3:	%{name}-build.properties
Source10:	apache-%{name}-context-ROOT.xml
Source11:	apache-%{name}-context-balancer.xml
Source12:	apache-%{name}-context-jsp-examples.xml
Source13:	apache-%{name}-context-tomcat-docs.xml
Source14:	apache-%{name}-context-webdav.xml
Patch0:		%{name}-build.xml.patch
URL:		http://tomcat.apache.org/
BuildRequires:	apr-devel
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRequires:	openssl-devel
%if %{with java_sun}
BuildRequires:	java-sun >= 1.5
BuildRequires:	java-sun-jre >= 1.5
%else
BuildRequires:	java-gcj-compat-devel
%endif
BuildRequires:	ant >= 1.5.3
BuildRequires:	ant-trax
BuildRequires:	eclipse-jdt >= 3.2
BuildRequires:	java-commons-collections >= 0:2.0
BuildRequires:	java-commons-daemon >= 1.0
BuildRequires:	java-commons-dbcp >= 0:1.1
BuildRequires:	java-commons-dbcp-tomcat5 >= 0:1.1
BuildRequires:	jpackage-utils
BuildRequires:	junit >= 0:3.8.1
BuildRequires:	rpmbuild(macros) >= 1.300
Requires(post,postun):	/sbin/ldconfig
Requires(post,preun):	/sbin/chkconfig
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires:	%{name}-jasper = %{version}-%{release}
Requires:	jaas
Requires:	java-commons-beanutils
Requires:	java-commons-collections
Requires:	java-commons-digester
Requires:	java-commons-el
Requires:	java-commons-logging
Requires:	java-commons-modeler
Requires:	java-commons-pool-tomcat5
Requires:	java-jdbc-mysql
Requires:	java-regexp
Requires:	java-servletapi5 = %{version}
Requires:	java-xml-commons
Requires:	javamail >= 1.2
Requires:	jaxp_parser_impl
Requires:	jdbc-stdext >= 2.0
Requires:	jndi >= 1.2.1
Requires:	jre >= 1.2
Requires:	jsse >= 1.0.2
%{?with_jta:Requires:	jta >= 1.0.1}
Requires:	rc-scripts
Provides:	group(servlet)
Provides:	group(tomcat)
Provides:	java-servlet-container
Provides:	user(tomcat)
Obsoletes:	apache-tomcat
Obsoletes:	jakarta-tomcat
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_tomcatdir	%{_datadir}/tomcat
%define 	_logdir		%{_var}/log
%define		_vardir		%{_var}/lib/tomcat
%define		_sysconfdir	/etc/tomcat

%define find_jar() %{expand:%%define jarfile {%(jar=$(find-jar %1); echo ${jar:-%%nil})}}%{?jarfile}%{!?jarfile:%{error:find-jar %1 failed}}%{nil}

%description
Tomcat is the servlet container that is used in the official Reference
Implementation for the Java Servlet and JavaServer Pages technologies.
The Java Servlet and JavaServer Pages specifications are developed by
Sun under the Java Community Process.

Tomcat is developed in an open and participatory environment and
released under the Apache Software License. Tomcat is intended to be a
collaboration of the best-of-breed developers from around the world.
We invite you to participate in this open development project.

%description -l pl.UTF-8
Tomcat to kontener serwletowy używany przez oficjalną implementację
wzorcową technologii Java Servlet i JavaServer Pages. Specyfikacje
Java Servlet i JavaServer Pages są rozwijane przez Suna zgodnie z Java
Community Process.

%package doc
Summary:	The Apache Tomcat Servlet/JSP Container documentation
Summary(pl.UTF-8):	Dokumentacja do Tomcata - kontenera Servlet/JSP
Group:		Documentation
Obsoletes:	apache-tomcat-doc
Obsoletes:	jakarta-tomcat-doc

%description doc
The Tomcat Servlet/JSP Container documentation.

%description doc -l pl.UTF-8
Dokumentacja do Tomcata - kontenera Servlet/JSP.

%package admin
Summary:	Apache Tomcat`s Administration Web Application
Summary(pl.UTF-8):	Panel Administracyjny dla Apache Tomcat
Group:		Networking/Daemons/Java/Servlets
Requires:	%{name} = %{version}-%{release}
Requires:	java-commons-chain

%description admin
Administration Web Application for Apache Tomcat.

%description admin -l pl.UTF-8
Panel Administracyjny dla Apache Tomcat.

%package jasper
Summary:	JSP compiler
Summary(pl.UTF-8):	Kompilator JSP
Group:		Libraries/Java
Requires:	jpackage-utils
Obsoletes:	apache-tomcat-jasper

%description jasper
Jasper is Java ServerPages compiler used by Apache Tomcat servlet
container.

%description jasper -l pl.UTF-8
Jasper jest kompilatorem Java ServerPages używanym przez kontener
servletów Apache Tomcat.

%prep
%setup -q -n apache-%{name}-%{version}-src

%patch0 -p0

# we don't need those scripts
rm -f container/catalina/src/bin/*.bat
rm -f container/catalina/src/bin/{startup,shutdown}.sh

cp %{SOURCE3} build.properties

%build
TOPDIR=$(pwd)

%ant -Drpm.javadir=%{_javadir} -Drpm.libdir=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
cd output/build

TOMCATDIR=$RPM_BUILD_ROOT%{_tomcatdir}
CATALINADIR=$RPM_BUILD_ROOT/var/lib/tomcat

install -d $TOMCATDIR \
	    $CATALINADIR/temp \
	    $RPM_BUILD_ROOT%{_vardir}/webapps \
	    $RPM_BUILD_ROOT%{_vardir}/work \
	    $RPM_BUILD_ROOT%{_vardir}/conf \
	    $RPM_BUILD_ROOT%{_logdir}/tomcat \
	    $RPM_BUILD_ROOT/etc/sysconfig \
	    $RPM_BUILD_ROOT/etc/rc.d/init.d

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/tomcat
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/tomcat

cp -a conf/* $CATALINADIR/conf
install -d $CATALINADIR/conf/Catalina/localhost
install %{SOURCE10} $CATALINADIR/conf/Catalina/localhost/ROOT.xml
install %{SOURCE11} $CATALINADIR/conf/Catalina/localhost/balancer.xml
install %{SOURCE12} $CATALINADIR/conf/Catalina/localhost/jsp-examples.xml
install %{SOURCE13} $CATALINADIR/conf/Catalina/localhost/tomcat-docs.xml
install %{SOURCE14} $CATALINADIR/conf/Catalina/localhost/webdav.xml

cp -a bin lib webapps $TOMCATDIR
cp -a temp $CATALINADIR

ln -sf %{_logdir}/tomcat $CATALINADIR/logs
ln -sf %{_logdir}/tomcat $TOMCATDIR/logs
ln -sf %{_vardir}/work $TOMCATDIR/work
ln -sf %{_vardir}/conf $TOMCATDIR/conf
ln -sf %{_vardir}/conf $RPM_BUILD_ROOT%{_sysconfdir}

# symlinks instead of copies
jars="commons-daemon commons-logging-api"
for jar in $jars; do
	jar=$(find-jar $jar)
	ln -sf $jar $TOMCATDIR/bin
done

# jars="commons-el commons-dbcp-tomcat5 commons-pool-tomcat5 servlet-api jsp-api commons-modeler jdbc-mysql"
# for jar in $jars; do
# 	jar=$(find-jar $jar)
# 	ln -sf $jar $TOMCATDIR/common/lib
# done
# 
# jars="jaxp_parser_impl xml-commons-apis"
# for jar in $jars; do
# 	jar=$(find-jar $jar)
# 	ln -sf $jar $TOMCATDIR/common/endorsed
# done

# jars="struts-core struts-taglib commons-collections commons-beanutils-core commons-digester commons-chain"
# for jar in $jars; do
# 	jar=$(find-jar $jar)
# 	ln -sf $jar $TOMCATDIR/server/webapps/admin/WEB-INF/lib
# done

# jars="commons-modeler"
# for jar in $jars; do
# 	jar=$(find-jar $jar)
# 	ln -sf $jar $TOMCATDIR/server/lib
# done

install -d $RPM_BUILD_ROOT%{_javadir}
mv $TOMCATDIR/lib/jasper*.jar $RPM_BUILD_ROOT%{_javadir}
ln -sf %{_javadir}/jasper-compiler-jdt.jar $TOMCATDIR/lib
ln -sf %{_javadir}/jasper-compiler.jar $TOMCATDIR/lib
ln -sf %{_javadir}/jasper-runtime.jar $TOMCATDIR/lib

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%groupadd -g 234 -r -f tomcat
%groupadd -g 237 -r -f servlet
%useradd -u 234 -r -d /var/lib/tomcat -s /bin/false -c "Tomcat User" -g tomcat -G servlet tomcat

%post
/sbin/chkconfig --add tomcat
%service tomcat restart

%preun
if [ "$1" = "0" ]; then
	%service tomcat stop
	/sbin/chkconfig --del tomcat
fi

%postun
if [ "$1" = "0" ]; then
	%userremove tomcat
	%groupremove tomcat
	%groupremove servlet
fi

%files
%defattr(644,root,root,755)
%doc build/{RELEASE-NOTES,RUNNING.txt}
%attr(754,root,root) /etc/rc.d/init.d/tomcat
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/tomcat
%{_sysconfdir}
%dir %{_tomcatdir}
%dir %{_tomcatdir}/conf
%dir %{_tomcatdir}/bin
%{_tomcatdir}/bin/catalina-tasks.xml
%{_tomcatdir}/bin/jkstatus-tasks.xml
%{_tomcatdir}/bin/jmxaccessor-tasks.xml
%attr(755,root,root) %{_tomcatdir}/bin/*.sh
%{_tomcatdir}/bin/*.jar
%dir %{_tomcatdir}/common
%dir %{_tomcatdir}/common/classes
%dir %{_tomcatdir}/common/endorsed
%dir %{_tomcatdir}/common/i18n
%{_tomcatdir}/common/endorsed/*.jar
%{_tomcatdir}/common/i18n/tomcat-i18n-en.jar
%lang(es) %{_tomcatdir}/common/i18n/tomcat-i18n-es.jar
%lang(fr) %{_tomcatdir}/common/i18n/tomcat-i18n-fr.jar
%lang(ja) %{_tomcatdir}/common/i18n/tomcat-i18n-ja.jar
%{_tomcatdir}/common/lib
%dir %{_tomcatdir}/server
%dir %{_tomcatdir}/server/classes
%{_tomcatdir}/server/lib
%dir %{_tomcatdir}/server/webapps

%config(noreplace) %attr(664,root,tomcat) %verify(not md5 mtime size) %{_vardir}/conf/Catalina/localhost/host-manager.xml
%{_tomcatdir}/server/webapps/host-manager

%config(noreplace) %attr(664,root,tomcat) %verify(not md5 mtime size) %{_vardir}/conf/Catalina/localhost/manager.xml
%{_tomcatdir}/server/webapps/manager

%dir %{_tomcatdir}/webapps

%config(noreplace) %attr(664,root,tomcat) %verify(not md5 mtime size) %{_vardir}/conf/Catalina/localhost/ROOT.xml
%{_tomcatdir}/webapps/ROOT

%config(noreplace) %attr(664,root,tomcat) %verify(not md5 mtime size) %{_vardir}/conf/Catalina/localhost/balancer.xml
%{_tomcatdir}/webapps/balancer

%config(noreplace) %attr(664,root,tomcat) %verify(not md5 mtime size) %{_vardir}/conf/Catalina/localhost/webdav.xml
%{_tomcatdir}/webapps/webdav

%{_tomcatdir}/logs
%{_tomcatdir}/work
%{_tomcatdir}/shared
%dir %{_vardir}
# these directory has to be writeable because /admin need to modify config
# files and create temporary files
%dir %attr(775,root,tomcat) %{_vardir}/conf
%dir %attr(775,root,tomcat) %{_vardir}/conf/Catalina
%dir %{_vardir}/conf/Catalina/localhost
# tomcat config has to be writeable because of tomcat-users.xml file and Catalina dir
%config(noreplace) %attr(664,root,tomcat) %verify(not md5 mtime size) %{_vardir}/conf/MANIFEST.MF
%config(noreplace) %attr(664,root,tomcat) %verify(not md5 mtime size) %{_vardir}/conf/catalina.policy
%config(noreplace) %attr(664,root,tomcat) %verify(not md5 mtime size) %{_vardir}/conf/*.properties*
%config(noreplace) %attr(664,root,tomcat) %verify(not md5 mtime size) %{_vardir}/conf/*.manifest
%config(noreplace) %attr(664,root,tomcat) %verify(not md5 mtime size) %{_vardir}/conf/*.xml
%dir %attr(1730,root,tomcat) %{_vardir}/work
%dir %attr(775,root,tomcat) %{_vardir}/webapps
%dir %attr(775,root,tomcat) %{_vardir}/temp
%dir %attr(775,root,tomcat) %{_logdir}/tomcat
%{_vardir}/logs

%files doc
%defattr(644,root,root,755)
%config(noreplace) %attr(664,root,tomcat) %verify(not md5 mtime size) %{_vardir}/conf/Catalina/localhost/tomcat-docs.xml
%{_tomcatdir}/webapps/tomcat-docs

%files admin
%defattr(644,root,root,755)
%config(noreplace) %attr(664,root,tomcat) %verify(not md5 mtime size) %{_vardir}/conf/Catalina/localhost/admin.xml
%{_tomcatdir}/server/webapps/admin

%files jasper
%defattr(644,root,root,755)
%{_javadir}/jasper-compiler-jdt.jar
%{_javadir}/jasper-compiler.jar
%{_javadir}/jasper-runtime.jar
