Name:		texlive-texcount
Version:	3.1
Release:	2
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

%description
TeXcount is a Perl script that counts words in the text of
LaTeX files. It has rules for handling most of the common
macros, and can provide colour-coded output showing which parts
of the text have been counted. The package script is available
as a Web service via its home page.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/texcount
%{_texmfdistdir}/scripts/texcount
%doc %{_texmfdistdir}/doc/support/texcount

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
