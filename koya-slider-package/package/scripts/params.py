from resource_management import *

config = Script.get_config()


app_root = config['configurations']['global']['app_root']
java64_home = config['hostLevelParams']['java_home']
app_user = config['configurations']['global']['app_user']
pid_file = config['configurations']['global']['pid_file']
app_log_dir = config['configurations']['global']['app_log_dir']
kafka_version = config['configurations']['global']['kafka_version']

conf_dir = format("{app_root}/config")
brokerConfig = config['configurations']['broker'].copy()
brokerConfig['broker.id'] = int(config['configurations']['global']['app_container_tag']) - 1

