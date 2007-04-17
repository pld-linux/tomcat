#
# Conditional build:
%bcond_with	binary	# build from binary source
%bcond_without	javadoc	# skip building javadocs
#
Summary:	Apache Servlet/JSP Engine, RI for Servlet 2.4/JSP 2.0 API
Summary(pl.UTF-8):	Silnik Servlet/JSP Apache będący wzorcową implementacją API Servlet 2.4/JSP 2.0
Name:		apache-tomcat
Version:	5.5.23
Release:	0.1
License:	Apache
Group:		Development/Languages/Java
#Source0:	http://www.apache.org/dist/tomcat/tomcat-5/v5.0.30/src/%{name}-%{version}-src.tar.gz
Source0:	http://www.apache.org/dist/tomcat/tomcat-5/v%{version}/src/%{name}-%{version}-src.tar.gz
# Source0-md5:	362d1d8b15dc09882440dcab8c592dd7
#Source0:	http://apache.zone-h.org/
Source1:	%{name}.init
Patch0:		%{name}-skip-servletapi.patch
Patch1:		%{name}-nsis.patch
Patch2:		%{name}-native.patch
Patch3:		%{name}-skip-jdt.patch
URL:		http://tomcat.apache.org/
# required:
BuildRequires:	ant >= 1.5.3
BuildRequires:	jaas
BuildRequires:	jakarta-commons-beanutils
BuildRequires:	jakarta-commons-collections
BuildRequires:	jakarta-commons-collections-source
BuildRequires:	jakarta-commons-daemon
BuildRequires:	jakarta-commons-dbcp
BuildRequires:	jakarta-commons-dbcp-source
BuildRequires:	jakarta-commons-digester
BuildRequires:	jakarta-commons-fileupload
BuildRequires:	jakarta-commons-httpclient
BuildRequires:	jakarta-commons-logging
BuildRequires:	jakarta-commons-modeler >= 2.0
BuildRequires:	jakarta-commons-pool
BuildRequires:	jakarta-commons-pool-source
BuildRequires:	jakarta-regexp
BuildRequires:	jakarta-servletapi5
BuildRequires:	jakarta-struts >= 1.0.2
BuildRequires:	jaxp_parser_impl
BuildRequires:	jdk >= 1.5
BuildRequires:	jpackage-utils
BuildRequires:	mx4j >= 1.1.1
BuildRequires:	puretls
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	xerces-j
%if %{with javadoc}
BuildRequires:	commons-el
%endif
# optional:
BuildRequires:	jaf >= 1.0.1
BuildRequires:	jakarta-commons-dbcp
BuildRequires:	jakarta-commons-pool
BuildRequires:	javamail >= 1.2
BuildRequires:	jdbc-stdext >= 2.0
BuildRequires:	jndi >= 1.2.1
BuildRequires:	jsse >= 1.0.2
BuildRequires:	jta >= 1.0.1
BuildRequires:	junit >= 3.7
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	tyrex >= 1.0
BuildRequires:	xml-commons
Requires(post,postun):	/sbin/ldconfig
Requires(post,preun):	/sbin/chkconfig
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires:	jaas
Requires:	jaf >= 1.0.1
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
Requires:	tyrex >= 1.0
Requires:	xml-commons
Provides:	group(http)
Provides:	user(http)
Obsoletes:	jakarta-tomcat
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_tomcatdir	%{_libdir}/tomcat
%define 	_logdir		%{_var}/log
%define		_vardir		%{_var}/lib/tomcat

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

# servletapi built from jakarta-servletapi5
rm -rf servletapi

# Remove pre-built jars
find -name '*.jar' | xargs rm -fv

%build
TOPDIR=$(pwd)
#xerces.jar=$(build-classpath xerces)
#jasper-compiler-jdt.jar=$(build-classpath jdtcore)

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
#cd build
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
%if 0
jdt.jar=${jdt.lib}/org.eclipse.jdt.core_3.1.2.jar
log4j.jar=${log4j.lib}/dist/lib/log4j-1.2.12.jar
%endif
commons-httpclient.jar=$(build-classpath commons-httpclient)
commons-collections.jar=$(build-classpath commons-collections)
commons-fileupload.jar=$(build-classpath commons-fileupload)


