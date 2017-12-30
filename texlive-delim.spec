# revision 23974
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-delim
Version:	1.0
Release:	1
Summary:	TeXLive delim package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/delim.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/delim.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/delim.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive delim package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/delim/delim.sty
%doc %{_texmfdistdir}/doc/latex/delim/README
%doc %{_texmfdistdir}/doc/latex/delim/delim.pdf
#- source
%doc %{_texmfdistdir}/source/latex/delim/delim.dtx
%doc %{_texmfdistdir}/source/latex/delim/delim.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111104-2
+ Revision: 750884
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111104-1
+ Revision: 718214
- texlive-delim
- texlive-delim
- texlive-delim

