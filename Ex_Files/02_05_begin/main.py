import os

DEVELOPMENT = "development"
PRODUCTION = "production"
STAGING = "staging"
CODE_SPACE = "code_space"
LOCAL = "local"

current_env = os.environ.get("ENV_NAME", DEVELOPMENT)#allows you to access the env that you're running on and grab things from there
#to change the ENV_NAME, type export ENV_NAME='*insert env name*' into the terminal and then run"

if current_env == DEVELOPMENT:
    print("Development environment")
elif current_env == PRODUCTION:
    print("Production environment")
elif current_env == STAGING:
    print("Staging environment")
elif current_env in [CODE_SPACE, LOCAL]: #checking a collection of things
    print("Codespace or local environment")
else:
    print("Unknown environment")
