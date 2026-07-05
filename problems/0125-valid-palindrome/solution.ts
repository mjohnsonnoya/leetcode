function isPalindrome(s: string): boolean {
    s = s.toLowerCase();
    function isAlphaNumeric(s: string): boolean {
        if (s.charCodeAt(0) >= 'a'.charCodeAt(0) && s.charCodeAt(0) <= 'z'.charCodeAt(0)) {
            return true;
        }
        if (s.charCodeAt(0) >= '0'.charCodeAt(0) && s.charCodeAt(0) <= '9'.charCodeAt(0)) {
            return true;
        }
        return false;
    }

    let l = 0;
    let r = s.length - 1;

    while (l <= r) {
        while (l < r && !isAlphaNumeric(s[l])) {
            l++;
        }

        while (l < r && !isAlphaNumeric(s[r])){
            console.log("trigger 2");
            r--;
        }

        if (s[l] !== s[r]) {
            return false;
        }
        console.log("trigger 3");
        l += 1;
        r -= 1;
    }
    return true;
};
