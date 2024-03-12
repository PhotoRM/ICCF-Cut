# ICCFCut

**ICCF-Cut** is proposed by [Ma et al. 2023](https://iopscience.iop.org/article/10.3847/1538-4357/acc4c1) for broadband PRM and is used to extract the emission line lightcurve with two broadband lightcurves.

ICCF-Cut simply needs two broadband lightcurves:
* a band which contains the broad emission line Halpha (`line band`);
* a band which is adjacent to the line band and nearly contains no emission line components (`continuum band`).

In addition, ICCF-Cut needs the `ratio` of the broad emission line in the line band, which can be determined from the single-epoch spectrum of the AGN.

Then, you can try:

    $ python iccfcut.py [continuum band filename] [line band filename] [ratio]

to extract the Halpha lightcurve. Each lightcurve file should contain 3 columns: `MJD`, `FLux` and `Flux error`.

Please note that there is a variable `gap` that needs to be set manually in `iccfcut.py`.
It should be a list with:
* length equal to the observational seasons of the lightcurves;
* the *i* th value of `gap` should be larger than the last observation date of the *i* th season, but less than the first observation date of the *i+1* th season.

You are welcome to use and modify ICCF-Cut, and please acknowledge its use with a citation to:

* [Ma et al. 2023](https://iopscience.iop.org/article/10.3847/1538-4357/acc4c1)
* Ma et al. 2024 (in preparation).
