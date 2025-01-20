from magent2.environments import test_env_v0
from pettingzoo.utils import random_demo

map_size = 45
env = test_env_v0.env(map_size=map_size, render_mode='human')
random_demo(env, render=True, episodes=1)