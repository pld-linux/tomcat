
# Conditional build:
%bcond_without	javadoc		# skip building javadocs

%define		jspapiver	2.2
%define		servletapiver	3.0

# Java Commons Logging version. Must be >= 1.1.
%define		jclver	1.1.3

%include	/usr/lib/rpm/macros.java
Summary:	Web server and Servlet/JSP Engine, RI for Servlet %{servletapiver}/JSP %{jspapiver} API
Summary(pl.UTF-8):	Serwer www i silnik Servlet/JSP będący wzorcową implementacją API Servlet %{servletapiver}/JSP %{jspapiver}
Name:		tomcat
Version:	7.0.40
Release:	1
License:	Apache v2.0
Group:		Networking/Daemons/Java
Source0:	http://www.apache.org/dist/tomcat/tomcat-7/v%{version}/src/apache-%{name}-%{version}-src.tar.gz
# Source0-md5:	158df72e6c046fa5d46a691a7c0805e6
Source1:	apache-%{name}.init
Source2:	apache-%{name}.sysconfig
Source3:	%{name}-build.properties
Source10:	%{name}-context-ROOT.xml
Source11:	%{name}-context-docs.xml
Source12:	%{name}-context-manager.xml
Source13:	%{name}-context-host-manager.xml
Source14:	%{name}-context-examples.xml
Source100:	http://www.apache.org/dist/commons/logging/source/commons-logging-%{jclver}-src.tar.gz
# Source100-md5:	e8e197d628436490886d17cffa108fe3
Patch0:		%{name}-build.xml.patch
Patch1:		server.xml-URIEncoding-utf8.patch
Patch2:		%{name}-LDAPUserDatabase.patch
Patch3:		%{name}-catalina.policy-javadir.patch
Patch4:		%{name}-userdir.patch
Patch100:	jcl-build.xml.patch
URL:		http://tomcat.apache.org/
BuildRequires:	ant >= 1.5.3
BuildRequires:	eclipse-jdt >= 3.2
BuildRequires:	java(JSR109)
BuildRequires:	java-avalon-logkit
BuildRequires:	java-commons-daemon >= 1.0
BuildRequires:	java-commons-dbcp-tomcat5 >= 0:1.1
BuildRequires:	java-commons-pool-tomcat5
BuildRequires:	java-geronimo-spec-jaxrpc
BuildRequires:	java-jdbc-mysql
BuildRequires:	java-junit
BuildRequires:	java-log4j
BuildRequires:	java-mail
BuildRequires:	jdk
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.553
BuildRequires:	sed >= 4.0
Requires(post,preun):	/sbin/chkconfig
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires:	java(jaxp_parser_impl)
Requires:	java(jndi) >= 1.2.1
Requires:	java-%{name}-catalina = %{version}-%{release}
Requires:	java-%{name}-coyote = %{version}-%{release}
Requires:	java-%{name}-jasper = %{version}-%{release}
Requires:	java-commons-dbcp-tomcat5 >= 0:1.1
Requires:	java-commons-pool-tomcat5
Requires:	java-jdbc-mysql
Requires:	java-mail
Requires:	java-servletapi = %{version}-%{release}
Requires:	jpackage-utils
Requires:	jre >= 1.2
Requires:	jsvc
Requires:	rc-scripts
Suggests:	tomcat-native
Provides:	group(servlet)
Provides:	group(tomcat)
Provides:	user(tomcat)
Obsoletes:	apache-tomcat
Obsoletes:	jakarta-tomcat
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_tomcatdir	%{_datadir}/tomcat
%define 	_logdir		%{_var}/log
%define		_vardir		%{_var}/lib/tomcat

%define find_jar() %{expand:%%define jarfile {%(jar=$(find-jar %1); echo ${jar:-%%nil})}}%{?jarfile}%{!?jarfile:%{error:find-jar %1 failed}}%{nil}

