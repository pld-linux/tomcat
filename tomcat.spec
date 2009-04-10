# TODO
# - packages for *.renametojar files (-cgi and -ssi in server/lib)
#
# Conditional build:
%bcond_without	javadoc		# skip building javadocs
%bcond_with	jta		# put jta jar into tomcat lib dir.
%bcond_without	java_sun	# build with gcj (does not work)
#
Summary:	Apache Servlet/JSP Engine, RI for Servlet 2.4/JSP 2.0 API
Summary(pl.UTF-8):	Silnik Servlet/JSP Apache będący wzorcową implementacją API Servlet 2.4/JSP 2.0
Name:		apache-tomcat
Version:	5.5.27
Release:	0.3
License:	Apache v2.0
Group:		Networking/Daemons/Java
Source0:	http://www.apache.org/dist/tomcat/tomcat-5/v%{version}/src/%{name}-%{version}-src.tar.gz
# Source0-md5:	eb3f196013550b9b1684e4ff18593a8e
Source1:	%{name}.init
Source2:	%{name}.sysconfig
Source10:	%{name}-context-ROOT.xml
Source11:	%{name}-context-balancer.xml
Source12:	%{name}-context-jsp-examples.xml
Source13:	%{name}-context-tomcat-docs.xml
Source14:	%{name}-context-webdav.xml
Patch0:		%{name}-skip-servletapi.patch
Patch1:		%{name}-nsis.patch
Patch2:		%{name}-native.patch
Patch3:		%{name}-skip-jdt.patch
Patch4:		%{name}-no-connectors.patch
Patch5:		%{name}-dbcp.patch
# this patch is needed for struts >= 1.3
Patch6:		%{name}-struts.patch
URL:		http://tomcat.apache.org/
%if %{with java_sun}
BuildRequires:	java-sun >= 1.5
BuildRequires:	java-sun-jre >= 1.5
%else
BuildRequires:	java-gcj-compat-devel
# BuildRequires:	jsse >= 0:1.0.3
%endif
BuildRequires:	ant >= 1.5.3
BuildRequires:	ant-trax
BuildRequires:	eclipse-jdt
BuildRequires:	jaas
BuildRequires:	jakarta-regexp >= 0:1.3
BuildRequires:	java-commons-beanutils >= 1.7
BuildRequires:	java-commons-collections >= 0:3.1
BuildRequires:	java-commons-collections-tomcat5 >= 0:3.1
BuildRequires:	java-commons-daemon >= 1.0
BuildRequires:	java-commons-dbcp >= 0:1.2.1
BuildRequires:	java-commons-dbcp-tomcat5 >= 0:1.2.1
BuildRequires:	java-commons-digester >= 0:1.7
BuildRequires:	java-commons-el >= 0:1.0
BuildRequires:	java-commons-fileupload >= 0:1.0
BuildRequires:	java-commons-httpclient
BuildRequires:	java-commons-io >= 1.4
BuildRequires:	java-commons-launcher >= 0:0.9
BuildRequires:	java-commons-logging >= 0:1.0.4
BuildRequires:	java-commons-modeler >= 2.0
BuildRequires:	java-commons-pool >= 0:1.2
BuildRequires:	java-commons-pool-tomcat5 >= 0:1.2
%{?with_jta:BuildRequires:	java-jta >= 0:1.0.1}
BuildRequires:	java-log4j
BuildRequires:	java-puretls
BuildRequires:	java-servletapi5 = %{version}
#BuildRequires:	java-struts >= 0:1.2.7
BuildRequires:	java-struts >= 1.0.2
BuildRequires:	java-xerces >= 0:2.7.1
BuildRequires:	java-xml-commons
#BuildRequires:	java-xml-commons >= 1.3
BuildRequires:	java-mail >= 0:1.3.1
BuildRequires:	jaxp_parser_impl >= 0:2.7.1
BuildRequires:	jdbc-stdext >= 0:2.0
BuildRequires:	jmx
BuildRequires:	jndi >= 0:1.2.1
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
#Requires:	jaf >= 1.0.1
Requires:	java-commons-beanutils
Requires:	java-commons-collections
#Requires:	java-commons-dbcp-tomcat5
Requires:	java-commons-digester
Requires:	java-commons-el
#Requires:	java-commons-fileupload
Requires:	java-commons-logging
Requires:	java-commons-modeler
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
Provides:	group(tomcat)
Provides:	java-servlet-container
Provides:	user(tomcat)
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
Summary(pl.UTF-8):	Dokumentacja do Tomcata - kontenera Servlet/JSP
Group:		Documentation
Obsoletes:	jakarta-tomcat-doc

%description doc
The Tomcat Servlet/JSP Container documentation.

%description doc -l pl.UTF-8
Dokumentacja do Tomcata - kontenera Servlet/JSP.

