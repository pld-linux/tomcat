# Conditional build:
%bcond_with	binary	# build from binary source
%bcond_without	javadoc	# skip building javadocs
#

Summary:	The Tomcat Servlet/JSP Container
Summary(pl):	Tomcat - Zasobnik servletów/JSP
Name:		jakarta-tomcat
Version:	5.0.30
Release:	0.1
License:	Apache
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/tomcat/tomcat-5/v5.0.30/src/%{name}-%{version}-src.tar.gz
# Source0-md5:	13fa1b56779c7b258c95266f69b22437
Source1:	%{name}.init
#Patch0:	%{name}-fixes.patch
#Patch1:	%{name}-JAVA_HOME.patch
#Patch2:	%{name}-fileupload.patch
URL:		http://jakarta.apache.org/tomcat/index.html
# required:
BuildRequires:	ant >= 1.5.3
BuildRequires:	jaas
BuildRequires:	jakarta-commons-beanutils
BuildRequires:	jakarta-commons-collections
BuildRequires:	jakarta-commons-digester
BuildRequires:	jakarta-commons-fileupload
BuildRequires:	jakarta-commons-logging
BuildRequires:	jakarta-regexp
BuildRequires:	jakarta-servletapi >= 4
BuildRequires:	jakarta-struts >= 1.0.2
BuildRequires:	jaxp_parser_impl
BuildRequires:	jdk >= 1.2
BuildRequires:	jpackage-utils
BuildRequires:	mx4j >= 1.1.1
BuildRequires:	puretls
BuildRequires:	rpmbuild(macros) >= 1.300
# optional:
BuildRequires:	jaf >= 1.0.1
BuildRequires:	jakarta-commons-daemon
BuildRequires:	jakarta-commons-dbcp
BuildRequires:	jakarta-commons-modeler
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
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_tomcatdir	%{_libdir}/tomcat
%define 	_logdir		%{_var}/log
%define		_vardir		%{_var}/lib/tomcat

%description
Tomcat 4.0, a server that implements the Servlet 2.3 and JSP 1.2
Specifications from Java Software.

%description -l pl
Tomcat 4.0 - serwer implementuj±cy specyfikacje Servlet 2.3 oraz JSP
1.2.

%package doc
Summary:	The Tomcat Servlet/JSP Container documentation
Summary(pl):	Dokumentacja do Tomcata
Group:		Development/Languages/Java

%description doc
The Tomcat Servlet/JSP Container documentation.

%description doc -l pl
Dokumentacja do Tomcata.

%prep
%setup -q -n %{name}-%{version}-src
#%patch0 -p1
#%patch1 -p1
#%patch2 -p1

rm -f lib/*.jar
rm -f %{name}-connectors-%{version}-src/lib/*.jar

cat >> build.properties <<EOBP
ant.jar=%{_javadir}/ant.jar
jtc.home=$RPM_BUILD_DIR/%{name}-%{version}-src/%{name}-connectors-%{version}-src/
jasper.home=./jasper
commons-beanutils.jar=%{_javadir}/commons-beanutils.jar
commons-fileupload.jar=%{_javadir}/commons-fileupload.jar
commons-collections.jar=%{_javadir}/commons-collections.jar
commons-daemon.jar=%{_javadir}/commons-daemon.jar
commons-dbcp.jar=%{_javadir}/commons-dbcp.jar
commons-digester.jar=%{_javadir}/commons-digester.jar
commons-logging.jar=%{_javadir}/commons-logging.jar
commons-logging-api.jar=%{_javadir}/commons-logging-api.jar
commons-modeler.jar=%{_javadir}/commons-modeler.jar
commons-pool.jar=%{_javadir}/commons-pool.jar
jcert.jar=%{_javadir}/jcert.jar
jnet.jar=%{_javadir}/jnet.jar
jsse.jar=%{_javadir}/jsse.jar
jmx.jar=%{_javadir}/mx4j-jmx.jar
jmxri.jar=%{_javadir}/mx4j-jmx.jar
junit.jar=%{_javadir}/junit.jar
regexp.jar=%{_javadir}/regexp.jar
servlet.jar=%{_javadir}/servlet.jar
#servlet.doc=%{javadocdir}/servletapi4
xercesImpl.jar=%{_javadir}/jaxp_parser_impl.jar
xmlParserAPIs.jar=%{_javadir}/xml-commons-apis.jar
puretls.jar=%{_javadir}/puretls.jar
jmx.jar=%{_javadir}/mx4j-jmx.jar
struts.jar=%{_javadir}/struts.jar
struts.lib=%{_datadir}/jakarta-struts
jdbc20ext.jar=%{_javadir}/jdbc-stdext.jar
activation.jar=%{_javadir}/activation.jar
mail.jar=%{_javadir}/mailapi.jar
jndi.jar=%{_javadir}/jndi.jar
jta.jar=%{_javadir}/jta.jar
jaas.jar=%{_javadir}/jaas.jar
tyrex.jar=%{_javadir}/tyrex.jar
EOBP

%build
export CLASSPATH=%(build-classpath xml-commons-apis xalan)
%ant

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
