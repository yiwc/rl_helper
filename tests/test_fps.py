# print("please install mujoco-py")
import gym
from rl_helper import envhelper,fps
if __name__=="__main__":

    env = gym.make('Pendulum-v0')
    env.reset()
    fps(env)