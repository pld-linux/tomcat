Summary:	The Tomcat Servlet/JSP Container
Summary(pl):	Tomcat - Zasobnik servletów/JSP
Name:		jakarta-tomcat
Version:	4.1.24
%define		base_version 4.0
Release:	4
License:	Apache
Group:		Development/Languages/Java
Source0:	http://jakarta.apache.org/builds/%{name}-%{base_version}/release/v%{version}/src/%{name}-%{version}-src.tar.gz
# Source0-md5:	bdcdf1091ff942f378b1e6f402e44a67
Source1:	http://jakarta.apache.org/builds/%{name}-%{base_version}/release/v%{version}/src/%{name}-connectors-%{version}-src.tar.gz
# Source1-md5:	0daa701e51d04570006abce1ac580aed
Source2:	%{name}.init
Patch0:		%{name}-fixes.patch
Patch1:		%{name}-JAVA_HOME.patch
Patch2:		%{name}-fileupload.patch
URL:		http://jakarta.apache.org/tomcat/index.html
# required:
BuildRequires:	jaas
BuildRequires:	jakarta-ant >= 1.5.3
BuildRequires:	jakarta-servletapi >= 4
BuildRequires:	jakarta-commons-collections
BuildRequires:	jakarta-commons-beanutils
BuildRequires:	jakarta-commons-digester
BuildRequires:	jakarta-commons-logging
BuildRequires:	jakarta-commons-fileupload
BuildRequires:	jakarta-regexp
BuildRequires:	jakarta-struts >= 1.0.2
BuildRequires:	jaxp_parser_impl
BuildRequires:	jdk >= 1.2
BuildRequires:	mx4j >= 1.1.1
BuildRequires:	puretls
BuildRequires:	rpmbuild(macros) >= 1.159
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
BuildRequires:	tyrex >= 1.0
BuildRequires:	xml-commons
Requires:	jre >= 1.2
Requires:	jakarta-servletapi >= 4
Requires:	jakarta-commons-collections
Requires:	jakarta-commons-beanutils
Requires:	jakarta-commons-digester
Requires:	jakarta-commons-logging
Requires:	jakarta-commons-fileupload
Requires:	jakarta-regexp
Requires:	jdbc-stdext >= 2.0
Requires:	jndi >= 1.2.1
Requires:	jaf >= 1.0.1
Requires:	javamail >= 1.2
Requires:	jsse >= 1.0.2
Requires:	jta >= 1.0.1
Requires:	tyrex >= 1.0
Requires:	jaxp_parser_impl
Requires:	xml-commons
Requires:	jaas
Requires:	mx4j >= 1.1.1
Requires(pre):	/usr/bin/getgid
Requires(pre):	/bin/id
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(post,preun):	/sbin/chkconfig
Requires(post,postun):	/sbin/ldconfig
Provides:	group(http)
Provides:	user(http)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	%{_datadir}/java
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
%setup -q -n %{name}-%{version}-src -a1
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
CLASSPATH=%{_javalibdir}/xml-commons-apis.jar
CLASSPATH=$CLASSPAHT:%{_javalibdir}/xalan.jar
CLASSPATH=%{_javalibdir}/servlet.jar
export CLASSPATH

