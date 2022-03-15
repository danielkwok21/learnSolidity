// SPDX-License-Identifier: MIT

pragma solidity >=0.6.6 <0.9.0;


contract Voting {

    struct Voter {
        bool isVoted;
        string proposalName;
        address voterAddress;
    }

    struct Proposal {
        string name;
    }

    address public chairPerson;

    mapping(address => Voter) public voterByAddress;
    mapping(string => uint256) public numberOfVotesByProposal;
    
    /*
    An array is kept here to allow for
    looping at getWinningProposalName()
    */
    Proposal[] proposals;

    constructor(string[] memory proposalNames){
        /*
        Initiates mapping with all proposal to have votes of 1, instead of 0
        This is because there is no such thing as empty value in solidity
        uint256 defaults to 0
        string defaults to ""        
        */
        for(uint i = 0; i<proposalNames.length; i++){
            string memory name = proposalNames[i];
            Proposal memory p = Proposal({name: name});
            numberOfVotesByProposal[p.name] = 1;

            proposals.push(p);
        }

        /*
        Set chairperson as initial contract address
        */
        chairPerson = msg.sender;
    }

    function registerVoter(address voterAddress) public {
        require(msg.sender == chairPerson, "Only chairperson is allowed to register voter");
        require(voterByAddress[voterAddress].voterAddress == address(0) , "Voter is already registered");

        voterByAddress[voterAddress] = Voter({
            isVoted: false,
            proposalName: "",
            voterAddress: voterAddress
        });
    }

    function vote(string memory proposalName) public {
        require(numberOfVotesByProposal[proposalName]!=0, "Invalid proposal name");
        require(voterByAddress[msg.sender].voterAddress != address(0), "Voter is not registered yet");
        require(!voterByAddress[msg.sender].isVoted, "Voter has already voted");

        voterByAddress[msg.sender].isVoted = true;
        voterByAddress[msg.sender].proposalName = proposalName;

        numberOfVotesByProposal[proposalName] += 1;
    }

    function getWinningProposalName() public view returns (string memory wpn) {
        uint256 highestNumberOfVotes = 0;
        string memory winningProposalName;

        for(uint256 i=0; i<proposals.length; i++){
            Proposal memory p = proposals[i];
            string memory p_name = p.name;

            uint256 numberOfVotes = numberOfVotesByProposal[p_name];
            if(highestNumberOfVotes < numberOfVotes){
                highestNumberOfVotes = numberOfVotes;
                winningProposalName = p_name;
            }
        }

        return winningProposalName;

    }

}