Name:		texlive-uestcthesis
Version:	36371
Release:	2
Summary:	Thesis class for UESTC
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/uestcthesis
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uestcthesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uestcthesis.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class is for typesetting a thesis at the University of
Electronic Science and Technology of China.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/uestcthesis
%{_texmfdistdir}/tex/latex/uestcthesis
%doc %{_texmfdistdir}/doc/latex/uestcthesis

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
