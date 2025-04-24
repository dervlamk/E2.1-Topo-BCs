# Optimizing Topographic Boundary Conditions for East Pacific Climate Simulation

by D. Meegan-Kumar1, G. Elsaesser2,3, D. S. Battisti4, C. M. Colose2,5, J. Wu2,6, J. S. Sexton1, & J. W. Baldwin1,7

1Department of Earth System Science, University of California Irvine, Irvine, California, USA<br>
2NASA Goddard Institute for Space Studies, New York, New York<br>
3Department of Applied Physics and Mathematics, Columbia University, New York, New York<br>
4Department of Atmospheric Science, University of Washington, Seattle, Washington<br>
5Autonomic Integra, LLC, New York, New York
6Center for Climate Systems Research, The Earth Institute, Columbia University, New York, New York<br>
7Lamont-Doherty Earth Observatory, Columbia University, Palisades, New York

Status: _This paper is published in Journal of Climate [DOI: 10.1175/JCLI-D-24-0316.1](https://journals.ametsoc.org/view/journals/clim/aop/JCLI-D-24-0316.1/JCLI-D-24-0316.1.xml). Relevant model output and observational/reanalysis data are available at [https://zenodo.org/records/13941966](https://zenodo.org/records/13941966). We welcome any comments, questions, or suggestions. Please email your feedback to dervlak@uci.edu._

Abstract: Overly-smooth topography in general circulation models (GCMs) underestimates the blocking effect of the steep mountain ranges flanking the eastern Pacific. We explore the impact of this bias on common biases in Pacific climate simulation (i.e. the unrealistic cross-equatorial symmetry of near-surface winds, sea surface temperatures (SST), and precipitation) through sensitivity experiments with modified Central and/or South American topography in an atmosphere-ocean coupled GCM. Quantifying orographic blocking potential via the Froude number, we determine that an envelope topographic interpolation scheme best captures observed blocking patterns. Implementing envelope topography only in Central America reduced model biases as greater blocking of the trade winds warmed SST and enhanced convergence in the northeastern Pacific. Doing so additionally over the Andes improved the simulation of south Pacific circulation and the South Pacific Convergence Zone as stronger deflection of the westerlies intensified the South Pacific Anticyclone. This mitigated convection biases in the southeast Pacific by increasing subsidence and cooling SST, however, remote impacts of the Andes exacerbated the dry bias in the northeast tropical Pacific, resulting in negligible improvement in the east Pacific double-ITCZ. We find that, due to the significant role of large-scale convergence in driving precipitation patterns, other model biases, such as cloud-radiative biases, may modulate the impact of altering topography. Our results highlight the importance of considering alternate methods for calculating model topographic boundary conditions, though the optimal interpolation scheme will vary with model resolution and the impact of topography on GCM biases can be sensitive to choices made in formulating parameterizations. 


# Project Organization
```
├── README.md          <- Top-level README for developers using this project
│
├── notebooks/         <- Jupyter notebooks that call functions from scripts/
│
├── scripts/           <- Source code for use in this project (e.g., scripts to clean and visualize data)
│   ├── colorbar_funcs.py    
│   ├── data_funcs.py
│   ├── dynamics_funcs.py
│   └── stats_funcs.py     
│
├── gcm_analysis.yml    <- File for reproducing the analysis environment
```

# Acknowledgements
This work is supported by NASA NIP Grant 80NSSC21K1735 awarded to J.W.B. Computing resources for data analysis were provided by the NASA High-End Computing (HEC) Program through the NASA Center for Climate Simulation (NCCS) at the Goddard Space Flight Center. Additional contributions by G.S.E. were supported by the NASA Modeling, Analysis and Prediction Program and APAM-GISS Cooperative Agreement 80NSSC18M0133, as well as NASA Precipitation Measurement Missions grant 80NSSC22K0609. We thank Reto Reudy and Maxwell Kelley at NASA GISS for their assistance with the E2.1 simulations.


_______

Repository template from @savannahferretti

