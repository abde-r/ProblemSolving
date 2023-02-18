var inputs: string[] = readline().split(' ');
const LX: number = parseInt(inputs[0]);
const LY: number = parseInt(inputs[1]);
const TX: number = parseInt(inputs[2]);
const TY: number = parseInt(inputs[3]);

let x=TX,y=TY

while (true) {
    const remainingTurns: number = parseInt(readline());
    let dx='',dy=''
    if (LX > x)
    {
        dx='E'
        x++
    }
    else if (LX < x)
    {
        dx='W'
        x--
    }
    else
        dx=''
    if (LY > y)
    {
        dy='S'
        y++
    }
    else if (LY < y)
    {
        dy='N'
        y--
    }
    else
        dy = ''
    console.log(dy+dx)
}