%description
Tomcat is the servlet container that is used in the official Reference
Implementation for the Java Servlet and JavaServer Pages technologies.
The Java Servlet and JavaServer Pages specifications are developed by
Sun under the Java Community Process.

Tomcat is developed in an open and participatory environment and
released under the Apache Software License. Tomcat is intended to be a
collaboration of the best-of-breed developers from around the world.

%description -l pl.UTF-8
Tomcat to kontener serwletowy używany przez oficjalną implementację
wzorcową technologii Java Servlet i JavaServer Pages. Specyfikacje
Java Servlet i JavaServer Pages są rozwijane przez Suna zgodnie z Java
Community Process.

%package webapp-docs
Summary:	The Apache Tomcat Servlet/JSP Container documentation
Summary(pl.UTF-8):	Dokumentacja do Tomcata - kontenera Servlet/JSP
Group:		Documentation
Obsoletes:	apache-tomcat-doc
Obsoletes:	jakarta-tomcat-doc
Obsoletes:	tomcat-doc

%description webapp-docs
The Tomcat Servlet/JSP Container documentation.

%description webapp-docs -l pl.UTF-8
Dokumentacja do Tomcata - kontenera Servlet/JSP.

%package webapp-manager
Summary:	The Apache Tomcat Servlet/JSP application manager
Summary(pl.UTF-8):	Zarządca aplikacji w Tomcacie
Group:		Networking/Daemons/Java/Servlets
Requires:	%{name} = %{version}-%{release}

%description webapp-manager
The Apache Tomcat Servlet/JSP application manager.

%description webapp-manager -l pl.UTF-8
Zarządca aplikacji w Tomcacie.

%package webapp-host-manager
Summary:	The Apache Tomcat Servlet/JSP virtual hosts manager
Summary(pl.UTF-8):	Zarządca wirtualnych hostów w Tomcacie
Group:		Networking/Daemons/Java/Servlets
Requires:	%{name} = %{version}-%{release}
Obsoletes:	tomcat-admin

%description webapp-host-manager
The Apache Tomcat Servlet/JSP virtual hosts manager.

%description webapp-host-manager -l pl.UTF-8
Zarządca wirtualnych hostów w Tomcacie.

%package webapp-examples
Summary:	The Apache Tomcat Servlet/JSP example applications
Summary(pl.UTF-8):	Przykładowe aplikacje dla Tomcata
Group:		Networking/Daemons/Java/Servlets
Requires:	%{name} = %{version}-%{release}

%description webapp-examples
The Apache Tomcat Servlet/JSP example applications.

%description webapp-examples -l pl.UTF-8
Przykładowe aplikacje dla Tomcata.

%package webservices
Summary:	Web Services support (JSR 109)
Summary(pl.UTF-8):	Wsparcie dla Web Services (JSR 109)
Group:		Libraries/Java
Requires:	%{name} = %{version}-%{release}
Requires:	java(JSR109)
Requires:	java-geronimo-spec-jaxrpc

%description webservices
Factories for JSR 109 which may be used to resolve web services
references.

%description webservices -l pl.UTF-8
Wsparcie dla JSR 109 (Web Services).

%package jmx
Summary:	JMX remote interface for Tomcat
Summary(pl.UTF-8):	Zdalny interfejs JMX dla Tomcata
Group:		Libraries/Java
Requires:	%{name} = %{version}-%{release}

%description jmx
JMX remote interface for Tomcat.

%description jmx -l pl.UTF-8
Zdalny interfejs JMX dla Tomcata.

%package -n java-tomcat-catalina
Summary:	Tomcat's servlet engine
Summary(pl.UTF-8):	Silnik servletów dla Tomcata.
Group:		Libraries/Java
Requires:	jpackage-utils

%description -n java-tomcat-catalina
Catalina is Tomcat's servlet container. Catalina implements Sun
Microsystems' specifications for servlet and JavaServer Pages (JSP).

