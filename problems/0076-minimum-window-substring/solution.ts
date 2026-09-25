function minWindow(s: string, t: string): string {
    let numNeeded = t.length;

    const count = new Map<string, number>();
    for (const char of t) {
        count.set(char, (count.get(char) ?? 0) + 1);
    }

    let l = 0;

    let leftMin = -1;
    let minLength = Infinity;
    for (let r = 0; r < s.length; r++) {
        let rightChar = s[r];
        count.set(rightChar, (count.get(rightChar) ?? 0) - 1);

        if (count.get(rightChar) >= 0) {
            numNeeded -= 1;
        }

        let leftChar = s[l];
        while (count.get(leftChar) < 0) {
            count.set(leftChar, (count.get(leftChar) ?? 0) + 1);
            l += 1;
            leftChar = s[l];
        }

        if (numNeeded === 0) {
            if ((r - l + 1) < minLength) {
                minLength = r - l + 1;
                leftMin = l;
            }
        }
    }

    if (leftMin !== -1) {
        return s.slice(leftMin, leftMin + minLength);
    }

    else {
        return "";
    }




    


};
