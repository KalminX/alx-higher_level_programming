#!/usr/bin/node
exports.callMeMoby = function (n, func) {
  while (n > 0) {
    func();
    n--;
  }
};