%if 0
jmx.jar=${jmx.lib}/mx4j.jar
%endif
jmx.jar=$(build-classpath jre/jmx)
%if 0
jmx-tools.jar=${jmx.lib}/mx4j-tools.jar
%endif
jmx-tools.jar=$(build-classpath jre/jmx)
%if 0
jmx-remote.jar=${jmx.lib}/mx4j-remote.jar
%endif
junit.jar=$(build-classpath junit)
%if 0
rhino.jar=${rhino.home}/js.jar
%endif
struts.jar=$(build-classpath struts)
activation.jar=$(build-classpath jaf)
jcert.jar=$(build-classpath java/jcert)
jnet.jar=$(build-classpath java/jnet)
jsse.jar=$(build-classpath java/jsse)
jta.jar=$(build-classpath jta)
mail.jar=$(build-classpath javamail/mailapi)
puretls.jar=$(build-classpath puretls)

servlet-api.jar=$(build-classpath servlet-api)
# how the fck those bools work
# build.xml:103: servletapi/jsr154/src not found.
servletapi.build.notrequired=true

jsp-api.jar=$(build-classpath jsp-api)
jspapi.build.notrequired=true

log4j.jar=$(build-classpath logging-log4j)
#log4j.loc=%{_javadir}

# source is needed because source is copied modified and recompiled as tomcat jar
# see <target name="-build-tomcat-dbcp"> in build/build.xml
tomcat-dbcp.home=
commons-collections.home=%{_prefix}/src/jakarta-commons-collections-3.1
commons-pool.home=%{_prefix}/src/jakarta-commons-pool-1.3
commons-dbcp.home=%{_prefix}/src/jakarta-commons-dbcp-1.2.1
tomcat-dbcp.home=$TOPDIR/tomcat-deps
# err, it compiles three above and then appends to the jar, so the file should exist
tomcat-dbcp.jar=$TOPDIR/tomcat-deps/tomcat-dbcp.jar

%if 0
ant.jar=%{_javadir}/ant.jar
ant-launcher.jar=%{_javadir}/ant-launcher.jar
jtc.home=$TOPDIR/jakarta-tomcat-connectors/
jasper.home=$TOPDIR/jakarta-tomcat-jasper/jasper2
commons-dbcp.jar=$(build-classpath commons-dbcp)
commons-pool.jar=$(build-classpath commons-pool)
jmxri.jar=$(build-classpath jre/jmx)
regexp.jar=$(build-classpath regexp)
jsp-api.jar=$TOPDIR/jakarta-servletapi-5/jsr152/dist/lib/jsp-api.jar
servlet.doc=$TOPDIR/jakarta-servletapi-5/jsr154/dist/docs/api
struts.lib=%{_datadir}/struts
servletapi.build.notrequired=true
tyrex.jar=$(build-classpath tyrex)
jaas.jar=$(build-classpath jre/jaas)
jndi.jar=$(build-classpath jre/jndi)
jdbc20ext.jar=$(build-classpath jdbc-stdext)
jspapi.build.notrequired=true
taglibs-core.jar=$(build-classpath taglibs-core)
taglibs-standard.jar=$(build-classpath taglibs-standard)
%endif

EOF

%ant

exit 1

# build the connectors
cd connectors

%if 0

# this is just plain and simply evil but something changed in a major way between 5.0.16 and 5.0.18
oldclasspath=$CLASSPATH
export CLASSPATH=$TOPDIR/jakarta-servletapi-5/jsr154/dist/lib/servlet-api.jar:\
$TOPDIR/jakarta-tomcat-5/build/server/lib/catalina.jar
%endif

%if 0
cat > build.properties <<EOF

activation.jar=$(build-classpath jaf)
ant.jar=%{_javadir}/ant.jar
junit.jar=$(build-classpath junit)
commons-beanutils.jar=$(build-classpath commons-beanutils)
commons-collections.jar=$(build-classpath commons-collections)
commons-digester.jar=$(build-classpath commons-digester)
commons-fileupload.jar=$(build-classpath commons-fileupload)
commons-logging.jar=$(build-classpath commons-logging)
commons-logging-api.jar=$(build-classpath commons-logging-api)
commons-modeler.jar=$(build-classpath commons-modeler)
commons-pool.jar=$(build-classpath commons-pool)
regexp.jar=$(build-classpath regexp)
jmx.jar=$(build-classpath mx4j/mx4j)
puretls=$(build-classpath puretls)
activation.jar=$(build-classpath jaf)
mail.jar=$(build-classpath javamail/mailapi)
jta.jar=$(build-classpath jta)
tyrex.jar=$(build-classpath tyrex)
jaas.jar=$(build-classpath jaas)
jndi.jar=$(build-classpath jndi)
jdbc20ext.jar=$(build-classpath java/jdbc-stdext)
puretls.jar=$(build-classpath puretls)
jcert.jar=$(build-classpath jsse/jcert)
jnet.jar=$(build-classpath jsse/jnet)
jsse.jar=$(build-classpath jsse/jsse)

