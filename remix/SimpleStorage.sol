// SPDX-License-Identifier: MIT

pragma solidity >=0.6.0 <0.9.0;

contract SimpleStorage {
    
    struct User {
        uint256 id;
        string name;
        string password;
    }

    uint256 idCounter = 0;

    mapping(uint256 => User) public UserById;

    function signUp(string memory _name, string memory _password) public returns(User memory) {
        idCounter++;
        User memory user = User(idCounter, _name, _password);
        UserById[idCounter] = user;

        return user;
    }

    function getUser(uint256 id) public view returns (User memory) {
        return UserById[id];
    }

}