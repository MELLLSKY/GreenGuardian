// test.js

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
    // Register a user
    await user.registerCustomer("John", "Doe", 1, 30, "john@example.com", "123 Main St");

    // Get user info
    const userInfo = await user.getCustomerInfo();
    expect(userInfo[0]).to.equal("John");
    expect(userInfo[1]).to.equal(30);
    expect(userInfo[2]).to.equal("123 Main St");

    // Update user info
    await user.updateCustomerInfo("newEmail@example.com", "456 Side St");

    // Get updated user info
    const updatedUserInfo = await user.getCustomerInfo();
    expect(updatedUserInfo[0]).to.equal("John");
    expect(updatedUserInfo[1]).to.equal(30);
    expect(updatedUserInfo[2]).to.equal("456 Side St");

    // Register a company
    await company.registerCompany("ABC Corp", "123456", "Jane Smith");

    // Get company info
    const companyInfo = await company.getCompanyInfo();
    expect(companyInfo[0]).to.equal("ABC Corp");
    expect(companyInfo[1]).to.equal("123456");
    expect(companyInfo[2]).to.equal("Jane Smith");

    // Update company info
    await company.updateCompanyInfo("XYZ Inc", "654321", "John Doe");

    // Get updated company info
    const updatedCompanyInfo = await company.getCompanyInfo();
    expect(updatedCompanyInfo[0]).to.equal("XYZ Inc");
    expect(updatedCompanyInfo[1]).to.equal("654321");
    expect(updatedCompanyInfo[2]).to.equal("John Doe");

    // Create land
    awai

