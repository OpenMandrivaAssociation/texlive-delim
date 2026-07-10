%global tl_name delim
%global tl_revision 23974

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Simplify typesetting mathematical delimiters
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/delim
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/delim.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/delim.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/delim.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package permits simpler control of delimiters without excessive use
of \big... commands (and the like).

