/* enlist-disable */
function cleanSet(set, startString) {
  if (typeof startString !== 'string') {
    return '';
  }

  const filteredValues = new Set();

  for (const value of set) {
    if (typeof value === 'string' && value.startsWith(startString)) {
      const restOfValue = value.slice(startString.length);
      filteredValues.add(restOfValue);
    }
  }

  return Array.from(filteredValues).join('-');
}

export default cleanSet;
