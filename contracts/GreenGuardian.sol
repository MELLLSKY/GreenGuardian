// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract LandToken {

// Struct containing basic information about the land
  struct Land {
    address institution;
    string location;
    uint256 area;
    bool active;
  }

// Struct containing token information for the land
  struct Token {
    uint256 tokenId;
    uint256 landId;
    bool active;
  }

// Mapping to store lands and tokens
  mapping(uint256 => Land) public lands;
  mapping(uint256 => Token) public tokens;

// Mapping to associate institutions with their corresponding landId values
  mapping(address => uint256) public institutionLands;

// Modifier to grant permission to add land
  modifier onlyInstitution() {
    require(msg.sender == lands[institutionLands[msg.sender]].institution, "You do not have permission for this operation.");
    _;
  }

// Function to add land
  function addLand(uint256 _landId, string memory _location, uint256 _area) public onlyInstitution {
    Land storage land = lands[_landId];
    require(land.institution == address(0), "Land already added.");
     
    land.institution = msg.sender;
    land.location = _location;
    land.area = _area;
    land.active = true;

// Store the institution's landId in the institutionLands mapping
    institutionLands[msg.sender] = _landId;

// Create a token
    Token storage token = tokens[_landId];
    token.tokenId = _landId;
    token.landId = _landId;
    token.active = true;
  }

// Function to update land information
  function updateLand(uint256 _landId, string memory _location, uint256 _area) public onlyInstitution {
    Land storage land = lands[_landId];
    require(land.institution == msg.sender, "You do not have permission to update this land.");

land.location = _location;
    land.area = _area;
  }

// Function to query token status
  function tokenStatus(uint256 _landId) public view returns (bool) {
    Token storage token = tokens[_landId];
    return token.active;
  }
}
