import logging

def get_config(name):

    config = {}

    if name.upper() == 'ARID':
        config['num_classes'] = 10
    else:
        logging.error("Configs for dataset '{}'' not found".format(name))
        raise NotImplemented

    logging.debug("Target dataset: '{}', configs: {}".format(name.upper(), config))

    return config


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.DEBUG)
    logging.info(get_config("ARID"))
