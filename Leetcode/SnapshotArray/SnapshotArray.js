var SnapshotArray = function(length) {
    this.t = [...Array(length)].map(() => new Map())
    this.x = 0
};

SnapshotArray.prototype.set = function(index, val) {
    this.t[index].set(this.x, val)
};

SnapshotArray.prototype.snap = function() {
    return this.x++
};

SnapshotArray.prototype.get = function(index, snap_id) {
    while (snap_id>=0)
    {
        if (this.t[index].has(snap_id))
            return this.t[index].get(snap_id)
        snap_id--
    }
    return 0
};

