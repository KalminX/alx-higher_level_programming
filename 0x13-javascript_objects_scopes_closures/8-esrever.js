#!/usr/bin/node

exports.esrever = function (list) {
  let len = list.length;
  const count = len / 2;
  len -= 1;
  for (let i = 0; i < count; i++) {
    [list[i], list[len - i]] = [list[len - i], list[i]];
  }
  return list;
};
