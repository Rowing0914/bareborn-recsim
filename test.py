from recsim.environments.interest_evolution import create_environment as iv_create_environment
from recsim.environments.interest_exploration import create_environment as ie_create_environment
from recsim.environments.long_term_satisfaction import create_environment as lts_create_environment

env_config = {
    "slate_size": 3,
    "seed": 2022,
    "num_candidates": 10,
    "resample_documents": False
}

# env = ie_create_environment(env_config)
# env = iv_create_environment(env_config)
env = lts_create_environment(env_config)

obs = env.reset()
for t in range(10):
    action = env.action_space.sample()
    obs, reward, done, info = env.step(action=action)
    print(obs, reward, done, info)
