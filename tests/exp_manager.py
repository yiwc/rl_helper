import gym
from rl_helper import ExperimentManager


model_name="ppo"
exp_class="try"
exp_target="PPOSolvePendulum_v0"
comments="show ppo with sde can solve pendulum"
sub_id=0
e=ExperimentManager()
e.init(model_name=model_name,exp_target=exp_target,comments=comments,exp_class=exp_class,sub_id=sub_id)
e.add_para("n_envs",4)
e.add_para('env',"Pendulum-v0")
e.add_para('use_sde',True)
e.add_para('sde_sample_freq',50000)
e.add_para('total_timesteps',3000000)
e.add_para("policy","MlpPolicy")
e.start(overwrite=True)

print(e.model_save_pth)

# Train your Model ....
    # env = make_vec_env(e.paras.env, n_envs=e.paras.n_envs)
    # model = PPO(e.paras.policy, env, verbose=1, use_sde=e.paras.use_sde, sde_sample_freq=e.paras.sde_sample_freq, tensorboard_log=e.log_save_dir_pth)
    # model.learn(total_timesteps=e.paras.total_timesteps)
    # model.save(e.model_save_pth)

# Test

# load your exp configs
e=ExperimentManager(add_env_helper=True)
e.load("runs/try/PPOSolvePendulum_v0/0/9f856")

# you can directly use its configs/paras e.paras.xxx
env = gym.make(e.paras.env)
obs = env.reset()
e.env_helper.recording(env)
e.env_helper.recording(env)
e.env_helper.recording(env)
e.save_gif(times=3)
