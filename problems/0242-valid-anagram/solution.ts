function isAnagram(s: string, t: string): boolean {
    if (s.length != t.length)
    {
        return false;
    }
    const counts: number[] = new Array(26).fill(0);
    for (let i = 0; i < s.length; i++){
        counts[s.charCodeAt(i) - 'a'.charCodeAt(0)]++;
        counts[t.charCodeAt(i) - 'a'.charCodeAt(0)]--;
    }
    for (const num of counts){
        if (num !== 0){
            return false;
        }
    }
    return true;
    
};
