export default function appendToEachArrayValue(array, appendString) {
    const appendedArray = [];
    for (const idx of array) {
      appendedArray.push(appendString + idx);
    }
    return appendedArray;
  }
