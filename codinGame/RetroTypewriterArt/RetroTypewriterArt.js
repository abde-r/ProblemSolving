const T = readline();

function checkIt(s) {
    for (let i=0; i < s.length; i++)
        if (!(s[i] >= '0' && s[i] <= '9'))
            return 0
    return 1
} 

let s = T.split(' ')
for (let i=0; i<s.length; i++)
{
    if (s[i] == 'nl')
        console.log('')
    else if (checkIt(s[i]))
    {
        let count = ''
        for (let j=0; j<s[i].length-1; j++)
            count += s[i][j]
        count = parseInt(count)
        for (let x=0; x < count; x++)
            process.stdout.write(s[i][s[i].length-1])
    }
    else
    {
        let count = 0
        let j=0
        let temp = ''
        for (; s[i][j] >= '0' && s[i][j] <= '9'; j++)
            count += s[i][j]
        count = parseInt(count)
        for (; j < s[i].length; j++)
            temp += s[i][j]

        if (temp == 'sp')
            for (let x=0; x < count; x++)
                process.stdout.write(' ')
        else if (temp == 'bS')
            for (let x=0; x < count; x++)
                process.stdout.write('\\')
        else if (temp == 'sQ')
            for (let x=0; x < count; x++)
                process.stdout.write('\'')
        else
            for (let x=0; x < count; x++)
                process.stdout.write(temp)
    }
}

