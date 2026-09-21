function isPalindrome(s: string): boolean {
    s = s.toLowerCase();
    function isAlphaNumeric(c: string): boolean {
        if (c.charCodeAt(0) >= 'a'.charCodeAt(0) && c.charCodeAt(0) <= 'z'.charCodeAt(0)) {
            return true;
        }

        else if (c.charCodeAt(0) >= '0'.charCodeAt(0) && c.charCodeAt(0) <= '9'.charCodeAt(0)) {
            return true;
        }

        else {
            return false;
        }
    }

    let l = 0;
    let r = s.length - 1;

    while (l < r) {
        while (l < r && !isAlphaNumeric(s[l])) {
            l += 1;
        }

        while (l < r && !isAlphaNumeric(s[r])) {
            r -= 1;
        }

        if (s[l] !== s[r]) {
            return false;
        }

        l += 1;
        r -= 1;
    }

    return true;


};
