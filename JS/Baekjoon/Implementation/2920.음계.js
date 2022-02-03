const [...input] = require('fs').readFileSync('/dev/stdin').toString().trim().split(' ');

let ascending = true;
let descending = true;

for (let i = 1; i < input.length; i++) {
    if (Number(input[i]) > Number(input[i - 1])) {
        descending = false;
    } else if (Number(input[i]) < Number(input[i - 1])) {
        ascending = false;
    }
}

if (ascending) {
    console.log('ascending');
} else if (descending) {
    console.log('descending');
} else {
    console.log('mixed')
}
