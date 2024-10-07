from dynaconf import Dynaconf

settings = Dynaconf(settings_files=['config.toml'])

# Accessing values
print(settings.api)  # Accesses the value of "debug"
# print(settings.database_url)  # Accesses the value of "database_url"