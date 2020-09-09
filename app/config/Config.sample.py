import os


class Config(object):


    def __init__(self):

        self.data = {
            'ip': '0.0.0.0',
            'port': 8080,
            'import_name': __name__,
            'instance_path': None,
            'instance_relative_config': True,
            'debug': True,
            'testing': True,
            'timezone': 'UTC',
            'date_format': '%m%d%y',
            'secret_key': 'kkYtz4BVRATXQ4NDTDLdcsJ2',
            'database_uri': 'sqlite:////' + os.getcwd() + '/app/data/default.db',
            'sqlalchemy_track_modifications': False,
            'enable_internal_log': True,
            'internal_log_file_path': 'app/logs/error_log',
            'internal_log_max_bytes': 2097152,
            'internal_log_backup_count': 10,
            'database_log_backup_count': 10,
            'limit': {
                'soft': 100,
                'hard': 1000
            }
        }

        ###
        # In production mode, the settings below takes priority overriding the ones above.
        ###
        if os.getenv('APP_PROD_' + self.data['secret_key']) is not None:
            if os.getenv('APP_PROD_' + self.data['secret_key']):
                self.data['debug'] = False
                self.data['testing'] = False