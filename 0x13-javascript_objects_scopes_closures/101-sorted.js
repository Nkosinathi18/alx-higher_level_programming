#!/usr/bin/node
const dict = require('./101-data').dict;

const totalist = Object.entries(dict);
const vals = Object.values(dict);
const valsUniq = [...new Set(vals)];
const newDict = {};
for (const p in valsUniq) {
  const list = [];
  for (const q in totalist) {
    if (totalist[q][1] === valsUniq[p]) {
      list.unshift(totalist[q][0]);
    }
  }
  newDict[valsUniq[p]] = list;
}
console.log(newDict);
