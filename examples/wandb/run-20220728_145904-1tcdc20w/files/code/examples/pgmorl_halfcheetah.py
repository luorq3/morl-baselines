import mo_gym
from morl_baselines.pgmorl.pgmorl import PGMORL

if __name__ == "__main__":
    algo = PGMORL(env_id="mo-halfcheetah-v4", num_envs=4, pop_size=1, warmup_iterations=1, evolutionary_iterations=1, limit_env_steps=100000)
    algo.train()