%description -n java-tomcat-catalina -l pl.UTF-8
Bibliotek Javy zawierające silnik servletów i JSP tomcata.

%package -n java-tomcat-coyote
Summary:	Tomcat HTTP connector
Summary(pl.UTF-8):	Interfejs HTTP dla Tomcata
Group:		Libraries/Java
Requires:	jpackage-utils

%description -n java-tomcat-coyote
Coyote is Tomcat's HTTP Connector component that supports the HTTP 1.1
protocol for the web server or application container. Coyote listens
for incoming connections on a specific TCP port on the server and
forwards the request to the Tomcat Engine to process the request and
send back a response to the requesting client.

%description -n java-tomcat-coyote -l pl.UTF-8
Biblioteki Javy zawierające serwer HTTP 1.1 dla Tomcata.

%package -n java-tomcat-jasper
Summary:	JSP compiler
Summary(pl.UTF-8):	Kompilator JSP
Group:		Libraries/Java
Requires:	java-eclipse-jdt >= 3.2
Requires:	jpackage-utils
Obsoletes:	apache-tomcat-jasper
Obsoletes:	tomcat-jasper

%description -n java-tomcat-jasper
Jasper is Java ServerPages compiler used by Apache Tomcat servlet
container.

%description -n java-tomcat-jasper -l pl.UTF-8
Jasper jest kompilatorem Java ServerPages używanym przez kontener
servletów Apache Tomcat.

%package -n java-servletapi
Summary:	Java servlet and JSP implementation classes
Summary(pl.UTF-8):	Klasy z implementacją Java Servlet i JSP
Group:		Libraries/Java
Provides:	java(jsp) = %{jspapiver}
Provides:	java(servlet) = %{servletapiver}
Obsoletes:	jakarta-servletapi5
Obsoletes:	jakarta-servletapi5
Obsoletes:	java-servletapi5

%description -n java-servletapi
Implementation classes of the Java Servlet and JSP APIs (packages
javax.servlet, javax.servlet.http, javax.servlet.jsp, and
javax.servlet.jsp.tagext).

%description -n java-servletapi -l pl.UTF-8
Implementacje klas API Java Servlet i JSP (pakiety javax.servlet,
javax.servlet.http, javax.servlet.jsp i java.servlet.jsp.tagext).

%prep
%setup -q -a100 -n apache-%{name}-%{version}-src
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

# Prepare java-commmons-logging sources
mkdir -p output/extras/logging
mv commons-logging-%{jclver}-src output/extras/logging
cd output/extras/logging/commons-logging-%{jclver}-src
%undos build.xml
%patch100 -p1
cd -

