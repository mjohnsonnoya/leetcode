function isPalindrome(s: string): boolean {
    // make all the letters lowercase first
    s = s.toLowerCase();
    function isAlphanumeric(c: string): boolean {
        // check if letters
        if (c.charCodeAt(0) >= 'a'.charCodeAt(0) && c.charCodeAt(0) <= 'z'.charCodeAt(0)){
            return true;
        }

        // check if numbers
        else if (c.charCodeAt(0) >= '0'.charCodeAt(0) && c.charCodeAt(0) <= '9'.charCodeAt(0)) {
            return true;
        }

        else { 
            return false;
        };
    }

    let l = 0;
    let r = s.length - 1;

    while (l < r) {
        // advance past non alphanumeric characters
        while (l < r && !isAlphanumeric(s[l])) {
            l += 1;
        }

        while (l < r && !isAlphanumeric(s[r])) {
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
