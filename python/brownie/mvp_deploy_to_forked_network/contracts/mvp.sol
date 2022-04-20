// SPDX-License-Identifier: MIT

pragma solidity >=0.6.0 <0.9.0;

contract MVP {
    
    string public greeting;

    function setGreeting(string memory _greeting) public returns (string memory){
        greeting = _greeting;
        return greeting;
    }

    function getGreeting() public view returns (string memory){
        return greeting;
    }
}