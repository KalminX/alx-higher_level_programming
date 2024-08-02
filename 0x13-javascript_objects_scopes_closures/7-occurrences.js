#!/usr/bin/node

function nbOccurences(list, searchElement) {
  let count = 0;
  list.forEach((element) => {
    if (element === searchElement) count += 1;
  });
  return count;
};

module.exports.nbOccurences = nbOccurences;
