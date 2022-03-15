// SPDX-License-Identifier: MIT

pragma solidity >=0.6.6 <0.9.0;


contract Modifier {

    /*1. set ownerAddress to whoever deployed this contract*/
    address ownerAddress;
    constructor(){
        ownerAddress = msg.sender;
    }
    
    /*2. Example of normal function*/
    function forAnyoneToCall() public view returns (string memory greeting){
        return "Hello!";
    }

    /*3. Example of function with require, without modifier*/
    function ownerOnly() public view returns (string memory greeting) {
        require(msg.sender == ownerAddress, "Only for owner");
        return "Hello!";
    }


    /*4. Example of function with modifier*/
    modifier myOnlyOwnerModifier {
        require(msg.sender == ownerAddress, "Only for owner");
        _;
    }
    function ownerOnlyWithModifier() public view myOnlyOwnerModifier returns(string memory greeting) {
        return "Hello!";
    }
}