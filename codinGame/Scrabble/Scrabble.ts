var Points = {
    'e': 1, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'r': 1, 't': 1, 'l': 1, 's': 1, 'u': 1,
    'd': 2, 'g': 2,
    'b': 3, 'c': 3, 'm': 3, 'p': 3,
    'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4,
    'k': 5,
    'j': 8, 'x': 8,
    'q': 10, 'z': 10
}

let t = []

const N: number = parseInt(readline());
for (let i = 0; i < N; i++) {
    const W: string = readline();
    t.push(W)
}

let LETTERS: string = readline();

let s:string = ''
let count:number = 0
for (let i: number=0; i<t.length; i++)
{
    let temp:number = 0
    let w = []
    w = LETTERS.split('')
    for (let j:number=0; j<t[i].length; j++)
    {
        if (w.includes(t[i][j]))
        {
            temp+=Points[t[i][j]]
            try
            {
                const index = w.indexOf(t[i][j]);
                if (index > -1)
                    w.splice(index, 1);
            }
            catch (err)
            {
                temp = -1
                break
            }
        }
        else
        {
            temp =-1
            break
        }
    }
    if (temp > count)
    {
        count = temp
        s = t[i]
    }
}

console.log(s)

