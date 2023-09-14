function expensive(L,i) {
  L = L.filter((e,index) => i !== index )
  //console.log(L)
  return L
}

function hard(L) {
  function product(args) {
    let r= args.length > 0 ? args[0] * product(args.slice(1)) : 1
    return r
   }

  let results = new Array(L.length)
  for(let i = 0; i < L.length; ++i) { 
   results[i] = product( expensive(L,i) )

  }
 return results
}


console.log(hard([1, 2, 3, 4, 5]))
console.log(hard([3,2,1]))
