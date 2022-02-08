from brownie import config, accounts


def get_account():
    return accounts.add(config["wallets"]["from_key"])
