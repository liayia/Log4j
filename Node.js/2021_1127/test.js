//console.log( "a,b,c,d".split("c") )
//[ 'a,b,', ',d' ]

//new Array(10).fill(0).map((v,i)=>-i).reduce((a,b)=>a+b);
//-45

//let main = ()=>{ let a = -123; if(a>0){ var b = 456; }else{ var b = 789; const c = 0; }; console.log(a,b,c); } main(); 
//SyntaxError: Unexpected identifier

//let func1 = async () => 12; let func2 = () => 25; let main = async ()=>{ func1() .then(async r1=>{ let r2 = await func2(); console.log(r1,r2); }) .catch(err=>{ console.log("Error!"); }) }; main(); 
//12 25