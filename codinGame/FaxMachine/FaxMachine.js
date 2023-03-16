const w = parseInt(readline());
const h = parseInt(readline());
const t = readline();

let s = t.split(' ')

let r = []
for (let i=0; i<s.length; i++)
{
    if (i%2 == 0)
        // for x in range(int(r[i])):
        for (let x=0; x<parseInt(s[i]); x++)
            r.push('*')
    else
        for (let x=0; x<parseInt(s[i]); x++)
            r.push(' ')
}

let x=0
let i=0

while (i<r.length)
{
    if (!x)
        process.stdout.write('|')
    if (x<w)
    {
        process.stdout.write(r[i])
        x++
        i++
    }
    else
    {
        console.log('|')
        x=0
    }
}
console.log('|')

