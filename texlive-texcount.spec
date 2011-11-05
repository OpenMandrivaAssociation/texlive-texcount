# revision 23293
# category Package
# catalog-ctan /support/texcount
# catalog-date 2011-07-29 16:36:04 +0200
# catalog-license lppl
# catalog-version 2.3
Name:		texlive-texcount
Version:	2.3
Release:	1
Summary:	Count words in a LaTeX document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/texcount
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texcount.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texcount.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-texcount.bin = %{EVRD}
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
TeXcount is a Perl script that counts words in the text of
LaTeX files. It has rules for handling most of the common
macros, and can provide colour-coded output showing which parts
of the text have been counted. The package script is available
as a Web service via its home page.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/texcount
%{_texmfdistdir}/scripts/texcount/texcount.pl
%doc %{_texmfdistdir}/doc/support/texcount/QuickReference.pdf
%doc %{_texmfdistdir}/doc/support/texcount/QuickReference.tex
%doc %{_texmfdistdir}/doc/support/texcount/README
%doc %{_texmfdistdir}/doc/support/texcount/TeXcount.pdf
%doc %{_texmfdistdir}/doc/support/texcount/TeXcount.tex
%doc %{_texmfdistdir}/doc/support/texcount/macros.tex
%doc %{_texmfdistdir}/doc/support/texcount/sub_addrules.tex
%doc %{_texmfdistdir}/doc/support/texcount/sub_options.tex
%doc %{_texmfdistdir}/doc/support/texcount/sub_tc_other.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/texcount/texcount.pl texcount
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
