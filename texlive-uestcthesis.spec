# revision 33194
# category Package
# catalog-ctan /macros/latex/contrib/uestcthesis
# catalog-date 2014-03-16 10:59:31 +0100
# catalog-license lppl1.3
# catalog-version 1.0.0
Name:		texlive-uestcthesis
Version:	1.0.0
Release:	5
Summary:	Thesis class for UESTC
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/uestcthesis
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uestcthesis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uestcthesis.doc.tar.xz
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
%{_texmfdistdir}/bibtex/bst/uestcthesis/uestcthesis.bst
%{_texmfdistdir}/tex/latex/uestcthesis/uestcthesis.cls
%doc %{_texmfdistdir}/doc/latex/uestcthesis/README
%doc %{_texmfdistdir}/doc/latex/uestcthesis/doc/chapters/DuplicateMe.tex
%doc %{_texmfdistdir}/doc/latex/uestcthesis/doc/chapters/Place_has_TrainDAO.java.tex
%doc %{_texmfdistdir}/doc/latex/uestcthesis/doc/chapters/implementation.tex
%doc %{_texmfdistdir}/doc/latex/uestcthesis/doc/chapters/math.tex
%doc %{_texmfdistdir}/doc/latex/uestcthesis/doc/chapters/test.c.tex
%doc %{_texmfdistdir}/doc/latex/uestcthesis/doc/chapters/tuition.tex
%doc %{_texmfdistdir}/doc/latex/uestcthesis/doc/contents/Cabstract.tex
%doc %{_texmfdistdir}/doc/latex/uestcthesis/doc/contents/Eabstract.tex
%doc %{_texmfdistdir}/doc/latex/uestcthesis/doc/contents/acknowledgements.tex
%doc %{_texmfdistdir}/doc/latex/uestcthesis/doc/contents/appendix.tex
%doc %{_texmfdistdir}/doc/latex/uestcthesis/doc/contents/cv.tex
%doc %{_texmfdistdir}/doc/latex/uestcthesis/doc/contents/original.tex
%doc %{_texmfdistdir}/doc/latex/uestcthesis/doc/contents/publications.bib
%doc %{_texmfdistdir}/doc/latex/uestcthesis/doc/contents/reference.bib
%doc %{_texmfdistdir}/doc/latex/uestcthesis/doc/contents/titlepage.tex
%doc %{_texmfdistdir}/doc/latex/uestcthesis/doc/contents/translation.tex
%doc %{_texmfdistdir}/doc/latex/uestcthesis/doc/packagecheck.tex
%doc %{_texmfdistdir}/doc/latex/uestcthesis/doc/pics/Chrysanthemum.jpg
%doc %{_texmfdistdir}/doc/latex/uestcthesis/doc/pics/Penguins.jpg
%doc %{_texmfdistdir}/doc/latex/uestcthesis/doc/pics/Tulips.jpg
%doc %{_texmfdistdir}/doc/latex/uestcthesis/doc/pics/apk.png
%doc %{_texmfdistdir}/doc/latex/uestcthesis/doc/pics/excel.png
%doc %{_texmfdistdir}/doc/latex/uestcthesis/doc/pics/fisher1.png
%doc %{_texmfdistdir}/doc/latex/uestcthesis/doc/pics/fisher2.png
%doc %{_texmfdistdir}/doc/latex/uestcthesis/doc/pics/flow1.png
%doc %{_texmfdistdir}/doc/latex/uestcthesis/doc/pics/flow3.png
%doc %{_texmfdistdir}/doc/latex/uestcthesis/doc/pics/flow4.png
%doc %{_texmfdistdir}/doc/latex/uestcthesis/doc/pics/flow5-1.png
%doc %{_texmfdistdir}/doc/latex/uestcthesis/doc/pics/flow5-2.png
%doc %{_texmfdistdir}/doc/latex/uestcthesis/doc/pics/flow5-3.png
%doc %{_texmfdistdir}/doc/latex/uestcthesis/doc/pics/highlight1.png
%doc %{_texmfdistdir}/doc/latex/uestcthesis/doc/pics/highlight2.png
%doc %{_texmfdistdir}/doc/latex/uestcthesis/doc/pics/system.png
%doc %{_texmfdistdir}/doc/latex/uestcthesis/doc/pics/winedt.png
%doc %{_texmfdistdir}/doc/latex/uestcthesis/doc/uestcthesis-doc.pdf
%doc %{_texmfdistdir}/doc/latex/uestcthesis/doc/uestcthesis-doc.tex
%doc %{_texmfdistdir}/doc/latex/uestcthesis/source/uestcthesis.dtx
%doc %{_texmfdistdir}/doc/latex/uestcthesis/source/uestcthesis.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
