// test/calculateNumber.test.js
const { expect } = require('chai');
const calculateNumber = require('../path/to/your/calculateNumber'); // Adjust the path accordingly

describe('calculateNumber', function() {
  
  it('should return the sum of two rounded numbers', function() {
    expect(calculateNumber('SUM', 1.4, 2.3)).to.equal(3);
    expect(calculateNumber('SUM', 1.5, 2.5)).to.equal(4);
  });

  it('should return the difference of two rounded numbers', function() {
    expect(calculateNumber('SUBTRACT', 5.5, 2.2)).to.equal(3);
    expect(calculateNumber('SUBTRACT', 3.7, 1.2)).to.equal(3);
  });

  it('should return the division of two rounded numbers', function() {
    expect(calculateNumber('DIVIDE', 5.5, 2.2)).to.equal(2.5);
    expect(calculateNumber('DIVIDE', 3.5, 1.5)).to.equal(2);
  });

  it('should return "Error" when dividing by zero', function() {
    expect(calculateNumber('DIVIDE', 5.5, 0)).to.equal('Error');
  });

  it('should handle invalid operation types gracefully', function() {
    expect(calculateNumber('INVALID', 1, 2)).to.be.undefined;
  });

});