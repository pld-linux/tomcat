Summary:	The Tomcat Servlet/JSP Container
Summary(pl):	Tomcat - Zasobnik servletów/JSP
Name:		jakarta-tomcat
Version:	4.1.24
%define		base_version 4.0
Release:	3
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
BuildRequires:	jdk >= 1.2
BuildRequires:	jakarta-ant >= 1.5.3
BuildRequires:	jaxp >= 1.1
BuildRequires:	xerces-j >= 1
BuildRequires:	jakarta-servletapi >= 4
BuildRequires:	jakarta-commons-collections
BuildRequires:	jakarta-commons-beanutils
BuildRequires:	jakarta-commons-digester
BuildRequires:	jakarta-commons-logging
BuildRequires:	jakarta-commons-fileupload
BuildRequires:	jakarta-regexp
# optional:
BuildRequires:	jakarta-commons-daemon
BuildRequires:	jakarta-commons-dbcp
BuildRequires:	jakarta-commons-modeler
BuildRequires:	jakarta-commons-pool
BuildRequires:	jdbc-stdext >= 2.0
BuildRequires:	jmx >= 1.0
BuildRequires:	jndi >= 1.2.1
BuildRequires:	jndi-provider-ldap
BuildRequires:	jaf >= 1.0.1
BuildRequires:	javamail >= 1.2
BuildRequires:	jsse >= 1.0.2
BuildRequires:	jta >= 1.0.1
BuildRequires:	tyrex >= 1.0
BuildRequires:	junit >= 3.7
Requires:	jre >= 1.2
Requires:	jaxp >= 1.1
Requires:	xerces-j >= 1
Requires:	jakarta-servletapi >= 4
Requires:	jakarta-commons-collections
Requires:	jakarta-commons-beanutils
Requires:	jakarta-commons-digester
Requires:	jakarta-commons-logging
Requires:	jakarta-commons-fileupload
Requires:	jakarta-regexp
Requires:	jdbc-stdext >= 2.0
Requires:	jmx >= 1.0
Requires:	jndi >= 1.2.1
Requires:	jndi-provider-ldap
Requires:	jaf >= 1.0.1
Requires:	javamail >= 1.2
Requires:	jsse >= 1.0.2
Requires:	jta >= 1.0.1
Requires:	tyrex >= 1.0
Requires(pre): /usr/bin/getgid
Requires(pre): /bin/id
Requires(pre): /usr/sbin/groupadd
Requires(pre): /usr/sbin/useradd
Requires(postun):      /usr/sbin/userdel
Requires(postun):      /usr/sbin/groupdel
Requires(post,preun):	/sbin/chkconfig
Requires(post,postun):	/sbin/ldconfig
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java
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
if [ -z "$JAVA_HOME" ]; then
	JAVA_HOME=%{_libdir}/java
fi
ANT_HOME=%{_javalibdir}
export JAVA_HOME ANT_HOME

cat > build.properties << EOF
# ----- Compile Control Flags -----
compile.debug=on
compile.deprecation=off
compile.optimize=on

# ----- Default Base Path for Dependent Packages -----
base.path=%{_prefix}

# ----- Jakarta Regular Expressions Library, version 1.2 -----
regexp.home=%{_javalibdir}
regexp.lib=\${regexp.home}
regexp.jar=\${regexp.home}/regexp.jar

# ----- Jakarta Servlet API Classes (Servlet 2.3 / JSP 1.2) -----
servlet.home=$RPM_BUILD_DIR/%{name}-%{version}-src/doc
servlet.lib=%{_javalibdir}
servlet.jar=\${servlet.lib}/servlet.jar

# ----- Java Activation Framework (JAF), version 1.0.1 or later -----
activation.home=%{_javalibdir}
activation.lib=\${activation.home}
activation.jar=\${activation.lib}/activation.jar

