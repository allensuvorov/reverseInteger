console.log (reverse(123));
// console.log (reverse(-12345));
// console.log ((-234)%10);
console.log (10);
/*
 @param {number} x
 @return {number}
 */

function reverse(x) {
    
    let rx = 0; //reversed x
    
    for (let int = x; Math.abs(int) > 0; int = Math.floor(int/10)) {
        rx *= 10;
        rx += int % 10;
    };
    
    return rx;
};