# we don't need those scripts
rm bin/*.bat
rm bin/{startup,shutdown}.sh

cp -a %{SOURCE3} build.properties
cat >>build.properties <<EOF

log4j.jar=%(find-jar log4j)
log4j12.jar=%(find-jar log4j)
junit.jar=%(find-jar junit)
logkit.jar=%(find-jar avalon-logkit)
avalon-framework-impl.jar=%(find-jar avalon-framework-impl.jar)
avalon-framework-api.jar=%(find-jar avalon-framework-api.jar)
servletapi.jar=$(pwd)/output/build/lib/servlet-api.jar
EOF

%build
export LC_ALL=en_US

# Base package
%ant \
	-Drpm.javadir=%{_javadir} \
	-Drpm.libdir=%{_libdir}

# Extras
mkdir -p output/extras/webservices

ln -sf %{_javadir}/geronimo-spec-jaxrpc.jar output/extras/webservices/jaxrpc.jar
ln -sf %{_javadir}/jsr109.jar output/extras/webservices/wsdl4j.jar

%ant -Dcommons-logging-version=%{jclver} extras

# Javadoc
%if %{with javadoc}
%ant javadoc
%endif

%install
rm -rf $RPM_BUILD_ROOT
cd output/build

TOMCATDIR=$RPM_BUILD_ROOT%{_tomcatdir}
CATALINADIR=$RPM_BUILD_ROOT/var/lib/tomcat

# useful for constructing relative symlinks. Is there a better way?
TOMCATDIRREV=$(echo %{_tomcatdir} | sed 's#[^/]\+#..#g;s#^/##')
CATALINADIRREV=$(echo /var/lib/tomcat | sed 's#[^/]\+#..#g;s#^/##')
SYSCONFDIRREV=$(echo %{_sysconfdir} | sed 's#[^/]\+#..#g;s#^/##')

install -d $TOMCATDIR \
	    $CATALINADIR/temp \
	    $RPM_BUILD_ROOT%{_vardir}/webapps \
	    $RPM_BUILD_ROOT%{_vardir}/work \
	    $RPM_BUILD_ROOT%{_vardir}/conf \
	    $RPM_BUILD_ROOT%{_logdir}/tomcat \
	    $RPM_BUILD_ROOT/etc/sysconfig \
	    $RPM_BUILD_ROOT/etc/rc.d/init.d

install -p %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/tomcat
cp -a %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/tomcat

cp -a conf/* $CATALINADIR/conf
install -d $CATALINADIR/conf/Catalina/localhost
cp -a %{SOURCE10} $CATALINADIR/conf/Catalina/localhost/ROOT.xml
cp -a %{SOURCE11} $CATALINADIR/conf/Catalina/localhost/docs.xml
cp -a %{SOURCE12} $CATALINADIR/conf/Catalina/localhost/manager.xml
cp -a %{SOURCE13} $CATALINADIR/conf/Catalina/localhost/host-manager.xml
cp -a %{SOURCE14} $CATALINADIR/conf/Catalina/localhost/examples.xml

cp -a bin lib webapps $TOMCATDIR
cp -a temp $CATALINADIR

ln -sf $CATALINADIRREV%{_logdir}/tomcat $CATALINADIR/logs
ln -sf $TOMCATDIRREV%{_logdir}/tomcat $TOMCATDIR/logs
ln -sf $TOMCATDIRREV%{_vardir}/work $TOMCATDIR/work
ln -sf $TOMCATDIRREV%{_vardir}/conf $TOMCATDIR/conf
ln -sf $SYSCONFDIRREV%{_vardir}/conf $RPM_BUILD_ROOT%{_sysconfdir}/tomcat

# symlinks instead of copies
jars="commons-daemon commons-logging-api"
for jar in $jars; do
	jar=$(find-jar $jar)
	ln -sf $jar $TOMCATDIR/bin
done

jars="commons-pool-tomcat5 commons-dbcp-tomcat5 mysql-connector-java org.eclipse.jdt.core mail"
for jar in $jars; do
	jar=$(find-jar $jar)
	ln -sf $jar $TOMCATDIR/lib
done

install -d $RPM_BUILD_ROOT%{_javadir}
mv $TOMCATDIR/lib/jasper*.jar $RPM_BUILD_ROOT%{_javadir}
mv $TOMCATDIR/lib/jsp-api.jar $RPM_BUILD_ROOT%{_javadir}/jsp-api-%{jspapiver}.jar
mv $TOMCATDIR/lib/servlet-api.jar $RPM_BUILD_ROOT%{_javadir}/servlet-api-%{servletapiver}.jar
mv $TOMCATDIR/lib/catalina.jar $RPM_BUILD_ROOT%{_javadir}/tomcat-catalina.jar
mv $TOMCATDIR/lib/tomcat-coyote.jar $RPM_BUILD_ROOT%{_javadir}/tomcat-coyote.jar
mv $TOMCATDIR/lib/tomcat-util.jar $RPM_BUILD_ROOT%{_javadir}/tomcat-util.jar
mv $TOMCATDIR/lib/tomcat-api.jar $RPM_BUILD_ROOT%{_javadir}/tomcat-api.jar

ln -s jsp-api-%{jspapiver}.jar $RPM_BUILD_ROOT%{_javadir}/jsp-api.jar
ln -s servlet-api-%{servletapiver}.jar $RPM_BUILD_ROOT%{_javadir}/servlet-api.jar

# XXX add softlinks jasper-compiler.jar and jasper-runtime for compatibility with tomcat 5.5?
ln -sf %{_javadir}/jasper-el.jar $TOMCATDIR/lib
ln -sf %{_javadir}/jasper.jar $TOMCATDIR/lib

ln -sf %{_javadir}/jsp-api-%{jspapiver}.jar $TOMCATDIR/lib/jsp-api.jar
ln -sf %{_javadir}/servlet-api-%{servletapiver}.jar $TOMCATDIR/lib/servlet-api.jar

ln -sf %{_javadir}/tomcat-catalina.jar $TOMCATDIR/lib/catalina.jar
ln -sf %{_javadir}/tomcat-util.jar $TOMCATDIR/lib/util.jar
ln -sf %{_javadir}/tomcat-api.jar $TOMCATDIR/lib/api.jar

ln -sf %{_javadir}/tomcat-coyote.jar $TOMCATDIR/lib/tomcat-coyote.jar

cp -a ../extras/catalina-ws.jar $TOMCATDIR/lib/catalina-ws.jar
cp -a ../extras/catalina-jmx-remote.jar $TOMCATDIR/lib/catalina-jmx-remote.jar
cp -a ../extras/tomcat-juli-adapters.jar $RPM_BUILD_ROOT%{_javadir}/tomcat-juli-adapters.jar
cp -a ../extras/tomcat-juli.jar $RPM_BUILD_ROOT%{_javadir}/tomcat-juli.jar
ln -sf %{_javadir}/tomcat-juli-adapters.jar $TOMCATDIR/lib/juli-adapters.jar
ln -sf %{_javadir}/tomcat-juli.jar $TOMCATDIR/lib/juli.jar

ln -s %{_javadir}/geronimo-spec-jaxrpc.jar $TOMCATDIR/lib/jaxrpc.jar
ln -s %{_javadir}/jsr109.jar $TOMCATDIR/lib/jsr109.jar

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
%doc KEYS RELEASE-NOTES
%attr(754,root,root) /etc/rc.d/init.d/tomcat
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/tomcat
%{_sysconfdir}/tomcat
%dir %{_tomcatdir}
%dir %{_tomcatdir}/conf
%dir %{_tomcatdir}/bin
%{_tomcatdir}/bin/catalina-tasks.xml
%attr(755,root,root) %{_tomcatdir}/bin/*.sh
%{_tomcatdir}/bin/*.jar
%dir %{_tomcatdir}/lib
%{_tomcatdir}/lib/annotations-api.jar
%{_tomcatdir}/lib/api.jar
%{_tomcatdir}/lib/catalina-ant.jar
%{_tomcatdir}/lib/catalina-ha.jar
%{_tomcatdir}/lib/catalina.jar
%{_tomcatdir}/lib/catalina-tribes.jar
%{_tomcatdir}/lib/commons-dbcp-tomcat5.jar
%{_tomcatdir}/lib/commons-pool-tomcat5.jar
%{_tomcatdir}/lib/el-api.jar
%{_tomcatdir}/lib/jasper-el.jar
%{_tomcatdir}/lib/jasper.jar
%{_tomcatdir}/lib/jsp-api.jar
%{_tomcatdir}/lib/juli-adapters.jar
%{_tomcatdir}/lib/juli.jar
%{_tomcatdir}/lib/mail.jar
%{_tomcatdir}/lib/mysql-connector-java.jar
%{_tomcatdir}/lib/org.eclipse.jdt.core.jar
%{_tomcatdir}/lib/servlet-api.jar
%{_tomcatdir}/lib/tomcat-jdbc.jar
%{_tomcatdir}/lib/tomcat-coyote.jar
%{_tomcatdir}/lib/tomcat-i18n-es.jar
%{_tomcatdir}/lib/tomcat-i18n-fr.jar
%{_tomcatdir}/lib/tomcat-i18n-ja.jar
%{_tomcatdir}/lib/util.jar

%dir %{_tomcatdir}/webapps

%config(noreplace) %attr(664,root,tomcat) %verify(not md5 mtime size) %{_vardir}/conf/Catalina/localhost/ROOT.xml
%{_tomcatdir}/webapps/ROOT

%{_tomcatdir}/logs
%{_tomcatdir}/work
%dir %attr(770,root,tomcat) %{_vardir}
# these directory has to be writeable because /admin need to modify config
# files and create temporary files
%dir %attr(770,root,tomcat) %{_vardir}/conf
%dir %attr(770,root,tomcat) %{_vardir}/conf/Catalina
%dir %{_vardir}/conf/Catalina/localhost
# tomcat config has to be writeable because of tomcat-users.xml file and Catalina dir
%config(noreplace) %attr(660,root,tomcat) %verify(not md5 mtime size) %{_vardir}/conf/catalina.policy
%config(noreplace) %attr(660,root,tomcat) %verify(not md5 mtime size) %{_vardir}/conf/*.properties*
%config(noreplace) %attr(660,root,tomcat) %verify(not md5 mtime size) %{_vardir}/conf/*.xml
%dir %attr(770,root,tomcat) %{_vardir}/work
%dir %attr(770,root,tomcat) %{_vardir}/webapps
%dir %attr(770,root,tomcat) %{_vardir}/temp
%dir %attr(770,root,tomcat) %{_logdir}/tomcat
%{_vardir}/logs

%files webapp-docs
%defattr(644,root,root,755)
%config(noreplace,missingok) %attr(664,root,tomcat) %verify(not md5 mtime size) %{_vardir}/conf/Catalina/localhost/docs.xml
%{_tomcatdir}/webapps/docs

%files webapp-manager
%defattr(644,root,root,755)
%config(noreplace,missingok) %attr(664,root,tomcat) %verify(not md5 mtime size) %{_vardir}/conf/Catalina/localhost/manager.xml
%{_tomcatdir}/webapps/manager

%files webapp-host-manager
%defattr(644,root,root,755)
%config(noreplace,missingok) %attr(664,root,tomcat) %verify(not md5 mtime size) %{_vardir}/conf/Catalina/localhost/host-manager.xml
%{_tomcatdir}/webapps/host-manager

%files webapp-examples
%defattr(644,root,root,755)
%config(noreplace,missingok) %attr(664,root,tomcat) %verify(not md5 mtime size) %{_vardir}/conf/Catalina/localhost/examples.xml
%{_tomcatdir}/webapps/examples

%files webservices
%defattr(644,root,root,755)
%{_tomcatdir}/lib/catalina-ws.jar
%{_tomcatdir}/lib/jsr109.jar
%{_tomcatdir}/lib/jaxrpc.jar

%files jmx
%defattr(644,root,root,755)
%{_tomcatdir}/lib/catalina-jmx-remote.jar

%files -n java-tomcat-jasper
%defattr(644,root,root,755)
%{_javadir}/jasper-el.jar
%{_javadir}/jasper.jar

%files -n java-tomcat-catalina
%defattr(644,root,root,755)
%{_javadir}/tomcat-api.jar
%{_javadir}/tomcat-catalina.jar
%{_javadir}/tomcat-juli-adapters.jar
%{_javadir}/tomcat-juli.jar
%{_javadir}/tomcat-util.jar

%files -n java-tomcat-coyote
%defattr(644,root,root,755)
%{_javadir}/tomcat-coyote.jar

%files -n java-servletapi
%defattr(644,root,root,755)
%{_javadir}/jsp-api*.jar
%{_javadir}/servlet-api*.jar
