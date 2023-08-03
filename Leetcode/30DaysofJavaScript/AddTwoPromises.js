var addTwoPromises = async function(promise1, promise2) {
    let r = await Promise.all([promise1, promise2])
    return r[0]+r[1]
};