# ----- Java API for XML Processing (JAXP), version 1.1 or later -----
jaxp.home=%{_javalibdir}
jaxp.lib=\${jaxp.home}
crimson.jar=\${jaxp.lib}/crimson.jar
jaxp.jar=\${jaxp.lib}/jaxp.jar
xalan.jar=\${jaxp.lib}/xalan.jar

# ----- Java Database Connectivity (JDBC) Optional Package, version 2.0 -----
jdbc20ext.home=%{_javalibdir}
jdbc20ext.lib=\${jdbc20ext.home}
jdbc20ext.jar=\${jdbc20ext.lib}/jdbc2_0-stdext.jar

# ----- Java Mail, version 1.2 or later -----
mail.home=%{_javalibdir}
mail.lib=\${mail.home}
mail.jar=\${mail.lib}/mail.jar

# ----- Java Management Extensions (JMX) RI, version 1.0.1 or later -----
jmx.home=%{_javalibdir}
jmx.lib=\${jmx.home}
jmxri.jar=\${jmx.lib}/jmxri.jar

# ----- Java Naming and Directory Interface (JNDI), version 1.2 or later -----
jndi.home=%{_javalibdir}
jndi.lib=\${jndi.home}
jndi.jar=\${jndi.lib}/jndi.jar
ldap.jar=\${jndi.lib}/ldap.jar

# ----- Java Secure Sockets Extension (JSSE), version 1.0.2 or later -----
jsse.home=%{_javalibdir}
jsse.lib=\${jsse.home}
jcert.jar=\${jsse.lib}/jcert.jar
jnet.jar=\${jsse.lib}/jnet.jar
jsse.jar=\${jsse.lib}/jsse.jar

# ----- Java Transaction API (JTA), version 1.0.1 or later -----
jta.home=%{_javalibdir}
jta.lib=\${jta.home}
jta.jar=\${jta.lib}/jta.jar

# ----- JUnit Unit Test Suite, version 3.7 or later -----
junit.home=%{_javalibdir}
junit.lib=\${junit.home}
junit.jar=\${junit.lib}/junit.jar

# ----- Tyrex Data Source, version 0.9.7 -----
tyrex.home=%{_javalibdir}
tyrex.lib=\${tyrex.home}
tyrex.jar=\${tyrex.lib}/tyrex.jar

# ----- Xerces XML Parser, version 1.4.3 or later -----
xerces.home=%{_javalibdir}
xerces.lib=\${xerces.home}
xerces.jar=\${xerces.lib}/xerces.jar

# ----- Commons Collections, version 1.0 or later -----
commons-collections.home=%{_javalibdir}
commons-collections.lib=\${commons-collections.home}
commons-collections.jar=\${commons-collections.lib}/commons-collections.jar

# ----- Commons Beanutils, version 1.1 or later -----
commons-beanutils.home=%{_javalibdir}
commons-beanutils.lib=\${commons-beanutils.home}
commons-beanutils.jar=\${commons-beanutils.lib}/commons-beanutils.jar

# ----- Commons Digester, version 1.1.1 or later -----
commons-digester.home=%{_javalibdir}
commons-digester.lib=\${commons-digester.home}
commons-digester.jar=\${commons-digester.lib}/commons-digester.jar

# ----- Commons Logging, version 1.0.1 or later -----
commons-logging.home=%{_javalibdir}
commons-logging.lib=\${commons-logging.home}
commons-logging-api.jar=\${commons-logging.lib}/commons-logging-api.jar
commons-logging.jar=\${commons-logging.lib}/commons-logging.jar

# ----- Commons Daemon, version 20020219 or later -----
commons-daemon.home=%{_javalibdir}
commons-daemon.lib=\${commons-daemon.home}
commons-daemon.jar=\${commons-daemon.lib}/commons-daemon.jar

# ----- Commons DBCP, version 1.0 or later -----
commons-dbcp.home=%{_javalibdir}
commons-dbcp.lib=\${commons-dbcp.home}
commons-dbcp.jar=\${commons-dbcp.lib}/commons-dbcp.jar

