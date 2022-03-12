// SPDX-License-Identifier: MIT

pragma solidity >=0.6.6 <0.9.0;

/*
How to run this in Remix

1. Go to sidebar > "DEPLOY & RUN TRANSACTIONS"
2. Click "Deploy" to deploy contract 
3. Click "fund". This simulates the act of funding an account
4. Copy address from "ACCOUNT"
5. Paste address into variable "amountFundedByAddress" to view value. 
6. Viewed value should be zero
7. Change "VALUE" to 20 (or any amount > 0)
8. Repeat step 3 > 5
9. Viewed value should be 20 (or the amount set in step 7)

Click "Deploy"
*/
contract FundMe {
    mapping(address => uint256) public amountFundedByAddress;

    /*
    msg is a solidity keyword
    msg.sender is the address who called the contract
    msg.amount is the amount
    */
    function fund()public payable {
        amountFundedByAddress[msg.sender] += msg.value;
    }

    /*
    require is a solidity keyword

    require(condition boolean, errMessage string)

    check is condition is true
    If false, it'll revert (i.e. return user their eth
    */
    function fundWithMinimum() public payable {  
        uint256 MIN_WEI = 20;
        require(msg.value > MIN_WEI, "Insufficient wei");
    }

    /*
    address(this) gets the current contract

    This function transfers current contract's balance to msg.sender
    */
    function withdraw() payable public {
        uint256 currentBalanceOfContract = address(this).balance;
        payable(msg.sender).transfer(currentBalanceOfContract);
    }
}