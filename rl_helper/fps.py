import time
def fps(env,steps_per_test=100,episode=10):
    for e in range(episode):
        count=0
        start_t=time.time()
        for i in range(steps_per_test):
            env.step(env.action_space.sample())
        dt=time.time()-start_t
        print("fps = {}".format(steps_per_test/dt))