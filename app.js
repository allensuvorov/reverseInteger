
/*
@param {number} x
@return {number}
*/

console.log (reverse(123));
console.log (reverse(-123));
console.log (reverse(120));

function reverse(x) {
    
    let rx = 0; //reversed x
    for (let int = x; Math.abs(int) > 0; int = Math.trunc(int/10)) {
        rx *= 10;
        rx += int % 10; // take the end digit of int and add to the reversed x 
        // console.log("stack: ",rx, int)
    };
    return rx;
};
