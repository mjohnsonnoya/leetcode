function isPalindrome(s: string): boolean {
    function isAlphanumeric(c: string): boolean {
        // check if it's a lowercase letter
        if (c.charCodeAt(0) >= 'a'.charCodeAt(0) && c.charCodeAt(0) <= 'z'.charCodeAt(0)) {
            return true;
        }

        else if (c.charCodeAt(0) >= '0'.charCodeAt(0) && c.charCodeAt(0) <= '9'.charCodeAt(0)) {
            return true
        }

        else {
            return false;
        }
    }

    s = s.toLowerCase();

    let l = 0;
    let r = s.length - 1;

    while (l < r) {
        if (!isAlphanumeric(s[l])) {
            l += 1;
            continue;
        }

        if (!isAlphanumeric(s[r])) {
            r -= 1;
            continue;
        }

        if (s[l] !== s[r]) {
            return false;
        }

        else {
        l += 1;
        r -= 1;
        }
    }
    return true
};
