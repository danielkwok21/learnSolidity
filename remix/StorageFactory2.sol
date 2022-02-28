// SPDX-License-Identifier: MIT

pragma solidity >=0.6.0 <0.9.0;
import "./SimpleStorage.sol";

contract StorageFactory {
    SimpleStorage[] public simpleStorageArray;

    function createSimpleStorageContract() public {
        SimpleStorage s = new SimpleStorage();
        simpleStorageArray.push(s);
    }

    function simpleStorageSignUp(uint256 index, string memory username, string memory password) public {
        SimpleStorage s = simpleStorageArray[index];
        s.signUp(username, password);
    }

    function simpleStorageGetUser(uint256 index, uint256 id) public view returns (SimpleStorage.User memory) {
        SimpleStorage s = simpleStorageArray[index];
        return s.getUser(id);
    }
}