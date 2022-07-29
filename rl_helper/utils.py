def get_envname(env):
    try:
        env_name=env.spec.id
    except Exception as err:
        print(err)
        env_name=str(env).split(" ")[0].replace("<","-").replace(">","-").strip("-")
    return env_name