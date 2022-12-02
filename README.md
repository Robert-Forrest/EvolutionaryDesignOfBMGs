# Evolutionary design of machine-learning-predicted bulk metallic glasses

Code and data associated with the publication "Evolutionary design of
machine-learning-predicted bulk metallic glasses".

doi:xyz

## Instructions

The code in this repository utilises a number of other packages to run genetic
algorithms, evaluate those machine-learning models, and visualise
predictions. For optimisation of properties discussed in the paper, a model
trained to predict those properties must be available - such a model can be
created using techniques discussed in our previous publication
(https://doi.org/10.1039/D2DD00026A) using the
[cerebral](https://github.com/Robert-Forrest/cerebral) package.

To run this code, execute the following:

```
git clone https://github.com/Robert-Forrest/EvolutionaryDesignOfBMGs
cd EvolutionaryDesignOfBMGs
python3 -m pip install -r requirements.txt
python3 __main__.py config.yaml
```



