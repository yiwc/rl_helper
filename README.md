# rl_helper
A few easy to use helper tools for your RL related works.

## Tools we have
- Experiment Manager
- GIF Recorder
- FPS
- Keyboard Interactor

## Install

    pip install rl-helper

# Tools



## GIF recorder

It helps you record your gym into gif. See the example [tests/play_gym.py](tests/play_gym.py).

    import gym
    from rl_helper import envhelper

    env = gym.make('CartPole-v1')
    gym_env_helper=envhelper()  # * 1. Init your env helper

    for episode in range(2): 
        obs = env.reset()
        for step in range(30):
            action = env.action_space.sample()  
            action = policy(observation)
            nobs, reward, done, info = env.step(action)
            if done:
                break
            gym_env_helper.recording(env) # * 2. Record the frame
        env.close()

    gym_env_helper.save_gif(times=3) # * 3. Save to gif


Find the GIF in the folder [runs / EnvID / YYYYMMDD-HrMinSc.gif](runs/)

<img src="runs/CartPole-v1/20210825-175235.gif" height=125>

<img src="runs/Pendulum-v0/20210825-175459.gif" height=125>


<br/>

------



## FPS test

    env = gym.make('Pendulum-v0')
    env.reset()
    fps(env)

------

## Keyboard Interactor

    import gym
    from rl_helper.keyboard import kbinteractor
    interactor=kbinteractor(env=gym.make('FetchPickAndPlaceDense-v1'),
            key2action={
                    'right':[1,0,0,0],
                    'left':[-1,0,0,0],
                    'up':[0,1,0,0],
                    'down':[0,-1,0,0],
                    "y":[0,0,1,0],
                    "h":[0,0,-1,0],
                    "n":[0,0,0,1],
                    "b":[0,0,0,-1],
                })

![d](runs/keyboard_interact.png) 