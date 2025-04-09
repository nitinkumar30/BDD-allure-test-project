import configparser


def read_config(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    return config


def get_config_value(file_path, key):
    config = read_config(file_path)
    return config.get('DEFAULT', key)  # Use 'DEFAULT' section by default


def get_loginPage_xpath_value(key):
    return get_config_value('xpaths/loginPage.properties', key)


def get_property_value(key):
    return get_config_value('config.properties', key)
