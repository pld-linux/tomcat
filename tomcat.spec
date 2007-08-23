# Conditional build:
%bcond_without	javadoc	# skip building javadocs
#
Summary:	Apache Servlet/JSP Engine, RI for Servlet 2.4/JSP 2.0 API
Summary(pl.UTF-8):	Silnik Servlet/JSP Apache będący wzorcową implementacją API Servlet 2.4/JSP 2.0
Name:		apache-tomcat
Version:	5.5.23
Release:	0.1
License:	Apache
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/tomcat/tomcat-5/v%{version}/src/%{name}-%{version}-src.tar.gz
# Source0-md5:	362d1d8b15dc09882440dcab8c592dd7
Source1:	%{name}.init
Patch0:		%{name}-skip-servletapi.patch
Patch1:		%{name}-nsis.patch
Patch2:		%{name}-native.patch
Patch3:		%{name}-skip-jdt.patch
Patch4:		%{name}-no-connectors.patch
URL:		http://tomcat.apache.org/
BuildRequires:	ant >= 1.5.3
BuildRequires:	ant-trax
BuildRequires:	eclipse-jdt
BuildRequires:	jaas
BuildRequires:	jakarta-commons-beanutils >= 1.7
BuildRequires:	jakarta-commons-collections >= 0:3.1
BuildRequires:	jakarta-commons-collections-source >= 0:3.1
BuildRequires:	jakarta-commons-daemon >= 1.0
BuildRequires:	jakarta-commons-dbcp >= 0:1.2.1
BuildRequires:	jakarta-commons-dbcp-source >= 0:1.2.1
BuildRequires:	jakarta-commons-digester >= 0:1.7
BuildRequires:	jakarta-commons-el >= 0:1.0
BuildRequires:	jakarta-commons-fileupload >= 0:1.0
BuildRequires:	jakarta-commons-httpclient
BuildRequires:	jakarta-commons-launcher >= 0:0.9
BuildRequires:	jakarta-commons-logging >= 0:1.0.4
BuildRequires:	jakarta-commons-modeler >= 2.0
BuildRequires:	jakarta-commons-pool >= 0:1.2
BuildRequires:	jakarta-commons-pool-source >= 0:1.2
BuildRequires:	jakarta-regexp >= 0:1.3
BuildRequires:	jakarta-servletapi5
#BuildRequires:	jakarta-struts >= 0:1.2.7
BuildRequires:	jakarta-struts >= 1.0.2
BuildRequires:	javamail >= 0:1.3.1
BuildRequires:	jaxp_parser_impl >= 0:2.7.1
BuildRequires:	jdbc-stdext >= 0:2.0
BuildRequires:	jdk >= 1.5
BuildRequires:	jmx
BuildRequires:	jndi >= 0:1.2.1
BuildRequires:	jpackage-utils
BuildRequires:	jsse >= 0:1.0.3
BuildRequires:	jta >= 0:1.0.1
BuildRequires:	junit >= 0:3.8.1
BuildRequires:	logging-log4j
#BuildRequires:	mx4j >= 0:3.0.1
BuildRequires:	mx4j >= 1.1.1
BuildRequires:	puretls
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	xerces-j >= 0:2.7.1
BuildRequires:	xml-commons
#BuildRequires:	xml-commons >= 1.3
Requires(post,postun):	/sbin/ldconfig
Requires(post,preun):	/sbin/chkconfig
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires:	jaas
#Requires:	jaf >= 1.0.1
Requires:	jakarta-commons-beanutils
Requires:	jakarta-commons-collections
Requires:	jakarta-commons-digester
Requires:	jakarta-commons-fileupload
Requires:	jakarta-commons-logging
Requires:	jakarta-regexp
Requires:	jakarta-servletapi >= 4
Requires:	javamail >= 1.2
Requires:	jaxp_parser_impl
Requires:	jdbc-stdext >= 2.0
Requires:	jndi >= 1.2.1
Requires:	jre >= 1.2
Requires:	jsse >= 1.0.2
Requires:	jta >= 1.0.1
Requires:	mx4j >= 1.1.1
Requires:	rc-scripts
Requires:	xml-commons
Provides:	group(http)
Provides:	user(http)
Obsoletes:	jakarta-tomcat
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_tomcatdir	%{_datadir}/tomcat
%define 	_logdir		%{_var}/log
%define		_vardir		%{_var}/lib/tomcat
%define		_sysconfdir	/etc/tomcat

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
Summary(pl.UTF-8):	Dokumentacja do Tomcata - kontekera Servlet/JSP
Group:		Development/Languages/Java
Obsoletes:	jakarta-tomcat-doc

%description doc
The Tomcat Servlet/JSP Container documentation.

%description doc -l pl.UTF-8
Dokumentacja do Tomcata - kontekera Servlet/JSP.

%prep
%setup -q -n %{name}-%{version}-src
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

# servletapi built from jakarta-servletapi5.spec
rm -rf servletapi

