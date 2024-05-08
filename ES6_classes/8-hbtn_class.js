/* 8-hbtn_class.js */

class HolbertonCourse {
    constructor(size, location) {
      this._size = size;
      this._location = location;
    }
  
    get size() {
      return this._size;
    }
  
    set size(newSize) {
      this._size = newSize;
    }
  
    get location() {
      return this._location;
    }
  
    set location(newLocation) {
      this._location = newLocation;
    }
  
    [Symbol.toPrimitive](hint) {
      if (hint === 'number') {
        return this._size;
      } if (hint === 'string') {
        return this._location;
      }
      return this;
    }
  }
  
  export default HolbertonCourse;
