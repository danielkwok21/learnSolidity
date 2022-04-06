// SPDX-License-Identifier: MIT

pragma solidity >=0.6.6 <0.9.0;

import "smartcontractkit/chainlink@1.2.1/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract Lottery {
    AggregatorV3Interface internal ethToUsdPriceFeed;
    address payable[] public players;

    constructor() {

        address rinkebyEthToUsdPriceFeedAddress = 0x8A753747A1Fa494EC906cE90E9f37563A8AF630e;
        ethToUsdPriceFeed = AggregatorV3Interface(
            rinkebyEthToUsdPriceFeedAddress
        );
    }

    function enter() public payable {
        require(msg.value > 50, "Insufficient eth");
        players.push(payable(msg.sender));
    }

    function getEntraceFeeInWei() public view returns (uint256) {
        uint256 ENTRY_FEE_IN_WEI = 50 * (10**18);
        (
            ,
            /**
            Price of 1 eth in USD, 
            e.g. 350802000000 or $3508.02000000
            Has 8 decimals, because this address specifies it.
            https://docs.chain.link/docs/ethereum-addresses/#Rinkeby%20Testnet
             */
            int256 _usdPerEth,
            ,
            ,

        ) = ethToUsdPriceFeed.latestRoundData();
        /**
        Tally up _usdPerEth to match 18 decimal places
         */
        uint256 usdPerWei = uint256(_usdPerEth) * 10**10;

        uint256 entryFeeInWei = (ENTRY_FEE_IN_WEI * 10**18) / usdPerWei;

        return entryFeeInWei;
    }
}