%global tl_name texcount
%global tl_revision 79618
%global tl_bin_links texcount:%{_texmfdistdir}/scripts/texcount/texcount.pl

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.1.1
Release:	%{tl_revision}.1
Summary:	Count words in a LaTeX document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/texcount
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texcount.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texcount.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(texcount.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
TeXcount is a Perl script that counts words in the text of LaTeX files.
It has rules for handling most of the common macros, and can provide
colour-coded output showing which parts of the text have been counted.
The package script is available as a Web service via its home page.

