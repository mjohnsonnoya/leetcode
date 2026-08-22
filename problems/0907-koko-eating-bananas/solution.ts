function minEatingSpeed(piles: number[], h: number): number {
    let r = Math.max(...piles);
    let l = 1;

    function isValidSpeed(speed: number) {
        let hours = h;
        for (const pile of piles) {
            hours -= Math.ceil(pile / speed);
        }
        return (hours < 0) ? false : true;
    }

    while (l < r) {
        const m = Math.floor((r + l)/2);
        if (!isValidSpeed(m)) {
            l = m + 1;
        }

        else {
            r = m;
        }
    }

    return l;
};
