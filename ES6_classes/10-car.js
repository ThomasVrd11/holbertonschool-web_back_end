#!/usr/bin/env node
/* 10-cars.js */

class Car {
    constructor(brand, motor, color) {
      this._brand = brand;
      this._motor = motor;
      this._color = color;
    }
  
    cloneCar() {
    /* Clone this car */
      return new this.constructor(this._brand, this._motor, this._color);
    }
  }
  
  export default Car;
