# COVID-19 USA Logistic Model
Code for modelling estimated prevalence and incidence rates of coronavirus cases in the United States from data reported by the New York Times <a href="https://github.com/nytimes/covid-19-data">repository</a>. The growth model utilizes a logistic function to estimate cumulative cases (prevalence) and daily rates of new cases (incidence) of COVID-19. Reported case data can then be fitted to the function using a non-linear least-squares optimization method available in optimize.curve_fit in SciPy.

Initial case data reported for California (05-April-2020) was fitted to the function with high shared variance (r^2>0.85) for both prevalence and indicence curves.

Model can be used to show the potential effects of mitigation (i.e., social distancing, lockdown, etc.) on the spread of coronavirus in the USA. The indicence rate (daily growth) curve should be used to demonstrate the effects of these efforts on "flattening" the curve since the prevalence curve will plateau at the defined population capacity (Nmax). Simply enter the growth rate and population max for the region of interest.

Any questions, please contact
<a href="mailto:arnelaguinaldo@pointloma.edu">arnelaguinaldo@pointloma.edu</a>.

Arnel Aguinaldo, PhD, ATC<br>
Assistant Professor, Kinesiology<br>
Point Loma Nazarene University
