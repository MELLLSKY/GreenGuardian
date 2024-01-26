const { expect } = require("chai");
const { ethers } = require("hardhat"); 

describe("Contracts Integration Test", function () {
    let DataObjectStore;
    let User;
    let Company;
    let Lands;

    let dataObjectStore;
    let user;
    let company;
    let lands;

    beforeEach(async function () {
        // Deploy DataObjectStore contract
        DataObjectStore = await ethers.getContractFactory("DataObjectStore");
        dataObjectStore = await DataObjectStore.deploy();
        await dataObjectStore.deployed();

        // Deploy User, Company, and Lands contracts with DataObjectStore address
        User = await ethers.getContractFactory("User", { libraries: { DataObjectStore: dataObjectStore.address } });
        user = await User.deploy(dataObjectStore.address);
        await user.deployed();

        Company = await ethers.getContractFactory("Company", { libraries: { DataObjectStore: dataObjectStore.address } });
        company = await Company.deploy(dataObjectStore.address);
        await company.deployed();

        Lands = await ethers.getContractFactory("Lands", { libraries: { DataObjectStore: dataObjectStore.address } });
        lands = await Lands.deploy(dataObjectStore.address);
        await lands.deployed();
    });

    it("Should register a user, update user info, register a company, update company info, and create land", async function () {

        //example
        await user.registerCustomer("Melise", "Kaya", 1, 30, "mell@example.com", "123 St");
        const userInfo = await user.getCustomerInfo();
        expect(userInfo[0]).to.equal("Melise");
        expect(userInfo[1]).to.equal(30);
        expect(userInfo[2]).to.equal("123 St");
    });
});
