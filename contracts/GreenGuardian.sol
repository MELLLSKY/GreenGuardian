// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.8.2 <0.9.0;

//Stores and manages data objects for other contracts. 
contract DataObjectStore {
    uint64 instanceId;
    mapping(uint64 => mapping(string => address)) importReferences;
    mapping(uint64 => mapping(string => uint64)) importInstanceIds;
    mapping(string => address) dataObjects;

    constructor(Lands landsContract) {
        dataObjects["Lands"] = address(landsContract);
    }
    
    //Creates a new instance of a DataObjectStore.
    function createInstance() public returns (uint64) {
        return instanceId++;
    }
    //Returns the ID of the most recently created instance.
    function getLatestInstanceId() public view returns (uint64) {
        return instanceId;
    }
    // Retrieves an imported data object.
    function getImportedDataObject(uint64 id, string memory identifier) public view returns (address) {
        return importReferences[id][identifier];
    }
    //Retrieves an imported data object.
    function getImportedDataObjectInstance(uint64 id, string memory identifier) public view returns (uint64) {
        return importInstanceIds[id][identifier];
    }
    //Retrieves a data object by its identifier.
    function getDataObject(string memory identifier) public view returns (address) {
        return dataObjects[identifier];
    }
    //Imports a data object from another contract.
    function importDataObject(uint64 id, string memory identifier, address dataObject, uint64 referenceId) public {
        importReferences[id][identifier] = dataObject;
        importInstanceIds[id][identifier] = referenceId;
    }
}



contract User {
    struct UserInfo {
        string name;
        string surname;
        uint64 userId;
        uint64 age;
        string email;
        string addres;
    }

    mapping(address => UserInfo) public users;

    DataObjectStore _store;

    constructor(DataObjectStore store) {
        _store = store;
    }

    function registerCustomer(string memory name, string memory surname, uint64 userId, uint64 age, string memory email, string memory addres) public {
        users[msg.sender] = UserInfo({
            name: name,
            surname: surname,
            userId: userId,
            age: age,
            email: email,
            addres: addres
        });
    }

    function getCustomerInfo() public view returns (string memory, uint64, string memory) {
        UserInfo storage info = users[msg.sender];
        return (info.name, info.age, info.addres);
    }

    function updateCustomerInfo(string memory newEmail, string memory newAddres) public {
        UserInfo storage info = users[msg.sender];
        info.email = newEmail;
        info.addres = newAddres;
    }
}



contract Company {
    struct CompanyInfo {
        string name;
        string registrationNumber;
        string contactPerson;
    }
    
    mapping(address => CompanyInfo) public companies;
    mapping(uint64 => string) public emergencyNotifications;

    DataObjectStore _store;
    Lands _landsContract;
    address public companyAddress;

    constructor(DataObjectStore store, Lands landsContract) {
        _store = store;
        _landsContract = landsContract;
        companyAddress = address(this);
    }

    function registerCompany(string memory name, string memory registrationNumber, string memory contactPerson) public {
        companies[msg.sender] = CompanyInfo({
            name: name,
            registrationNumber: registrationNumber,
            contactPerson: contactPerson
        });
    }

    function getCompanyInfo() public view returns (string memory, string memory, string memory) {
        CompanyInfo storage info = companies[msg.sender];
        return (info.name, info.registrationNumber, info.contactPerson);
    }

    function updateCompanyInfo(string memory name, string memory registrationNumber, string memory contactPerson) public {
        CompanyInfo storage info = companies[msg.sender];
        info.name = name;
        info.registrationNumber = registrationNumber;
        info.contactPerson = contactPerson;
    }

    function createLand(string memory province, string memory town, string memory street, uint64 latitude, uint64 longitude) public {
    _landsContract.registerLand(province, town, street, latitude, longitude);
    }

    function getLandInfo(uint64 blockId) public view returns (uint64, string memory, string memory, string memory, uint64, uint64) {
        return _landsContract.getLandInfo(blockId);
    }

    function updateLandInfo(string memory province, string memory town, string memory street, uint64 latitude, uint64 longitude) public {
    _landsContract.registerLand(province, town, street, latitude, longitude);
    }

    function getEmergency(address userAddress) public view returns (string memory) {
        // Get user's emergency information
        return _landsContract.getEmergency(userAddress);
    }

    function reportEmergency(address[] memory users, string memory emergencyMessage) public {
        for (uint256 i = 0; i < users.length; i++) {
            // Send emergency alert to users
            _landsContract.reportEmergency(users[i], emergencyMessage);
        }
    }
}


contract Lands {

    //Tokenization
    struct LandInfo {
        uint64 blockId;
        uint64 areaId;
        string province;
        string town;
        string street;
        uint64 latitude;
        uint64 longitude;
    }
    address public _companyContractAddress;
    mapping(uint64 => LandInfo) public lands;
    mapping(address => string) public emergencyNotifications;
    uint64 public latestLandId = 0;
    uint64 public latestBlockId = 0;

    function registerLand(string memory province, string memory town, string memory street, uint64 latitude, uint64 longitude) public {
        latestLandId++;
        latestBlockId++;
        lands[latestLandId] = LandInfo({
            blockId: latestBlockId,
            areaId: latestLandId,
            province: province,
            town: town,
            street: street,
            latitude: latitude,
            longitude: longitude
        });
    }

    function getLandInfo(uint64 landId) public view returns (uint64, string memory, string memory, string memory, uint64, uint64) {
        LandInfo storage info = lands[landId];
        return (info.areaId, info.province, info.town, info.street, info.latitude, info.longitude);
    }
    function getEmergency(address userAddress) public view returns (string memory) {
    // Get emergency message from user
    return emergencyNotifications[userAddress];
    }
    function reportEmergency(address user, string memory emergencyMessage) public {
        emergencyNotifications[user] = emergencyMessage;
    }

}