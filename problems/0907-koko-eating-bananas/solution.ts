function minEatingSpeed(piles: number[], h: number): number {
    let l = 1;
    let r = Math.max(...piles);

    function isValid(speed: number) {
        let timeleft = h;

        for (const pile of piles) {
            const time = Math.ceil(pile/speed);
            timeleft -= time;
        }

        return timeleft >= 0;
    }

    while (l < r) {
        const m = Math.floor((l + r)/2);

        if (isValid(m)) {
            r = m;
        }

        else {
            l = m + 1;
        }
    }

    return l;
};