rm -f lib/*.jar
rm -f %{name}-connectors-%{version}-src/lib/*.jar

cat >> build.properties <<EOBP
ant.jar=%{_javalibdir}/ant.jar
jtc.home=$RPM_BUILD_DIR/%{name}-%{version}-src/%{name}-connectors-%{version}-src/
jasper.home=./jasper
commons-beanutils.jar=%{_javalibdir}/commons-beanutils.jar
commons-fileupload.jar=%{_javalibdir}/commons-fileupload.jar
commons-collections.jar=%{_javalibdir}/commons-collections.jar
commons-daemon.jar=%{_javalibdir}/commons-daemon.jar
commons-dbcp.jar=%{_javalibdir}/commons-dbcp.jar
commons-digester.jar=%{_javalibdir}/commons-digester.jar
commons-logging.jar=%{_javalibdir}/commons-logging.jar
commons-logging-api.jar=%{_javalibdir}/commons-logging-api.jar
commons-modeler.jar=%{_javalibdir}/commons-modeler.jar
commons-pool.jar=%{_javalibdir}/commons-pool.jar
jcert.jar=%{_javalibdir}/jcert.jar
jnet.jar=%{_javalibdir}/jnet.jar
jsse.jar=%{_javalibdir}/jsse.jar
jmx.jar=%{_javalibdir}/mx4j-jmx.jar
jmxri.jar=%{_javalibdir}/mx4j-jmx.jar
junit.jar=%{_javalibdir}/junit.jar
regexp.jar=%{_javalibdir}/regexp.jar
servlet.jar=%{_javalibdir}/servlet.jar
#servlet.doc=%{javadocdir}/servletapi4
xercesImpl.jar=%{_javalibdir}/jaxp_parser_impl.jar
xmlParserAPIs.jar=%{_javalibdir}/xml-commons-apis.jar
puretls.jar=%{_javalibdir}/puretls.jar
jmx.jar=%{_javalibdir}/mx4j-jmx.jar
struts.jar=%{_javalibdir}/struts.jar
struts.lib=%{_datadir}/jakarta-struts
jdbc20ext.jar=%{_javalibdir}/jdbc-stdext.jar
activation.jar=%{_javalibdir}/activation.jar
mail.jar=%{_javalibdir}/mailapi.jar
jndi.jar=%{_javalibdir}/jndi.jar
jta.jar=%{_javalibdir}/jta.jar
jaas.jar=%{_javalibdir}/jaas.jar
tyrex.jar=%{_javalibdir}/tyrex.jar
EOBP

JAVA_HOME=%{_libdir}/java
ant -Djava.home=$JAVA_HOME

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
ln -sf %{_javalibdir}/commons-daemon.jar	$DEST/bin

ln -sf %{_javalibdir}/activation.jar		$DEST/common/lib
ln -sf %{_javalibdir}/ant.jar			$DEST/common/lib
ln -sf %{_javalibdir}/commons-collections.jar	$DEST/common/lib
ln -sf %{_javalibdir}/commons-dbcp.jar		$DEST/common/lib
ln -sf %{_javalibdir}/commons-logging-api.jar	$DEST/common/lib
ln -sf %{_javalibdir}/commons-pool.jar		$DEST/common/lib
ln -sf %{_javalibdir}/servlet.jar		$DEST/common/lib
ln -sf %{_javalibdir}/servlet.jar		$DEST/common/lib/servletapi4.jar
ln -sf %{_javalibdir}/jdbc-stdext.jar		$DEST/common/lib/jdbc2_0-stdext.jar
ln -sf %{_javalibdir}/jdbc-stdext.jar		$DEST/common/lib/jdbc-stdext-2.0.jar
ln -sf %{_javalibdir}/jmxri.jar			$DEST/common/lib
ln -sf %{_javalibdir}/jndi.jar			$DEST/common/lib
ln -sf %{_javalibdir}/jta.jar			$DEST/common/lib
ln -sf %{_javalibdir}/mail.jar			$DEST/common/lib
ln -sf %{_javalibdir}/jsse.jar			$DEST/common/lib
ln -sf %{_javalibdir}/tyrex.jar			$DEST/common/lib
ln -sf %{_javalibdir}/junit.jar			$DEST/common/lib

ln -sf %{_javalibdir}/mailapi.jar		$DEST/common/lib
ln -sf %{_javalibdir}/pop3.jar			$DEST/common/lib
ln -sf %{_javalibdir}/pop3.jar			$DEST/common/lib/pop.jar
ln -sf %{_javalibdir}/smtp.jar			$DEST/common/lib
ln -sf %{_javalibdir}/imap.jar			$DEST/common/lib

ln -sf %{_javalibdir}/commons-beanutils.jar	$DEST/server/lib
ln -sf %{_javalibdir}/commons-digester.jar	$DEST/server/lib
ln -sf %{_javalibdir}/commons-fileupload.jar	$DEST/server/lib
ln -sf %{_javalibdir}/commons-logging.jar	$DEST/server/lib
ln -sf %{_javalibdir}/commons-modeler.jar	$DEST/server/lib
ln -sf %{_javalibdir}/jaas.jar			$DEST/server/lib/jaas.jar
ln -sf %{_javalibdir}/mx4j-jmx.jar		$DEST/server/lib
ln -sf %{_javalibdir}/regexp.jar		$DEST/server/lib
ln -sf %{_javalibdir}/regexp.jar		$DEST/server/lib/jakarta-regexp-1.2.jar
ln -sf %{_javalibdir}/regexp.jar		$DEST/server/lib/regexp-1.2.jar

ln -sf %{_javalibdir}/jaxp_parser_impl.jar	$DEST/common/endorsed
ln -sf %{_javalibdir}/xml-commons-apis.jar	$DEST/common/endorsed

ln -sf %{_javalibdir}/struts.jar $DEST/server/webapps/admin/WEB-INF/lib

install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/tomcat

%clean
rm -rf $RPM_BUILD_ROOT

%pre
if [ -n "`getgid http`" ]; then
	if [ "`getgid http`" != "51" ]; then
		echo "Error: group http doesn't have gid=51. Correct this before installing tomcat." 1>&2
		exit 1
	fi
else
	/usr/sbin/groupadd -g 51 -r -f http
fi
if [ -n "`id -u http 2>/dev/null`" ]; then
	if [ "`id -u http`" != "51" ]; then
		echo "Error: user http doesn't have uid=51. Correct this before installing tomcat." 1>&2
		exit 1
	fi
else
	/usr/sbin/useradd -u 51 -r -d /home/services/httpd -s /bin/false -c "HTTP User" -g http http 1>&2
fi

%post
/sbin/chkconfig --add tomcat
if [ -f /var/lock/subsys/tomcat ]; then
	/etc/rc.d/init.d/tomcat restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/tomcat start\" to start tomcat daemon."
fi

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/tomcat ]; then
		/etc/rc.d/init.d/tomcat stop 1>&2
	fi
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
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/tomcat/*
%attr(754,root,root) /etc/rc.d/init.d/tomcat
%dir %{_vardir}
%attr(1730,root,http) %dir %{_vardir}/work
%attr(1730,root,http) %dir %{_logdir}/tomcat

%files doc
%defattr(644,root,root,755)
%doc catalina/docs/*
