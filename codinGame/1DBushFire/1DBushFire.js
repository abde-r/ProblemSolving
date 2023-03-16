const N = parseInt(readline());
for (let i = 0; i < N; i++) {
    const line = readline();
    let count=0;
    for (let x=0; x<line.length; x++)
    {
        if (line[x] == 'f' && (line[x+1] == 'f' || line[x+2] == 'f'))
        {
            count+=1;
            x+=2;
        }
        else if (line[x] == 'f' && (line[x+1] != 'f' || line[x+2] != 'f'))
            count+=1;
    }
    console.log(count)
}

