const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("LandToken", function () {
  let landToken;
  let institutionAddress;

  beforeEach(async function () {
    [landToken, institutionAddress] = await ethers.getSigners();
  });

});
it("should add land successfully", async function () {
  const landId = 1;
  const location = "New York";
  const area = 1000;

  await expect(
    landToken.addLand(landId, location, area)
  ).to.emit(landToken, "LandAdded");

  const land = await landToken.lands(landId);
  expect(land.institution).to.equal(institutionAddress);
  expect(land.location).to.equal(location);
  expect(land.area).to.equal(area);
  expect(land.active).to.equal(true);
});

it("should prevent adding land twice", async function () {
  const landId = 1;
  const location = "New York";
  const area = 1000;

  await landToken.addLand(landId, location, area);

  await expect(
    landToken.addLand(landId, location, area)
  ).to.be.revertedWith("Land already added.");
});
it("should update land information successfully", async function () {
  const landId = 1;
  const newLocation = "London";
  const newArea = 2000;

  await landToken.addLand(landId, "New York", 1000);

  await landToken.updateLand(landId, newLocation, newArea);

  const land = await landToken.lands(landId);
  expect(land.location).to.equal(newLocation);
  expect(land.area).to.equal(newArea);
});

it("should prevent unauthorized updates", async function () {
  // Deploy a second instance of the contract as a different institution
  const otherInstitution = await ethers.getSigners();
  const otherLandToken = await otherInstitution[0].deploy(LandToken);

  await landToken.addLand(1, "New York", 1000);

  await expect(
    otherLandToken.connect(otherInstitution[0]).updateLand(1, "London", 2000)
  ).to.be.revertedWith("You do not have permission to update this land.");
});

it("should return the token status correctly", async function () {
  const landId = 1;
  const expectedStatus = true;

  await landToken.addLand(landId, "New York", 1000);

  const status = await landToken.tokenStatus(landId);
  expect(status).to.equal(expectedStatus);
});
