# Evolutionary design of machine-learning-predicted bulk metallic glasses

Code and data associated with the publication "Evolutionary design of
machine-learning-predicted bulk metallic glasses".

doi:xyz

## Instructions

The code in this repository utilises a number of other packages to run genetic
algorithms, evaluate machine-learning models, and visualise predictions. For
optimisation of properties discussed in the paper, a model trained to predict
those properties must be available - such a model can be created using
techniques discussed in our previous publication
(https://doi.org/10.1039/D2DD00026A) using the
[cerebral](https://github.com/Robert-Forrest/cerebral) package. The
[evomatic](https://github.com/Robert-Forrest/evomatic) package is used here to
perform genetic algorithm searching.

To prepare to run this code, execute the following:

```
git clone https://github.com/Robert-Forrest/EvolutionaryDesignOfBMGs
cd EvolutionaryDesignOfBMGs
python3 -m pip install -r requirements.txt
```

There are various YAML configuration file examples provided demonstrating
searching scenarios with different targets and constraints. The example
congfiguration for a simple search for high-Dmax alloy compositions may be
invoked as follows:

```
python3 __main__.py Dmax.yaml
```

Custom YAML files may easily be created and invoked in a similar way. 

Running __main__.py will perform the search as configured, and will output a
variety of figures and data-files to the output directory, describing the alloy
population it observed.
