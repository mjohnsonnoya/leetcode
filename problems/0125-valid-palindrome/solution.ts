function isPalindrome(s: string): boolean {
    s = s.toLowerCase();
    function isAlphaNumeric(c: string) {
        const charCode = c.charCodeAt(0);
        if (('a'.charCodeAt(0) <= charCode) && (charCode <= 'z'.charCodeAt(0))) {
            return true;
        }

        else if (('0'.charCodeAt(0) <= charCode) && (charCode <= '9'.charCodeAt(0))) {
            return true;
        }

        else {
            return false;
        }
    }

    let l = 0;
    let r = s.length - 1;

    while (l < r) {
        while (!isAlphaNumeric(s[l]) && (l < r)) {
            l += 1;
        }

        while (!isAlphaNumeric(s[r]) && (l < r)) {
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
