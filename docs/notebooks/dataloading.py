from waymax import config
from waymax import dataloader

scenarios = dataloader.simulator_state_generator(config.WOD_1_1_0_TRAINING)
scenario = next(scenarios)