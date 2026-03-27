var areSimilar = function(mat, k) {
    const n = mat.length;
    const m = mat[0].length;
    k %= m;

    for (let r = 0; r < n; r++) {
        const row = mat[r];
        let shifted;

        if (r % 2 === 0) {
            // shift right
            shifted = row.slice(m - k).concat(row.slice(0, m - k));
        } else {
            // shift left
            shifted = row.slice(k).concat(row.slice(0, k));
        }

        // compare arrays
        for (let i = 0; i < m; i++) {
            if (row[i] !== shifted[i]) {
                return false;
            }
        }
    }

    return true;
};
