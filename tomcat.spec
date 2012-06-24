Summary:	The Tomcat Servlet/JSP Container
Summary(pl):	Tomcat - Zasobnik servlet�w/JSP
Name:		jakarta-tomcat
Version:	4.0.1
%define		base_version 4.0
Release:	2
License:	Apache Software License
Group:		Development/Languages/Java
Source0:	http://jakarta.apache.org/builds/%{name}-%{base_version}/release/v%{version}/src/%{name}-%{version}-src.tar.gz
URL:		http://jakarta.apache.org/tomcat/index.html
Requires:	jre
Requires:	jaxp
Requires:	xerces-j
Requires:	jakarta-servletapi
Requires:	jdbc-stdext
Requires:	jmx
Requires:	jndi
Requires:	jaf
Requires:	javamail
Requires:	jta
Requires:	jsse
Requires:	tyrex
Requires:	jakarta-regexp
Requires:	junit
Requires:	ldap
BuildRequires:	jdk
BuildRequires:	jakarta-ant
BuildRequires:	jaxp
BuildRequires:	xerces-j
BuildRequires:	jakarta-servletapi
BuildRequires:	jdbc-stdext
BuildRequires:	jmx
BuildRequires:	jndi
BuildRequires:	jaf
BuildRequires:	javamail
BuildRequires:	jta
BuildRequires:	jsse
BuildRequires:	tyrex
BuildRequires:	jakarta-regexp
BuildRequires:	junit
BuildRequires:	ldap
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java
%define		_tomcatdir	%{_libdir}/tomcat
%define 	_logdir		%{_var}/log

%description
Tomcat 4.0, a server that implements the Servlet 2.3 and JSP 1.2
Specifications from Java Software.

%description -l pl
Tomcat 4.0 - serwer implementuj�cy specyfikacje Servlet 2.3 oraz JSP
1.2.

%package doc
Summary:	The Tomcat Servlet/JSP Container documentation
Summary(pl):	Dokumentacja do Tomcata.
Group:		Development/Languages/Java

%description doc
The Tomcat Servlet/JSP Container documentation.

%description doc -l pl
Dokumentacja do Tomcata.

%prep
%setup -q -n %{name}-%{version}-src

%build
if [ ! `echo $JAVA_HOME` ]; then
	echo "You haven't JAVA_HOME variable set. Can't continue."
	exit 1
fi
		
ANT_HOME=%{_javalibdir}
export ANT_HOME

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
xerces.home=%{_javalibdir}/classes
xerces.lib=\${xerces.home}
xerces.jar=\${xerces.lib}/xerces.jar
EOF

install -d doc/docs/api

ant dist

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_tomcatdir}/bin \
	    $RPM_BUILD_ROOT%{_tomcatdir}/classes \
	    $RPM_BUILD_ROOT%{_tomcatdir}/common/{lib,classes} \
	    $RPM_BUILD_ROOT%{_tomcatdir}/lib \
	    $RPM_BUILD_ROOT%{_tomcatdir}/server/{lib,classes} \
	    $RPM_BUILD_ROOT%{_tomcatdir}/webapps \
	    $RPM_BUILD_ROOT%{_tomcatdir}/work \
	    $RPM_BUILD_ROOT%{_sysconfdir}/tomcat \
	    $RPM_BUILD_ROOT%{_logdir}/tomcat

install build/bin/*.sh $RPM_BUILD_ROOT%{_tomcatdir}/bin
install build/bin/*.jar $RPM_BUILD_ROOT%{_tomcatdir}/bin
install build/common/lib/naming-*.jar $RPM_BUILD_ROOT%{_tomcatdir}/common/lib
install build/conf/* $RPM_BUILD_ROOT%{_sysconfdir}/tomcat
install build/server/lib/[!r]*.jar $RPM_BUILD_ROOT%{_tomcatdir}/server/lib
install build/lib/*.jar $RPM_BUILD_ROOT%{_tomcatdir}/lib
cp -rf  build/webapps $RPM_BUILD_ROOT%{_tomcatdir}

ln -sf %{_logdir}/tomcat $RPM_BUILD_ROOT%{_tomcatdir}/logs
ln -sf %{_sysconfdir}/tomcat $RPM_BUILD_ROOT%{_tomcatdir}/conf


ln -sf %{_javalibdir}/jaxp.jar $RPM_BUILD_ROOT%{_tomcatdir}/common/lib/jaxp.jar
ln -sf %{_javalibdir}/classes/xerces.jar $RPM_BUILD_ROOT%{_tomcatdir}/common/lib/xerces.jar
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
ln -sf %{_javalibdir}/regexp.jar $RPM_BUILD_ROOT%{_tomcatdir}/common/lib/regexp.jar

gzip -9nf *.txt LICENSE

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_tomcatdir}/bin/*.sh
%dir %{_tomcatdir}/common/classes
%dir %{_tomcatdir}/classes
%dir %{_tomcatdir}/server
%dir %{_tomcatdir}/server/classes
%dir %{_tomcatdir}/webapps
%dir %{_tomcatdir}/work
%dir %{_sysconfdir}/tomcat
%dir %{_logdir}/tomcat
%{_tomcatdir}/bin/*.jar
%{_tomcatdir}/common/lib
%{_tomcatdir}/conf
%{_tomcatdir}/lib
%{_tomcatdir}/logs
%{_tomcatdir}/server/lib
%{_tomcatdir}/webapps/*
%{_sysconfdir}/tomcat/*

%files doc
%defattr(644,root,root,755)
%doc catalina/docs/*
