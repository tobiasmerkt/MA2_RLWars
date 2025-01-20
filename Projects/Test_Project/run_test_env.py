from magent2.environments import test_env_v0
import numpy as np
from pettingzoo.utils import random_demo

map_size = 45
env = test_env_v0.env(map_size=map_size, render_mode='human', minimap_mode=True)
env.reset()
state = np.array(env.state())
print(state[:15,:15,2:4])
print(np.shape(state))
# random_demo(env, render=True, episodes=1)