# ----- Commons FileUpload, nightly build -----
commons-fileupload.home=%{_javalibdir}
commons-fileupload.lib=\${commons-fileupload.home}
commons-fileupload.jar=\${commons-fileupload.lib}/commons-fileupload.jar

# ----- Commons Modeler, version 1.0 or later -----
commons-modeler.home=%{_javalibdir}
commons-modeler.lib=\${commons-modeler.home}
commons-modeler.jar=\${commons-modeler.lib}/commons-modeler.jar

# ----- Commons Pool, version 1.0 or later -----
commons-pool.home=%{_javalibdir}
commons-pool.lib=\${commons-pool.home}
commons-pool.jar=\${commons-pool.lib}/commons-pool.jar


jasper.home=jasper
jtc.home=../jakarta-tomcat-connectors-%{version}-src
EOF

install -d doc/docs/api

ln -s ../jakarta-tomcat-connectors-%{version}-src  webapps/jakarta-tomcat-connectors-%{version}-src
cd jakarta-tomcat-connectors-%{version}-src
ln -s . jakarta-tomcat-connectors-%{version}-src
ant
cd ..

ant dist

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_tomcatdir}/bin \
	    $RPM_BUILD_ROOT%{_tomcatdir}/common/{lib,classes,endorsed} \
	    $RPM_BUILD_ROOT%{_tomcatdir}/server/{lib,classes} \
	    $RPM_BUILD_ROOT%{_tomcatdir}/webapps \
	    $RPM_BUILD_ROOT%{_sysconfdir}/tomcat \
	    $RPM_BUILD_ROOT%{_logdir}/tomcat \
	    $RPM_BUILD_ROOT%{_vardir}/work \
	    $RPM_BUILD_ROOT/etc/rc.d/init.d

