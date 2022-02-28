// SPDX-License-Identifier: MIT

pragma solidity >=0.6.0 <0.9.0;
import "./SimpleStorage.sol";

contract StorageFactory {
    SimpleStorage[] public simpleStorageArray;

    function createSimpleStorageContract() public {
        SimpleStorage s = new SimpleStorage();
        simpleStorageArray.push(s);
    }
}