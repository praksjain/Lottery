from brownie import Lottery, accounts, network, config
from dotenv import load_dotenv

load_dotenv()

LOCAL_BLOKCHN_ENVTS = ["hardhat", "development", "ganache", "mainnet-fork"]


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if network.show_active() in LOCAL_BLOKCHN_ENVTS:
        return accounts[0]
    if id:
        return accounts.load(id)
    return accounts.add(config["wallets"]["from-key"])


def deploy_and_create():
    account = get_account()
    lottery = Lottery.deploy({"from": account})
    tx = lottery.startLottery({"from": account})
    tx.wait(1)


def main():
    deploy_and_create()
