Summary: 	The Tomcat Servlet/JSP Container
Summary(pl):	The Tomcat Servlet/JSP Container
Name:		jakarta-tomcat
Version:	4.0
Release:	1
License:	Apache Software License
Group:		Development/Languages/Java
Group(de):	Entwicklung/Sprachen/Java
Group(pl):	Programowanie/Jêzyki/Java
Source0:	http://jakarta.apache.org/dist/jakarta/%{name}-%{version}/release/v%{version}/src/%{name}-%{version}-src.tar.gz
URL:		http://jakarta.apache.org/tomcat/index.html
Requires:	ibm-java-sdk
Requires:	crimson
Requires:	xalan-j
Requires:	jaxp
Requires:	jakarta-regexp
Requires:	jakarta-servletapi
Requires:	jdbc-stdext
Requires:	javamail
Requires:	jaf
Requires:	jmx
Requires:	jsse
Requires:	junit
Requires:	jta
Requires:	tyrex
Requires:	ldap
Requires:	jndi
Requires:	jdbc-stdext
BuildRequires:	jakarta-ant
BuildRequires:	ibm-java-sdk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java
%define		_tomcatdir	%{_libdir}/tomcat
%define 	_logdir		%{_var}/log

%description
Tomcat 4.0, a server that implements the Servlet 2.3 
and JSP 1.2 Specifications from Java Software. 


%package doc
Group:		Development/Languages/Java
Group(de):	Entwicklung/Sprachen/Java
Group(pl):	Programowanie/Jêzyki/Java
Summary: 	The Tomcat Servlet/JSP Container documentation

%description doc
The Tomcat Servlet/JSP Container documentation

%prep
%setup -q -n %{name}-%{version}-src

%build
export JAVA_HOME="/usr/lib/IBMJava2-13"
export ANT_HOME=%{_javalibdir}

cat > $RPM_BUILD_DIR/%{name}-%{version}-src/build.properties << EOF
# ----- Compile Control Flags -----
compile.debug=on
compile.deprecation=off
compile.optimize=on

# ----- Default Base Path for Dependent Packages -----
base.path=/usr

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
EOF

install -d $RPM_BUILD_DIR/%{name}-%{version}-src/doc/docs/api

ant dist

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_bindir}
install -d $RPM_BUILD_ROOT/%{_javalibdir}
install -d $RPM_BUILD_ROOT/%{_tomcatdir}/classes
install -d $RPM_BUILD_ROOT/%{_tomcatdir}/common/classes
install -d $RPM_BUILD_ROOT/%{_sysconfdir}/tomcat
install -d $RPM_BUILD_ROOT/%{_logdir}/tomcat
install -d $RPM_BUILD_ROOT/%{_tomcatdir}/server/classes
install -d $RPM_BUILD_ROOT/%{_tomcatdir}/webapps
install -d $RPM_BUILD_ROOT/%{_tomcatdir}/work

cp dist/bin/*.sh $RPM_BUILD_ROOT/%{_bindir}
cp dist/bin/*.jar $RPM_BUILD_ROOT/%{_bindir}
cp dist/common/lib/naming-*.jar $RPM_BUILD_ROOT/%{_javalibdir}
cp dist/conf/* $RPM_BUILD_ROOT/%{_sysconfdir}/tomcat
cp dist/jasper/jasper-*.jar $RPM_BUILD_ROOT/%{_javalibdir}
cp dist/server/lib/[!r]*.jar $RPM_BUILD_ROOT/%{_javalibdir}
cp dist/lib/*.jar $RPM_BUILD_ROOT/%{_javalibdir}
cp -r dist/webapps $RPM_BUILD_ROOT/%{_tomcatdir}

ln -sf %{_bindir} $RPM_BUILD_ROOT/%{_tomcatdir}/bin
ln -sf %{_javalibdir} $RPM_BUILD_ROOT/%{_tomcatdir}/common/lib
ln -sf %{_javalibdir} $RPM_BUILD_ROOT/%{_tomcatdir}/jasper
ln -sf %{_javalibdir} $RPM_BUILD_ROOT/%{_tomcatdir}/lib
ln -sf %{_javalibdir} $RPM_BUILD_ROOT/%{_tomcatdir}/server/lib
ln -sf %{_logdir}/tomcat $RPM_BUILD_ROOT/%{_tomcatdir}/logs
ln -sf %{_sysconfdir}/tomcat $RPM_BUILD_ROOT/%{_tomcatdir}/conf

gzip -9nf *.txt LICENSE

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*.sh
%dir %{_tomcatdir}/common/classes
%dir %{_tomcatdir}/classes
%dir %{_tomcatdir}/server
%dir %{_tomcatdir}/server/classes
%dir %{_tomcatdir}/webapps
%dir %{_tomcatdir}/work
%dir %{_sysconfdir}/tomcat
%dir %{_logdir}/tomcat
%{_bindir}/*.jar
%{_javalibdir}/*.jar
%{_tomcatdir}/bin
%{_tomcatdir}/common/lib
%{_tomcatdir}/conf
%{_tomcatdir}/jasper
%{_tomcatdir}/lib
%{_tomcatdir}/logs
%{_tomcatdir}/server/lib
%{_tomcatdir}/webapps/*
%{_sysconfdir}/tomcat/*

%files doc
%defattr(644 root root 755)
%doc catalina/docs/*
