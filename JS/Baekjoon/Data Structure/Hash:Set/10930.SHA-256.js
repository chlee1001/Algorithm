// 백준 10930번 SHA-256

const [input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const crypto = require('crypto');

async function sha256(message) {
    // encode as UTF-8
    const msgBuffer = new TextEncoder().encode(message);
    // hash the message
    return crypto.createHash('sha256').update(msgBuffer).digest('hex');
}
sha256(input).then(hashResult => console.log(hashResult));