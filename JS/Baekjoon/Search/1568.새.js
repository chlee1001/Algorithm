const [n] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')

let N = Number(n);
let count = 0;
let song = 0;

while (N > 0) {
    song += 1;
    if (N - song < 0) {
        song = 1;
    }
    N -= song;
    count += 1

}
console.log(count)

