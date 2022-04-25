#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-DescTools
Version  : 0.99.44
Release  : 46
URL      : https://cran.r-project.org/src/contrib/DescTools_0.99.44.tar.gz
Source0  : https://cran.r-project.org/src/contrib/DescTools_0.99.44.tar.gz
Summary  : Tools for Descriptive Statistics
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-DescTools-lib = %{version}-%{release}
Requires: R-BH
Requires: R-Exact
Requires: R-Rcpp
Requires: R-data.table
Requires: R-expm
Requires: R-gld
Requires: R-mvtnorm
Requires: R-rstudioapi
BuildRequires : R-BH
BuildRequires : R-Exact
BuildRequires : R-Rcpp
BuildRequires : R-data.table
BuildRequires : R-expm
BuildRequires : R-gld
BuildRequires : R-mvtnorm
BuildRequires : R-rstudioapi
BuildRequires : buildreq-R

%description
<!-- badges: start -->
[![CRAN
status](https://www.r-pkg.org/badges/version-last-release/DescTools)](https://CRAN.R-project.org/package=DescTools)
[![downloads](https://cranlogs.r-pkg.org/badges/grand-total/DescTools)](https://CRAN.R-project.org/package=DescTools)
[![downloads](http://cranlogs.r-pkg.org/badges/last-week/DescTools)](https://CRAN.R-project.org/package=DescTools)
[![License: GPL
v2+](https://img.shields.io/badge/License-GPL%20v2+-blue.svg)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)
[![Lifecycle:
maturing](https://img.shields.io/badge/lifecycle-maturing-blue.svg)](https://lifecycle.r-lib.org/articles/stages.html)
[![R build
status](https://github.com/AndriSignorell/DescTools/workflows/R-CMD-check/badge.svg)](https://github.com/AndriSignorell/DescTools/actions)
[![pkgdown](https://github.com/AndriSignorell/DescTools/workflows/pkgdown/badge.svg)](https://andrisignorell.github.io/DescTools/)
<!-- badges: end -->

%package lib
Summary: lib components for the R-DescTools package.
Group: Libraries

%description lib
lib components for the R-DescTools package.


%prep
%setup -q -c -n DescTools
cd %{_builddir}/DescTools

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640999612

%install
export SOURCE_DATE_EPOCH=1640999612
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library DescTools
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library DescTools
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library DescTools
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc DescTools || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/DescTools/CITATION
/usr/lib64/R/library/DescTools/DESCRIPTION
/usr/lib64/R/library/DescTools/INDEX
/usr/lib64/R/library/DescTools/Meta/Rd.rds
/usr/lib64/R/library/DescTools/Meta/data.rds
/usr/lib64/R/library/DescTools/Meta/demo.rds
/usr/lib64/R/library/DescTools/Meta/features.rds
/usr/lib64/R/library/DescTools/Meta/hsearch.rds
/usr/lib64/R/library/DescTools/Meta/links.rds
/usr/lib64/R/library/DescTools/Meta/nsInfo.rds
/usr/lib64/R/library/DescTools/Meta/package.rds
/usr/lib64/R/library/DescTools/Meta/vignette.rds
/usr/lib64/R/library/DescTools/NAMESPACE
/usr/lib64/R/library/DescTools/NEWS
/usr/lib64/R/library/DescTools/R/DescTools
/usr/lib64/R/library/DescTools/R/DescTools.rdb
/usr/lib64/R/library/DescTools/R/DescTools.rdx
/usr/lib64/R/library/DescTools/data/Rdata.rdb
/usr/lib64/R/library/DescTools/data/Rdata.rds
/usr/lib64/R/library/DescTools/data/Rdata.rdx
/usr/lib64/R/library/DescTools/demo/DescTools.R
/usr/lib64/R/library/DescTools/demo/describe.r
/usr/lib64/R/library/DescTools/demo/plots.R
/usr/lib64/R/library/DescTools/doc/Combinatorics.pdf
/usr/lib64/R/library/DescTools/doc/Combinatorics.pdf.asis
/usr/lib64/R/library/DescTools/doc/DescToolsCompanion.pdf
/usr/lib64/R/library/DescTools/doc/DescToolsCompanion.pdf.asis
/usr/lib64/R/library/DescTools/doc/TablesInR.pdf
/usr/lib64/R/library/DescTools/doc/TablesInR.pdf.asis
/usr/lib64/R/library/DescTools/doc/index.html
/usr/lib64/R/library/DescTools/extdata/R.ico
/usr/lib64/R/library/DescTools/extdata/key.ico
/usr/lib64/R/library/DescTools/help/AnIndex
/usr/lib64/R/library/DescTools/help/DescTools.rdb
/usr/lib64/R/library/DescTools/help/DescTools.rdx
/usr/lib64/R/library/DescTools/help/aliases.rds
/usr/lib64/R/library/DescTools/help/figures/bartext.png
/usr/lib64/R/library/DescTools/help/figures/faces.png
/usr/lib64/R/library/DescTools/help/paths.rds
/usr/lib64/R/library/DescTools/html/00Index.html
/usr/lib64/R/library/DescTools/html/R.css
/usr/lib64/R/library/DescTools/tests/TestsPseudoR2.R
/usr/lib64/R/library/DescTools/tests/misc.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/DescTools/libs/DescTools.so
/usr/lib64/R/library/DescTools/libs/DescTools.so.avx2
/usr/lib64/R/library/DescTools/libs/DescTools.so.avx512
