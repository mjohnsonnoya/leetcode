function minEatingSpeed(piles: number[], h: number): number {
    function validSpeed(speed: number): boolean {
        let timeLeft = h;
        for (const pile of piles) {
            timeLeft -= Math.ceil(pile/speed);
        }

        return timeLeft >= 0;
    }

    let l = 1;
    let r = Math.max(...piles);

    while (l < r) {
        const m = Math.floor((l + r) / 2);
        // console.log("l: ", l);
        // console.log("r: ", r);
        // console.log("m: ", m);

        if (validSpeed(m)) {
            r = m;
        }

        else {
            l = m + 1;
        }
    }

    return l;
};
