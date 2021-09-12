import gym
from rl_helper import fps
if __name__=="__main__":

    env = gym.make('Pendulum-v0')
    env.reset()
    fps(env)