# Remove pre-built jars
find -name '*.jar' | xargs rm -fv

%build
TOPDIR=$(pwd)

mkdir -p tomcat-deps
> tomcat-deps/tomcat-dbcp.jar

%if 0
# build jasper javadocs
cd jasper
CLASSPATH=$(build-classpath xml-commons-apis)
cat > build.properties <<EOF
ant.jar=$(build-classpath ant)
servlet-api.jar=$(build-classpath servlet-api)
jsp-api.jar=$(build-classpath jsp-api)
tools.jar=%{java_home}/lib/tools.jar
xercesImpl.jar=$(build-classpath jaxp_parser_impl)
xmlParserAPIs.jar=$(build-classpath xml-commons-apis)
commons-collections.jar=$(build-classpath commons-collections)
commons-logging.jar=$(build-classpath commons-logging)
commons-daemon.jar=$(build-classpath commons-daemon)
junit.jar=$(build-classpath junit)
commons-el.jar=$(build-classpath commons-el)
EOF
# building jasper needs eclipse classes
#%ant dist

%if %{with javadoc}
%ant javadoc \
	-Dcompile.source=1.4 \
	-Dbuild.compiler=modern \

%endif
cd -
%endif

# build tomcat 5.5
cat > build.properties <<EOF
commons-beanutils.jar=$(build-classpath commons-beanutils)
commons-launcher.jar=$(build-classpath commons-launcher)
commons-daemon.jar=$(build-classpath commons-daemon)
commons-digester.jar=$(build-classpath commons-digester)
commons-el.jar=$(build-classpath commons-el)
commons-logging-api.jar=$(build-classpath commons-logging-api)
commons-logging.jar=$(build-classpath commons-logging)
commons-modeler.jar=$(build-classpath commons-modeler)
xercesImpl.jar=$(build-classpath jaxp_parser_impl)
xml-apis.jar=$(build-classpath xml-commons-apis)
jdt.jar=$(build-classpath org.eclipse.jdt.core)
jasper-compiler-jdt.home=$TOPDIR/tomcat-deps
commons-httpclient.jar=$(build-classpath commons-httpclient)
commons-collections.jar=$(build-classpath commons-collections)
commons-fileupload.jar=$(build-classpath commons-fileupload)
jmx.jar=$(build-classpath jmx)
jmx-tools.jar=$(build-classpath jmx)
junit.jar=$(build-classpath junit)
struts.jar=$(build-classpath struts)
jcert.jar=$(build-classpath java/jcert)
jnet.jar=$(build-classpath java/jnet)
jsse.jar=$(build-classpath java/jsse)
jta.jar=$(build-classpath jta)
puretls.jar=$(build-classpath puretls)
servlet-api.jar=$(build-classpath servlet-api)
servletapi.build.notrequired=true
jsp-api.jar=$(build-classpath jsp-api)
jspapi.build.notrequired=true
log4j.jar=$(build-classpath log4j)
# source is needed because source is copied modified and recompiled as tomcat jar
# see <target name="-build-tomcat-dbcp"> in build/build.xml
commons-collections.home=%{_prefix}/src/jakarta-commons-collections-3.1
commons-pool.home=%{_prefix}/src/jakarta-commons-pool-1.3
commons-dbcp.home=%{_prefix}/src/jakarta-commons-dbcp-1.2.1
tomcat-dbcp.home=$TOPDIR/tomcat-deps
# err, it compiles three above and then appends to the jar, so the file should exist
tomcat-dbcp.jar=$TOPDIR/tomcat-deps/tomcat-dbcp.jar
EOF

%ant \
	-Dcompile.source=1.4

%install
rm -rf $RPM_BUILD_ROOT
cd build/build
TOMCATDIR=$RPM_BUILD_ROOT%{_tomcatdir}
CATALINADIR=$RPM_BUILD_ROOT/var/lib/tomcat

