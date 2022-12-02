"""Evolutionary design of machine-learning-predicted bulk metallic glasses."""

import argparse

import pandas as pd
from omegaconf import OmegaConf
import seaborn as sns
import metallurgy as mg

import evomatic as evo


if __name__ == "__main__":

    sns.set()

    parser = argparse.ArgumentParser()
    parser.add_argument("config", default="config.yaml", nargs="?", type=str)
    args = parser.parse_args()
    conf = OmegaConf.load(args.config)

    evolver_conf = dict(conf.evolver)

    repeats = conf.get("repeats", 1)
    overall_history = pd.DataFrame([])
    for i in range(repeats):
        evolver = evo.Evolver(**evolver_conf)

        history = evolver.evolve()
        overall_history = pd.concat(
            [overall_history, history["alloys"]], ignore_index=True
        )

        output_directory = conf.get("output_directory", "./output")
        if repeats > 1:
            output_directory += "/" + str(i)

        evolver.output_results(output_directory=output_directory)

    for target in (
        evolver_conf["targets"]["minimise"] + evolver_conf["targets"]["maximise"]
    ):
        composition_weighted_average = mg.analyse.composition_weighted_average(
            overall_history["alloy"], overall_history[target]
        )

        mg.plots.periodic_table(
            composition_weighted_average, output_filename=target + ".png"
        )
