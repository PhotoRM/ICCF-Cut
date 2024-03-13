# ICCF-Cut

**ICCF-Cut**, proposed by [Ma et al. 2023](https://iopscience.iop.org/article/10.3847/1538-4357/acc4c1), is a tool designed for broadband PRM. It extracts the emission line lightcurve with two broadband lightcurves.

ICCF-Cut simply needs two broadband lightcurves:
* a `line band` which contains the broad emission line Halpha;
* a `continuum band` which is adjacent to the line band and nearly contains no emission line components.

In addition, ICCF-Cut needs the `ratio` of the broad emission line in the line band, i.e. the flux of the broad emission line divided by the total flux of the line band. This can be determined from a single-epoch spectrum of the AGN.

Then, you can try:

    $ python iccfcut.py [continuum band filename] [line band filename] [ratio]

to extract the Halpha lightcurve. Each input lightcurve file should contain 3 columns: `MJD`, `FLux` and `Flux error`. The output lightcurve file for the emission line is `Halpha.txt`.

Please note that there is a variable `gap` that needs to be set manually in `iccfcut.py`.
It should be a list with:
* length equal to the observational seasons of the lightcurves;
* the *i* th value of `gap` should be larger than the last observation date of the *i* th season, but less than the first observation date of the *i+1* th season.

We provide an example of Mrk 841 in `Example` directory. To extract the Halpha lightcurve of Mrk 841, you can try:

    $ python iccfcut.py Mrk841g.txt Mrk841r.txt 0.18


You are welcome to use and modify ICCF-Cut. If you do, please acknowledge its use with a citation to:

* [Ma et al. 2023](https://iopscience.iop.org/article/10.3847/1538-4357/acc4c1)
* Ma et al. 2024 (in preparation).
