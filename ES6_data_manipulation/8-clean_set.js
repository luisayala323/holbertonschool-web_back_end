/* enlist-disable */
function cleanSet(set) {
  const cleanedSet = new Set();
  set.forEach((item) => {
    if (item.trim() !== '') {
      cleanedSet.add(item.trim());
    }
  });
  return cleanedSet;
}

export default cleanSet;
