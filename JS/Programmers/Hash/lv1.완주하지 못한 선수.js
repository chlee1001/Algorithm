function solution(participant, completion) {
    let dic = completion.reduce((obj, t) => (obj[t] = obj[t] ? obj[t] + 1 : 1, obj), {});
    console.log(dic);
    return participant.find(t => {
        if (dic[t]) {
            dic[t] = dic[t] - 1
        } else {
            return true;
        }
    })
}


const case1 = {participant: ["leo", "kiki", "eden"], completion: ["eden", "kiki"]}
const case2 = {
    participant: ["marina", "josipa", "nikola", "vinko", "filipa"],
    completion: ["josipa", "filipa", "marina", "nikola"]
}
const case3 = {participant: ["mislav", "stanko", "mislav", "ana"], completion: ["stanko", "ana", "mislav"]}

console.log(
    solution(case2.participant, case2.completion))
