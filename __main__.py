from omegaconf import OmegaConf

import evomatic as evo

conf = OmegaConf.load("config.yaml")

evo.setup(dict(conf))

evo.evolve()