%endif

%if 0
commons-beanutils.jar=${commons-beanutils.lib}/commons-beanutils.jar
commons-collections.jar=${commons-collections.lib}/commons-collections.jar
commons-digester.jar=${commons-digester.lib}/commons-digester.jar
commons-fileupload.jar=${commons-fileupload.lib}/commons-fileupload-1.0-beta-1.jar
commons-logging-api.jar=${commons-logging.lib}/commons-logging-api.jar
commons-logging.jar=${commons-logging.lib}/commons-logging.jar
jndi.jar=${jndi.lib}/jndi.jar
ldap.jar=${jndi.lib}/ldap.jar
jaas.jar=${jndi.lib}/jaas.jar
regexp.jar=${regexp.lib}/jakarta-regexp-1.4.jar
servlet.jar=${servlet.lib}/servlet.jar
#xerces.jar=${xerces.lib}/xerces.jar
xercesImpl.jar=${xerces.lib}/xercesImpl.jar
xml-apis.jar=${xerces.lib}/xml-apis.jar
activation.jar=${activation.lib}/activation.jar
commons-daemon.jar=${commons-daemon.lib}/commons-daemon.jar
commons-dbcp.jar=${commons-dbcp.lib}/commons-dbcp.jar
commons-modeler.jar=${commons-modeler.lib}/commons-modeler.jar
commons-pool.jar=${commons-pool.lib}/commons-pool.jar
jdbc20ext.jar=${jdbc20ext.lib}/jdbc2_0-stdext.jar
jmx.jar=${jmx.lib}/mx4j-jmx.jar
jcert.jar=${jsse.lib}/jcert.jar
jnet.jar=${jsse.lib}/jnet.jar
jsse.jar=${jsse.lib}/jsse.jar
jta.jar=${jta.lib}/jta.jar
junit.jar=${junit.lib}/junit.jar
mail.jar=${mail.lib}/mail.jar
puretls.jar=${puretls.lib}/puretls.jar
struts.jar=${struts.lib}/struts.jar
tyrex.jar=${tyrex.lib}/tyrex-1.0.jar
tomcat5.jar=${tomcat5.home}/server/lib/catalina.jar
servlet-api.jar=${tomcat5.home}/common/lib/servlet-api.jar
tomcat41.jar=${tomcat41.home}/server/lib/catalina.jar
servlet-api.jar=${tomcat41.home}/common/lib/servlet.jar
tomcat33.jar=${tomcat33.home}/lib/common/tomcat_core.jar
%endif


%if 0
EOF
%ant build \
	-Dbuild.compiler=modern \
	-Djava.home=%{java_home}
%endif
%if 0
export CLASSPATH=$oldclasspath

# build the webapps and make the tree ready to install
cd ../jakarta-tomcat-5
%ant -Dbuild.compiler=modern -Djava.home=%{java_home} dist
%endif

%install
rm -rf $RPM_BUILD_ROOT

DEST=$RPM_BUILD_ROOT%{_tomcatdir}

install -d $DEST/bin \
	    $DEST/common/{lib,classes,endorsed} \
	    $DEST/server/{lib,classes} \
	    $DEST/webapps \
	    $RPM_BUILD_ROOT%{_sysconfdir}/tomcat \
	    $RPM_BUILD_ROOT%{_logdir}/tomcat \
	    $RPM_BUILD_ROOT%{_vardir}/work \
	    $RPM_BUILD_ROOT/etc/rc.d/init.d

