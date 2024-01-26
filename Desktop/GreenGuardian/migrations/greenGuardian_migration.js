const GreenGuardian = artifacts.require("GreenGuardian");

module.exports = function(deployer){
    deployer.deploy(GreenGuardian);
};