%package admin
Summary:	Apache Tomcat`s Administration Web Application
Summary(pl.UTF-8):	Panel Administracyjny dla Apache Tomcat
Group:		Networking/Daemons/Java/Servlets
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

%description jasper
Jasper is Java ServerPages compiler used by Apache Tomcat servlet
container.

%description jasper -l pl.UTF-8
Jasper jest kompilatorem Java ServerPages używanym przez kontener
servletów Apache Tomcat.

%prep
%setup -q -n %{name}-%{version}-src
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

# servletapi built from jakarta-servletapi5.spec
rm -rf servletapi

# Remove pre-built jars
find -name '*.jar' | xargs rm -fv

%build
TOPDIR=$(pwd)

%if 0
# build jasper javadocs
cd jasper
CLASSPATH=$(build-classpath xml-commons-apis)
# building jasper needs eclipse classes
cat > build.properties <<EOF
ant.jar=$(find-jar ant)
servlet-api.jar=$(find-jar servlet-api)
jsp-api.jar=$(find-jar jsp-api)
tools.jar=%{java_home}/lib/tools.jar
xercesImpl.jar=$(find-jar jaxp_parser_impl)
xmlParserAPIs.jar=$(find-jar xml-commons-apis)
commons-collections.jar=$(find-jar commons-collections)
commons-logging.jar=$(find-jar commons-logging)
commons-daemon.jar=$(find-jar commons-daemon)
junit.jar=$(find-jar junit)
commons-el.jar=$(find-jar commons-el)
EOF
#%ant dist

%if %{with javadoc}
%ant javadoc \
	-Dcompile.source=1.4 \
	-Dbuild.compiler=modern \

%endif
cd -
%endif

# build tomcat 5.5
# XXX build process should fail if one of these find-jar commands fails
#	 how to fix that?
cat > build.properties <<EOF
commons-beanutils.jar=$(find-jar commons-beanutils-core)
commons-launcher.jar=$(find-jar commons-launcher)
commons-daemon.jar=$(find-jar commons-daemon)
commons-digester.jar=$(find-jar commons-digester)
commons-el.jar=$(find-jar commons-el)
commons-logging-api.jar=$(find-jar commons-logging-api)
commons-logging.jar=$(find-jar commons-logging)
commons-modeler.jar=$(find-jar commons-modeler)
xercesImpl.jar=$(find-jar jaxp_parser_impl)
xml-apis.jar=$(find-jar xml-commons-apis)
jdt.jar=$(find-jar org.eclipse.jdt.core)
jasper-compiler-jdt.home=$TOPDIR/tomcat-deps
commons-httpclient.jar=$(find-jar commons-httpclient)
commons-collections.jar=$(find-jar commons-collections)
commons-fileupload.jar=$(find-jar commons-fileupload)
commons-io.jar=$(find-jar commons-io)
jmx.jar=$(find-jar jmx)
jmx-tools.jar=$(find-jar jmx)
junit.jar=$(find-jar junit)
struts.jar=$(find-jar struts-core)
struts-core.jar=$(find-jar struts-core)
struts-taglib.jar=$(find-jar struts-taglib)
jcert.jar=$(find-jar jcert)
jnet.jar=$(find-jar jnet)
jsse.jar=$(find-jar jsse)
%{?with_jta:jta.jar=$(find-jar jta)}
puretls.jar=$(find-jar puretls)
servlet-api.jar=$(find-jar servlet-api)
servletapi.build.notrequired=true
jsp-api.jar=$(find-jar jsp-api)
jspapi.build.notrequired=true
log4j.jar=$(find-jar log4j)
tomcat-dbcp.jar=$(find-jar commons-dbcp-tomcat5)
struts.lib=%{_javadir}-struts
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
%{__sed} -i -e "s:SHUTDOWN:${randpw}:" conf/{server,server-minimal}.xml

install -d $TOMCATDIR/bin \
	    $TOMCATDIR/common/{lib,classes,endorsed} \
	    $TOMCATDIR/server/{lib,classes} \
	    $TOMCATDIR/webapps \
	    $RPM_BUILD_ROOT%{_logdir}/tomcat \
	    $RPM_BUILD_ROOT%{_vardir}/webapps \
	    $RPM_BUILD_ROOT%{_vardir}/work \
	    $RPM_BUILD_ROOT%{_vardir}/conf \
	    $RPM_BUILD_ROOT/etc/sysconfig \
	    $RPM_BUILD_ROOT/etc/rc.d/init.d

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/tomcat
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/tomcat

cp -pR conf/* $CATALINADIR/conf
install %{SOURCE10} $CATALINADIR/conf/Catalina/localhost/ROOT.xml
install %{SOURCE11} $CATALINADIR/conf/Catalina/localhost/balancer.xml
install %{SOURCE12} $CATALINADIR/conf/Catalina/localhost/jsp-examples.xml
install %{SOURCE13} $CATALINADIR/conf/Catalina/localhost/tomcat-docs.xml
install %{SOURCE14} $CATALINADIR/conf/Catalina/localhost/webdav.xml
cp -HR bin common server $TOMCATDIR

cp -rf server/webapps $TOMCATDIR/server
cp -rf webapps $TOMCATDIR
cp -rf shared $TOMCATDIR
cp -rf temp $CATALINADIR

ln -sf %{_logdir}/tomcat $CATALINADIR/logs
ln -sf %{_vardir}/work $TOMCATDIR/work
ln -sf %{_vardir}/conf $TOMCATDIR/conf
ln -sf %{_vardir}/conf $RPM_BUILD_ROOT%{_sysconfdir}

# symlinks instead of copies
ln -sf $(find-jar commons-el) $TOMCATDIR/common/lib/commons-el.jar
ln -sf $(find-jar jakarta-commons-dbcp-tomcat5) $TOMCATDIR/common/lib/jakarta-commons-dbcp-tomcat5.jar
ln -sf $(find-jar servlet-api) $TOMCATDIR/common/lib/servlet-api.jar
ln -sf $(find-jar jsp-api) $TOMCATDIR/common/lib/jsp-api.jar

ln -sf $(find-jar commons-modeler) $TOMCATDIR/server/lib/commons-modeler.jar

ln -sf $(find-jar jaxp_parser_impl) $TOMCATDIR/common/endorsed/jaxp_parser_impl.jar
ln -sf $(find-jar xml-commons-apis) $TOMCATDIR/common/endorsed/xml-commons-apis.jar
ln -sf $(find-jar struts) $TOMCATDIR/server/webapps/admin/WEB-INF/lib/struts.jar
ln -sf $(find-jar commons-collections) $TOMCATDIR/server/webapps/admin/WEBINF/lib/commons-collections.jar
ln -sf $(find-jar commons-beanutils-core) $TOMCATDIR/server/webapps/admin/WEBINF/lib/commons-beanutils-core.jar
ln -sf $(find-jar commons-digester) $TOMCATDIR/server/webapps/admin/WEBINF/lib/commons-digester.jar
ln -sf $(find-jar commons-chain) $TOMCATDIR/server/webapps/admin/WEBINF/lib/commons-chain.jar

%if 0
# do not make these symlinks as ant didn't do
ln -sf $(find-jar commons-daemon) $TOMCATDIR/bin/commons-daemon.jar
ln -sf $(find-jar activation) $TOMCATDIR/common/lib/activation.jar
ln -sf $(find-jar ant) $TOMCATDIR/common/lib/ant.jar
ln -sf $(find-jar commons-dbcp) $TOMCATDIR/common/lib/commons-dbcp.jar
ln -sf $(find-jar commons-logging-api) $TOMCATDIR/common/lib/commons-logging-api.jar
ln -sf $(find-jar commons-pool) $TOMCATDIR/common/lib/commons-pool.jar
ln -sf $(find-jar servlet) $TOMCATDIR/common/lib/servlet.jar
ln -sf $(find-jar servlet) $TOMCATDIR/common/lib/servletapi4.jar
ln -sf $(find-jar jdbc-stdext) $TOMCATDIR/common/lib/jdbc-stdext.jar
ln -sf jdbc-stdext.jar $TOMCATDIR/common/lib/jdbc2_0-stdext.jar
ln -sf jdbc-stdext.jar $TOMCATDIR/common/lib/jdbc-stdext-2.0.jar
ln -sf $(find-jar jmxri) $TOMCATDIR/common/lib/jmxri.jar
ln -sf $(find-jar jndi) $TOMCATDIR/common/lib/jndi.jar
%{?with_jta:ln -sf $(find-jar jta) $TOMCATDIR/common/lib/jta.jar}
ln -sf $(find-jar mail) $TOMCATDIR/common/lib/mail.jar
ln -sf $(find-jar jsse) $TOMCATDIR/common/lib/jsse.jar
ln -sf $(find-jar junit) $TOMCATDIR/common/lib/junit.jar
ln -sf $(find-jar mailapi) $TOMCATDIR/common/lib/mailapi.jar
ln -sf $(find-jar pop3) $TOMCATDIR/common/lib/pop3.jar
ln -sf pop3.jar $TOMCATDIR/common/lib/pop.jar
ln -sf $(find-jar smtp) $TOMCATDIR/common/lib/smtp.jar
ln -sf $(find-jar imap) $TOMCATDIR/common/lib/imap.jar
ln -sf $(find-jar commons-beanutils) $TOMCATDIR/server/lib/commons-beanutils.jar
ln -sf $(find-jar commons-digester) $TOMCATDIR/server/lib/commons-digester.jar
ln -sf $(find-jar commons-fileupload) $TOMCATDIR/server/lib/commons-fileupload.jar
ln -sf $(find-jar commons-logging) $TOMCATDIR/server/lib/commons-logging.jar
ln -sf $(find-jar jaas) $TOMCATDIR/server/lib/jaas.jar
ln -sf $(find-jar regexp) $TOMCATDIR/server/lib/regexp.jar
ln -sf $(find-jar regexp) $TOMCATDIR/server/lib/jakarta-regexp-1.2.jar
ln -sf $(find-jar regexp) $TOMCATDIR/server/lib/regexp-1.2.jar
%endif

ln -sf $(find-jar jaxp_parser_impl) $TOMCATDIR/common/endorsed/jaxp_parser_impl.jar
ln -sf $(find-jar xml-commons-apis) $TOMCATDIR/common/endorsed/xml-commons-apis.jar
ln -sf $(find-jar struts-core) $TOMCATDIR/server/webapps/admin/WEB-INF/lib/struts-core.jar

install -d $RPM_BUILD_ROOT%{_javadir}
mv $TOMCATDIR/common/lib/jasper* $RPM_BUILD_ROOT%{_javadir}
ln -sf %{_javadir}/jasper-compiler-jdt.jar $TOMCATDIR/common/lib/
ln -sf %{_javadir}/jasper-compiler.jar $TOMCATDIR/common/lib/
ln -sf %{_javadir}/jasper-runtime.jar $TOMCATDIR/common/lib/

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%groupadd -g 234 -r -f tomcat
%useradd -u 234 -r -d /var/lib/tomcat -s /bin/false -c "Tomcat User" -g tomcat tomcat

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
%{_tomcatdir}/server/webapps/host-manager
%{_tomcatdir}/server/webapps/manager
%{_tomcatdir}/webapps
%{_tomcatdir}/work
%{_tomcatdir}/shared
%dir %{_vardir}
%dir %{_vardir}/conf/Catalina
%dir %{_vardir}/conf/Catalina/localhost
# tomcat config has to be writeable because of tomacta-users.xml file and Catalina dir
%config(noreplace) %attr(664,root,tomcat) %verify(not md5 mtime size) %{_vardir}/conf/MANIFEST.MF
%config(noreplace) %attr(664,root,tomcat) %verify(not md5 mtime size) %{_vardir}/conf/catalina.policy
%config(noreplace) %attr(664,root,tomcat) %verify(not md5 mtime size) %{_vardir}/conf/*.properties*
%config(noreplace) %attr(664,root,tomcat) %verify(not md5 mtime size) %{_vardir}/conf/*.manifest
%config(noreplace) %attr(664,root,tomcat) %verify(not md5 mtime size) %{_vardir}/conf/*.xml
%config(noreplace) %attr(664,root,tomcat) %verify(not md5 mtime size) %{_vardir}/conf/Catalina/localhost/balancer.xml
%config(noreplace) %attr(664,root,tomcat) %verify(not md5 mtime size) %{_vardir}/conf/Catalina/localhost/host-manager.xml
%config(noreplace) %attr(664,root,tomcat) %verify(not md5 mtime size) %{_vardir}/conf/Catalina/localhost/jsp-examples.xml
%config(noreplace) %attr(664,root,tomcat) %verify(not md5 mtime size) %{_vardir}/conf/Catalina/localhost/manager.xml
%config(noreplace) %attr(664,root,tomcat) %verify(not md5 mtime size) %{_vardir}/conf/Catalina/localhost/ROOT.xml
%config(noreplace) %attr(664,root,tomcat) %verify(not md5 mtime size) %{_vardir}/conf/Catalina/localhost/tomcat-docs.xml
%config(noreplace) %attr(664,root,tomcat) %verify(not md5 mtime size) %{_vardir}/conf/Catalina/localhost/webdav.xml
%dir %attr(1730,root,tomcat) %{_vardir}/work
%dir %attr(775,root,tomcat) %{_vardir}/webapps
%dir %attr(775,root,tomcat) %{_vardir}/temp
%dir %attr(775,root,tomcat) %{_logdir}/tomcat
%{_vardir}/logs

%if 0
%files doc
%defattr(644,root,root,755)
%doc catalina/docs/*
%endif

%files admin
%defattr(644,root,root,755)
%config(noreplace) %attr(664,root,tomcat) %verify(not md5 mtime size) %{_vardir}/conf/Catalina/localhost/admin.xml
%{_tomcatdir}/server/webapps/admin

%files jasper
%defattr(644,root,root,755)
%{_javadir}/jasper-compiler-jdt.jar
%{_javadir}/jasper-compiler.jar
%{_javadir}/jasper-runtime.jar
