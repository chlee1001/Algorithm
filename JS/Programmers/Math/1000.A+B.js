const stdin = require('fs').readFileSync('/dev/stdin').toString().split(' ');

console.log(parseInt(stdin[0], 10) + parseInt(stdin[1], 10));