install build/bin/*.sh			$DEST/bin
install build/bin/bootstrap*.jar	$DEST/bin
install build/bin/tomcat*.jar		$DEST/bin
install build/common/lib/naming-*.jar	$DEST/common/lib
install build/common/lib/jasper-*.jar	$DEST/common/lib
install build/conf/* 			$RPM_BUILD_ROOT%{_sysconfdir}/tomcat
install build/server/lib/catalina*.jar	$DEST/server/lib
install build/server/lib/servlets*.jar	$DEST/server/lib
install build/server/lib/tomcat*.jar	$DEST/server/lib
install build/server/lib/servlets-cgi.renametojar $DEST/server/lib/servlets-cgi.jar
install build/server/lib/servlets-ssi.renametojar $DEST/server/lib/servlets-ssi.jar
cp -rf  build/server/webapps	$DEST/server
cp -rf  build/webapps 		$DEST
cp -rf	build/shared		$DEST
cp -rf	build/temp		$DEST

ln -sf %{_logdir}/tomcat	$DEST/logs
ln -sf %{_vardir}/work		$DEST/work
ln -sf %{_sysconfdir}/tomcat	$DEST/conf

# symlinks instead of copies
ln -sf %{_javadir}/commons-daemon.jar	$DEST/bin

ln -sf %{_javadir}/activation.jar		$DEST/common/lib
ln -sf %{_javadir}/ant.jar			$DEST/common/lib
ln -sf %{_javadir}/commons-collections.jar	$DEST/common/lib
ln -sf %{_javadir}/commons-dbcp.jar		$DEST/common/lib
ln -sf %{_javadir}/commons-logging-api.jar	$DEST/common/lib
ln -sf %{_javadir}/commons-pool.jar		$DEST/common/lib
ln -sf %{_javadir}/servlet.jar		$DEST/common/lib
ln -sf %{_javadir}/servlet.jar		$DEST/common/lib/servletapi4.jar
ln -sf %{_javadir}/jdbc-stdext.jar		$DEST/common/lib/jdbc2_0-stdext.jar
ln -sf %{_javadir}/jdbc-stdext.jar		$DEST/common/lib/jdbc-stdext-2.0.jar
ln -sf %{_javadir}/jmxri.jar			$DEST/common/lib
ln -sf %{_javadir}/jndi.jar			$DEST/common/lib
ln -sf %{_javadir}/jta.jar			$DEST/common/lib
ln -sf %{_javadir}/mail.jar			$DEST/common/lib
ln -sf %{_javadir}/jsse.jar			$DEST/common/lib
ln -sf %{_javadir}/tyrex.jar			$DEST/common/lib
ln -sf %{_javadir}/junit.jar			$DEST/common/lib

ln -sf %{_javadir}/mailapi.jar		$DEST/common/lib
ln -sf %{_javadir}/pop3.jar			$DEST/common/lib
ln -sf %{_javadir}/pop3.jar			$DEST/common/lib/pop.jar
ln -sf %{_javadir}/smtp.jar			$DEST/common/lib
ln -sf %{_javadir}/imap.jar			$DEST/common/lib

ln -sf %{_javadir}/commons-beanutils.jar	$DEST/server/lib
ln -sf %{_javadir}/commons-digester.jar	$DEST/server/lib
ln -sf %{_javadir}/commons-fileupload.jar	$DEST/server/lib
ln -sf %{_javadir}/commons-logging.jar	$DEST/server/lib
ln -sf %{_javadir}/commons-modeler.jar	$DEST/server/lib
ln -sf %{_javadir}/jaas.jar			$DEST/server/lib/jaas.jar
ln -sf %{_javadir}/mx4j-jmx.jar		$DEST/server/lib
ln -sf %{_javadir}/regexp.jar		$DEST/server/lib
ln -sf %{_javadir}/regexp.jar		$DEST/server/lib/jakarta-regexp-1.2.jar
ln -sf %{_javadir}/regexp.jar		$DEST/server/lib/regexp-1.2.jar

ln -sf %{_javadir}/jaxp_parser_impl.jar	$DEST/common/endorsed
ln -sf %{_javadir}/xml-commons-apis.jar	$DEST/common/endorsed

ln -sf %{_javadir}/struts.jar $DEST/server/webapps/admin/WEB-INF/lib

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/tomcat

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
%doc *.txt LICENSE
%dir %{_tomcatdir}
%dir %{_tomcatdir}/bin
%attr(755,root,root) %{_tomcatdir}/bin/*.sh
%{_tomcatdir}/bin/*.jar
%dir %{_tomcatdir}/common
%dir %{_tomcatdir}/common/classes
%dir %{_tomcatdir}/common/endorsed
%{_tomcatdir}/common/endorsed/*.jar
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
# tomcat wants to regenerate tomcat-users.xml
%attr(775,root,http) %dir %{_sysconfdir}/tomcat
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/tomcat/*
%attr(754,root,root) /etc/rc.d/init.d/tomcat
%dir %{_vardir}
%attr(1730,root,http) %dir %{_vardir}/work
%attr(1730,root,http) %dir %{_logdir}/tomcat

%files doc
%defattr(644,root,root,755)
%doc catalina/docs/*
