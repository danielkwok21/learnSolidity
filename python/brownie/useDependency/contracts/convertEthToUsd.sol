// SPDX-License-Identifier: MIT

pragma solidity >=0.6.6 <0.9.0;

import "smartcontractkit/chainlink@1.2.1/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract ConvertEthToUsd {
    AggregatorV3Interface internal ethToUsdPriceFeed;

    constructor() public {
        address rinkebyEthToUsdPriceFeedAddress = 0x8A753747A1Fa494EC906cE90E9f37563A8AF630e;
        ethToUsdPriceFeed = AggregatorV3Interface(
            rinkebyEthToUsdPriceFeedAddress
        );
    }

    function getLatestEthPriceInUsd() public view returns (int256) {
        (
            ,
            int256 price,
            ,
            ,

        ) = ethToUsdPriceFeed.latestRoundData();

        return price / (10**8);
    }
}
