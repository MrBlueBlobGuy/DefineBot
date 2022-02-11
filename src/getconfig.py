from configparser import ConfigParser
config = ConfigParser()

config.read('keys/config.ini')
client_secret = config.get('keys', 'client_secret')
client_id = config.get('keys', 'client_id')
user_agent = config.get('keys', 'user_agent')

input()