# we don't need dos scripts
rm -f bin/*.bat

randpw=$(echo $RANDOM$$ | md5sum | cut -c 1-15)
sed -i -e s:SHUTDOWN:${randpw}: conf/{server,server-minimal}.xml

install -d $TOMCATDIR/bin \
	    $TOMCATDIR/common/{lib,classes,endorsed} \
	    $TOMCATDIR/server/{lib,classes} \
	    $TOMCATDIR/webapps \
	    $RPM_BUILD_ROOT%{_sysconfdir} \
	    $RPM_BUILD_ROOT%{_logdir}/tomcat \
	    $RPM_BUILD_ROOT%{_vardir}/work \
	    $RPM_BUILD_ROOT/etc/rc.d/init.d

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/tomcat

cp -pR conf/* $RPM_BUILD_ROOT%{_sysconfdir}
cp -HR bin common server $TOMCATDIR

cp -rf  server/webapps	$TOMCATDIR/server
cp -rf  webapps 		$TOMCATDIR
cp -rf	shared		$TOMCATDIR
cp -rf	temp		$TOMCATDIR

ln -sf %{_logdir}/tomcat	$TOMCATDIR/logs
ln -sf %{_vardir}/work		$TOMCATDIR/work
ln -sf %{_sysconfdir}	$TOMCATDIR/conf

# symlinks instead of copies
ln -sf %{_javadir}/commons-daemon.jar	$TOMCATDIR/bin

ln -sf %{_javadir}/activation.jar		$TOMCATDIR/common/lib
ln -sf %{_javadir}/ant.jar			$TOMCATDIR/common/lib
ln -sf %{_javadir}/commons-collections.jar	$TOMCATDIR/common/lib
ln -sf %{_javadir}/commons-dbcp.jar		$TOMCATDIR/common/lib
ln -sf %{_javadir}/commons-logging-api.jar	$TOMCATDIR/common/lib
ln -sf %{_javadir}/commons-pool.jar		$TOMCATDIR/common/lib
ln -sf %{_javadir}/servlet.jar		$TOMCATDIR/common/lib
ln -sf %{_javadir}/servlet.jar		$TOMCATDIR/common/lib/servletapi4.jar
ln -sf %{_javadir}/jdbc-stdext.jar		$TOMCATDIR/common/lib/jdbc2_0-stdext.jar
ln -sf %{_javadir}/jdbc-stdext.jar		$TOMCATDIR/common/lib/jdbc-stdext-2.0.jar
ln -sf %{_javadir}/jmxri.jar			$TOMCATDIR/common/lib
ln -sf %{_javadir}/jndi.jar			$TOMCATDIR/common/lib
ln -sf %{_javadir}/jta.jar			$TOMCATDIR/common/lib
ln -sf %{_javadir}/mail.jar			$TOMCATDIR/common/lib
ln -sf %{_javadir}/jsse.jar			$TOMCATDIR/common/lib
ln -sf %{_javadir}/junit.jar			$TOMCATDIR/common/lib

ln -sf %{_javadir}/mailapi.jar		$TOMCATDIR/common/lib
ln -sf %{_javadir}/pop3.jar			$TOMCATDIR/common/lib
ln -sf %{_javadir}/pop3.jar			$TOMCATDIR/common/lib/pop.jar
ln -sf %{_javadir}/smtp.jar			$TOMCATDIR/common/lib
ln -sf %{_javadir}/imap.jar			$TOMCATDIR/common/lib

ln -sf %{_javadir}/commons-beanutils.jar	$TOMCATDIR/server/lib
ln -sf %{_javadir}/commons-digester.jar	$TOMCATDIR/server/lib
ln -sf %{_javadir}/commons-fileupload.jar	$TOMCATDIR/server/lib
ln -sf %{_javadir}/commons-logging.jar	$TOMCATDIR/server/lib
ln -sf %{_javadir}/commons-modeler.jar	$TOMCATDIR/server/lib
ln -sf %{_javadir}/jaas.jar			$TOMCATDIR/server/lib/jaas.jar
ln -sf %{_javadir}/mx4j-jmx.jar		$TOMCATDIR/server/lib
ln -sf %{_javadir}/regexp.jar		$TOMCATDIR/server/lib
ln -sf %{_javadir}/regexp.jar		$TOMCATDIR/server/lib/jakarta-regexp-1.2.jar
ln -sf %{_javadir}/regexp.jar		$TOMCATDIR/server/lib/regexp-1.2.jar

ln -sf %{_javadir}/jaxp_parser_impl.jar	$TOMCATDIR/common/endorsed
ln -sf %{_javadir}/xml-commons-apis.jar	$TOMCATDIR/common/endorsed

ln -sf %{_javadir}/struts.jar $TOMCATDIR/server/webapps/admin/WEB-INF/lib

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%groupadd -g 51 -r -f http
%useradd -u 51 -r -d /home/services/httpd -s /bin/false -c "HTTP User" -g http http

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
	%userremove http
	%groupremove http
fi

%files
%defattr(644,root,root,755)
%doc build/{RELEASE-NOTES,RUNNING.txt}
# tomcat wants to regenerate tomcat-users.xml
%dir %attr(775,root,http) %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(754,root,root) /etc/rc.d/init.d/tomcat
%dir %{_tomcatdir}
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
%{_tomcatdir}/conf
%{_tomcatdir}/logs
%dir %{_tomcatdir}/server
%dir %{_tomcatdir}/server/classes
%{_tomcatdir}/server/lib
%{_tomcatdir}/server/webapps
%{_tomcatdir}/webapps
%{_tomcatdir}/work
%{_tomcatdir}/shared
%{_tomcatdir}/temp
%dir %{_vardir}
%dir %attr(1730,root,http) %{_vardir}/work
%dir %attr(1730,root,http) %{_logdir}/tomcat

%if 0
%files doc
%defattr(644,root,root,755)
%doc catalina/docs/*
%endif
