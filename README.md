
# On multi-dimensional (discrete, non-parametric) goodness-of-fit tests

1. [About the MINEN test](#minentest)
1. [Some About the A-D test](#adtest)
1. [About the K-S test](#kstest)
    1. [Multi-dimensional](#kstestmulti)
1. [About the DNN test](#dnntest)
1. [About the Li test](#litest)



<a name="minentest"></a>
## About the MINEN test

This [CV answer][11] mentions the `ndtest` [Python code][12]. It is a
translation of the Matlab `minentest` function from the [`multdist` code][14].

> implements Aslan & Zech's and Szekely & Rizzo's test based on an analogy to
statistical energy, which is minimized when the two samples are drawn from
the same parent distribution

The main references for this method appear to be:

* [Statistical energy as a tool for binning-free, multivariate goodness-of-fit
tests, two-sample comparison and unfolding][16], Aslan & Zech (2005)
* [Energy statistics: A class of statistics based on distances][17], Szekely &
Rizzo (2014)

The `multdist` package is now developed as part of the [`highdim` code][15].

Recently, the [`energy` package][18] by Maria Rizzo (written in `R`) and the 
[code's manual][19] became available.



<a name="adtest"></a>
## About the A-D test

[Multi-dimensional Anderson-Darling statistic based goodness-of-fit test for
spectrum sensing][1], Gurugopinath & Samudhyatha (2015)

> (..) we propose a multi-dimensional extension of the Anderson-Darling
statistic based goodness-of-fit lest for spectrum sensing in a cognitive radio
network with multiple nodes.



<a name="kstest"></a>
## About the K-S test

The [ASAIP][5] article [Beware the Kolmogorov-Smirnov test!][4] by Feigelson &
Babu states that:

> KS test probabilities are wrong if the model was derived from the dataset.
>
> The KS test can not be applied in two or more dimensions.
>
> we recommend that astronomers replace the Kolmogorov-Smirnov test with the
similar, but more sensitive, Anderson-Darling test.

The CV question [Why can't one generalize the Kolmogorov-Smirnov test to 2
or more dimensions?][3] is related to this article. Regarding the statement that
"*The KS test can not be applied in two or more dimensions*", user **Glen_b**
says:

> As stated, this seems too strong.
>
> (..) difficulties have been considered in several ways in a number of papers
that yield bivariate/multivariate versions of Kolmogorov-Smirnov statistics that
don't suffer from that problem.

and **whuber** comments:

> I find the OP's reference of dubious quality (at the outset it misinterprets
what hypothesis tests mean), it finally admits that "the bootstrap can come to
the rescue, and significance levels for the particular multidimensional
statistic and the particular dataset under study can be numerically computed."

so the dismissal of the K-S test by Feigelson & Babu is downplayed. This article
also mentions several references on the topic.


<a name="kstestmulti"></a>
### Multi-dimensional

The article [The two-dimensional Kolmogorov-Smirnov test][6] by Lopes, Reid &
Hobson (2007) compares:

> three variations on the Kolmogorov-Smirnov test for multi-dimensional data
sets are surveyed: Peacock’s test (..) Fasano and Franceschini’s test (..)
Cooke’s test
>
> Adapting goodness-of-fit tests to multi-dimensional space is generally seen as
a challenge. Tests based on binning face the hurdle of what is called in the
literature "the curse of dimensionality"

About Cooke's test they mention:

> We show that his test is not a faithful variation of Peacock’s test and that
the upper-bound for computing it is incorrectly stated

Apparently, only the two-dimensional case is addressed in this article. The
references for the methods compared are:

* [Two-dimensional goodness-of-fit testing in astronomy][8], Peacock (1983)

> (..) Two new statistical tests are developed. The first is a two-dimensional
version of the Kolmogorov–Smirnov test, for which the distribution of the test
statistic is investigated using a Monte Carlo method. This test is found in
practice to be very nearly distribution-free, and empirical formulae for the
confidence levels are given.

* [A multidimensional version of the Kolmogorov-Smirnov test][7], Fasano and
Franceschini (1987)

> The authors discuss a generalization of the classical Kolmogorov-Smirnov test,
which is suitable to analyse random samples defined in two or three dimensions.
This test provides some improvements with respect to an earlier version proposed
by Peacock.

Cooke's method does not appear to have a valid reference and I could not find
it online.

This [answer][10] in CV mentions "*A two-dimensional extension of the
Kolmogorov-Smirnov test*" in the article:

[A multivariate Kolmogorov-Smirnov test of goodness of fit][9] Justel, Peña &
Zamar (1997)

> This paper presents a distribution-free multivariate Kolmogorov-Smirnov
goodness-of-fit test. The test uses a statistic which is built using
Rosenblatt's transformation and an algorithm is developed to compute it in the
bivariate case. An approximate test, that can be easily computed in any
dimension, is also presented. The power of these multivariate tests is studied
in a simulation study.




<a name="dnntest"></a>
## About the DNN test

[Estimation of Goodness-of-Fit in Multidimensional Analysis Using Distance to
Nearest Neighbor][2], Narsky (2003)

> A new method for calculation of goodness of multidimensional fits in particle
physics experiments is proposed. This method finds the smallest and largest
clusters of nearest neighbors for observed data points. The cluster size is used
to estimate the goodness-of-fit and the cluster location provides clues about
possible problems with data modeling. The performance of the new method is
compared to that of the likelihood method and Kolmogorov-Smirnov test using toy
Monte Carlo studies.



<a name="litest"></a>
## About the Li test

[A nonparametric test for equality of distributions with mixed categorical and
continuous data][13], Li, Maasoumi & Racined (2009)

> In this paper we consider the problem of testing for equality of two density
or two conditional density functions defined over mixed discrete and continuous
variables. We smooth both the discrete and continuous variables, with the
smoothing parameters chosen via least-squares cross-validation. The test
statistics are shown to have (asymptotic) normal null distributions. However, we
advocate the use of bootstrap methods in order to better approximate their null
distribution in finite-sample settings and we provide asymptotic validity of the
proposed bootstrap method. Simulations show that the proposed tests have better
power than both conventional frequency-based tests and smoothing tests based on
ad hoc smoothing parameter selection, while a demonstrative empirical
application to the joint distribution of earnings and educational attainment
underscores the utility of the proposed approach in mixed data settings.



________________________________________________________________________________
[1]: https://ieeexplore.ieee.org/document/7458396
[2]: https://arxiv.org/abs/physics/0306171
[3]: https://stats.stackexchange.com/q/100124/10416
[4]: https://asaip.psu.edu/Articles/beware-the-kolmogorov-smirnov-test
[5]: https://asaip.psu.edu
[6]: https://bura.brunel.ac.uk/handle/2438/1166
[7]: http://adsabs.harvard.edu/abs/1987MNRAS.225..155F
[8]: https://academic.oup.com/mnras/article/202/3/615/967854
[9]: https://www.sciencedirect.com/science/article/pii/S0167715297000205
[10]: https://stats.stackexchange.com/a/27353/10416
[11]: https://stats.stackexchange.com/a/200884/10416
[12]: https://github.com/syrte/ndtest
[13]: https://www.sciencedirect.com/science/article/pii/S0304407608002054
[14]: https://github.com/brian-lau/multdist
[15]: https://github.com/brian-lau/highdim
[16]: http://adsabs.harvard.edu/abs/2005NIMPA.537..626
[17]: http://www.sciencedirect.com/science/article/pii/S0378375813000633
[18]: https://github.com/mariarizzo/energy
[19]: https://cloud.r-project.org/web/packages/energy/index.html