install build/bin/*.sh $RPM_BUILD_ROOT%{_tomcatdir}/bin
install build/bin/bootstrap*.jar $RPM_BUILD_ROOT%{_tomcatdir}/bin
install build/bin/tomcat*.jar $RPM_BUILD_ROOT%{_tomcatdir}/bin
install build/common/lib/naming-*.jar $RPM_BUILD_ROOT%{_tomcatdir}/common/lib
install build/common/lib/jasper-*.jar $RPM_BUILD_ROOT%{_tomcatdir}/common/lib
install build/conf/* $RPM_BUILD_ROOT%{_sysconfdir}/tomcat
install build/server/lib/catalina*.jar $RPM_BUILD_ROOT%{_tomcatdir}/server/lib
install build/server/lib/servlets*.jar $RPM_BUILD_ROOT%{_tomcatdir}/server/lib
install build/server/lib/servlets-cgi.renametojar $RPM_BUILD_ROOT%{_tomcatdir}/server/lib/servlets-cgi.jar
install build/server/lib/servlets-ssi.renametojar $RPM_BUILD_ROOT%{_tomcatdir}/server/lib/servlets-ssi.jar
install build/server/lib/tomcat*.jar $RPM_BUILD_ROOT%{_tomcatdir}/server/lib
cp -rf  build/server/webapps $RPM_BUILD_ROOT%{_tomcatdir}/server
cp -rf  build/webapps $RPM_BUILD_ROOT%{_tomcatdir}
cp -rf	build/shared $RPM_BUILD_ROOT%{_tomcatdir}
cp -rf	build/temp $RPM_BUILD_ROOT%{_tomcatdir}

ln -sf %{_logdir}/tomcat $RPM_BUILD_ROOT%{_tomcatdir}/logs
ln -sf %{_vardir}/work $RPM_BUILD_ROOT%{_tomcatdir}/work
ln -sf %{_sysconfdir}/tomcat $RPM_BUILD_ROOT%{_tomcatdir}/conf

# symlinks instead of copies
ln -sf %{_javalibdir}/ant.jar $RPM_BUILD_ROOT%{_tomcatdir}/common/lib/ant.jar
ln -sf %{_javalibdir}/jaxp.jar $RPM_BUILD_ROOT%{_tomcatdir}/common/lib/jaxp.jar
ln -sf %{_javalibdir}/xerces.jar $RPM_BUILD_ROOT%{_tomcatdir}/common/lib/xerces.jar
ln -sf %{_javalibdir}/servlet.jar $RPM_BUILD_ROOT%{_tomcatdir}/common/lib/servlet.jar
ln -sf %{_javalibdir}/jdbc2_0-stdext.jar $RPM_BUILD_ROOT%{_tomcatdir}/common/lib/jdbc2_0.jar
ln -sf %{_javalibdir}/jmxri.jar $RPM_BUILD_ROOT%{_tomcatdir}/common/lib/jmxri.jar
ln -sf %{_javalibdir}/jndi.jar $RPM_BUILD_ROOT%{_tomcatdir}/common/lib/jndi.jar
ln -sf %{_javalibdir}/ldap.jar $RPM_BUILD_ROOT%{_tomcatdir}/common/lib/ldap.jar
ln -sf %{_javalibdir}/activation.jar $RPM_BUILD_ROOT%{_tomcatdir}/common/lib/activation.jar
ln -sf %{_javalibdir}/jta.jar $RPM_BUILD_ROOT%{_tomcatdir}/common/lib/jta.jar
ln -sf %{_javalibdir}/mail.jar $RPM_BUILD_ROOT%{_tomcatdir}/common/lib/mail.jar
ln -sf %{_javalibdir}/jsse.jar $RPM_BUILD_ROOT%{_tomcatdir}/common/lib/jsse.jar

ln -sf %{_javalibdir}/tyrex.jar $RPM_BUILD_ROOT%{_tomcatdir}/common/lib/tyrex.jar
ln -sf %{_javalibdir}/junit.jar $RPM_BUILD_ROOT%{_tomcatdir}/common/lib/junit.jar

ln -sf %{_javalibdir}/commons-collections.jar $RPM_BUILD_ROOT%{_tomcatdir}/common/lib/commons-collections.jar
ln -sf %{_javalibdir}/commons-dbcp.jar $RPM_BUILD_ROOT%{_tomcatdir}/common/lib/commons-dbcp.jar
ln -sf %{_javalibdir}/commons-logging-api.jar $RPM_BUILD_ROOT%{_tomcatdir}/common/lib/commons-logging-api.jar
ln -sf %{_javalibdir}/commons-pool.jar $RPM_BUILD_ROOT%{_tomcatdir}/common/lib/commons-pool.jar

ln -sf %{_javalibdir}/regexp.jar $RPM_BUILD_ROOT%{_tomcatdir}/server/lib/regexp.jar
ln -sf %{_javalibdir}/commons-beanutils.jar $RPM_BUILD_ROOT%{_tomcatdir}/server/lib/commons-beanutils.jar
ln -sf %{_javalibdir}/commons-digester.jar $RPM_BUILD_ROOT%{_tomcatdir}/server/lib/commons-digester.jar
ln -sf %{_javalibdir}/commons-logging.jar $RPM_BUILD_ROOT%{_tomcatdir}/server/lib/commons-logging.jar
ln -sf %{_javalibdir}/commons-modeler.jar $RPM_BUILD_ROOT%{_tomcatdir}/server/lib/commons-modeler.jar
ln -sf %{_javalibdir}/commons-fileupload.jar $RPM_BUILD_ROOT%{_tomcatdir}/server/lib/commons-fileupload.jar

ln -sf %{_javalibdir}/commons-daemon.jar $RPM_BUILD_ROOT%{_tomcatdir}/bin/commons-daemon.jar

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
       /usr/sbin/userdel http
       /usr/sbin/groupdel http
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
